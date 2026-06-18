#!/usr/bin/env python3
"""Scrape all products + tiered variant pricing from bulksupplements.com.

BulkSupplements runs on Shopify, which exposes a public read-only JSON feed at
/products.json (paginated, max 250 per page). We use that instead of parsing
HTML: it is stable, complete, and gives every variant (size tier) with its price.

Outputs (under data/bulksupplements/):
  - products_raw.json          full raw payload (one object per product)
  - bulksupplements_products.csv   one row per product (summary)
  - bulksupplements_variants.csv   one row per variant/size tier (price detail)
"""
from __future__ import annotations

import csv
import html
import json
import os
import re
import sys
import time
import urllib.request
import urllib.error

BASE = "https://www.bulksupplements.com"
PRODUCTS_URL = BASE + "/products.json?limit=250&page={page}"
OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "bulksupplements")
USER_AGENT = (
    "Mozilla/5.0 (compatible; MadeInAmericas-IngredientBot/1.0; "
    "ingredient cost research)"
)
MAX_PAGES = 200          # hard safety cap
SLEEP_BETWEEN = 0.7      # be polite to the server
RETRIES = 4


def fetch(url: str) -> dict:
    last_err = None
    for attempt in range(RETRIES):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=40) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as e:
            last_err = e
            wait = 2 ** attempt
            print(f"  retry {attempt + 1}/{RETRIES} after error: {e} (wait {wait}s)")
            time.sleep(wait)
    raise RuntimeError(f"failed to fetch {url}: {last_err}")


def strip_html(raw: str | None) -> str:
    if not raw:
        return ""
    text = re.sub(r"<[^>]+>", " ", raw)
    text = html.unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def scrape_all() -> list[dict]:
    products: list[dict] = []
    for page in range(1, MAX_PAGES + 1):
        data = fetch(PRODUCTS_URL.format(page=page))
        batch = data.get("products", [])
        if not batch:
            break
        products.extend(batch)
        print(f"page {page}: +{len(batch)} (total {len(products)})")
        time.sleep(SLEEP_BETWEEN)
    return products


def write_outputs(products: list[dict]) -> None:
    os.makedirs(OUT_DIR, exist_ok=True)

    with open(os.path.join(OUT_DIR, "products_raw.json"), "w") as f:
        json.dump(products, f, indent=2)

    prod_csv = os.path.join(OUT_DIR, "bulksupplements_products.csv")
    var_csv = os.path.join(OUT_DIR, "bulksupplements_variants.csv")

    with open(prod_csv, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow([
            "product_id", "product_name", "product_url", "product_type",
            "vendor", "tags", "num_variants", "min_price_usd", "max_price_usd",
            "image_url", "description",
        ])
        for p in products:
            variants = p.get("variants", [])
            prices = [float(v["price"]) for v in variants if v.get("price")]
            images = p.get("images", [])
            w.writerow([
                p.get("id"),
                p.get("title"),
                f"{BASE}/products/{p.get('handle')}",
                p.get("product_type"),
                p.get("vendor"),
                "; ".join(p.get("tags", [])) if isinstance(p.get("tags"), list) else p.get("tags"),
                len(variants),
                min(prices) if prices else "",
                max(prices) if prices else "",
                images[0]["src"] if images else "",
                strip_html(p.get("body_html"))[:500],
            ])

    with open(var_csv, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow([
            "product_name", "product_url", "product_type", "size_option",
            "price_usd", "compare_at_price_usd", "sku", "grams", "available",
            "variant_id",
        ])
        for p in products:
            url = f"{BASE}/products/{p.get('handle')}"
            for v in p.get("variants", []):
                w.writerow([
                    p.get("title"),
                    url,
                    p.get("product_type"),
                    v.get("title"),
                    v.get("price"),
                    v.get("compare_at_price") or "",
                    v.get("sku"),
                    v.get("grams"),
                    v.get("available"),
                    v.get("id"),
                ])

    n_var = sum(len(p.get("variants", [])) for p in products)
    print(f"\nWrote {len(products)} products / {n_var} variants to {OUT_DIR}")


def main() -> int:
    products = scrape_all()
    if not products:
        print("No products fetched.", file=sys.stderr)
        return 1
    write_outputs(products)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
