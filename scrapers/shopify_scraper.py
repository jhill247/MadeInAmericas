#!/usr/bin/env python3
"""Generic Shopify ingredient-store scraper.

Many ingredient retailers run on Shopify, which exposes a public read-only
/products.json feed (paginated, max 250/page) with every product and every
variant (size tier) + price. This script pulls that feed for ANY such store.

Usage:
    python3 shopify_scraper.py <domain> [--name SLUG]

Examples:
    python3 shopify_scraper.py www.bulksupplements.com --name bulksupplements
    python3 shopify_scraper.py purebulk.com --name purebulk
    python3 shopify_scraper.py lotioncrafter.com --name lotioncrafter

Confirmed working (as of this writing): bulksupplements.com, purebulk.com,
nutricost.com, n101nutrition.com, ingredi.com, lotioncrafter.com,
formulatorsampleshop.com, wholesalesuppliesplus.com, essentialwholesale.com,
camdengrey.com, tkbtrading.com.

NOT Shopify (need a custom scraper): mountainroseherbs.com, starwest-botanicals.com,
bulkapothecary.com, makingcosmetics.com, newdirectionsaromatics.com, brambleberry.com.

Outputs under data/<name>/:
  - products_raw.json
  - <name>_products.csv   (one row per product)
  - <name>_variants.csv   (one row per size/price tier)
"""
from __future__ import annotations

import argparse
import csv
import html
import json
import os
import re
import sys
import time
import urllib.request
import urllib.error

USER_AGENT = (
    "Mozilla/5.0 (compatible; MadeInAmericas-IngredientBot/1.0; "
    "ingredient cost research)"
)
MAX_PAGES = 400
SLEEP_BETWEEN = 0.7
RETRIES = 4


def fetch(url: str) -> dict:
    last_err = None
    for attempt in range(RETRIES):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=40) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, json.JSONDecodeError) as e:
            last_err = e
            wait = 2 ** attempt
            print(f"  retry {attempt + 1}/{RETRIES} after error: {e} (wait {wait}s)")
            time.sleep(wait)
    raise RuntimeError(f"failed to fetch {url}: {last_err}")


def strip_html(raw: str | None) -> str:
    if not raw:
        return ""
    text = re.sub(r"<[^>]+>", " ", raw)
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


def scrape_all(base: str) -> list[dict]:
    products: list[dict] = []
    for page in range(1, MAX_PAGES + 1):
        data = fetch(f"{base}/products.json?limit=250&page={page}")
        batch = data.get("products", [])
        if not batch:
            break
        products.extend(batch)
        print(f"page {page}: +{len(batch)} (total {len(products)})")
        time.sleep(SLEEP_BETWEEN)
    return products


def write_outputs(products: list[dict], base: str, name: str) -> None:
    out_dir = os.path.join(os.path.dirname(__file__), "..", "data", name)
    os.makedirs(out_dir, exist_ok=True)

    with open(os.path.join(out_dir, "products_raw.json"), "w") as f:
        json.dump(products, f, indent=2)

    with open(os.path.join(out_dir, f"{name}_products.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow([
            "product_id", "product_name", "product_url", "product_type",
            "vendor", "tags", "num_variants", "min_price", "max_price",
            "image_url", "description",
        ])
        for p in products:
            variants = p.get("variants", [])
            prices = [float(v["price"]) for v in variants if v.get("price")]
            images = p.get("images", [])
            tags = p.get("tags")
            w.writerow([
                p.get("id"), p.get("title"),
                f"{base}/products/{p.get('handle')}",
                p.get("product_type"), p.get("vendor"),
                "; ".join(tags) if isinstance(tags, list) else tags,
                len(variants),
                min(prices) if prices else "", max(prices) if prices else "",
                images[0]["src"] if images else "",
                strip_html(p.get("body_html"))[:500],
            ])

    with open(os.path.join(out_dir, f"{name}_variants.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow([
            "product_name", "product_url", "product_type", "size_option",
            "price", "compare_at_price", "sku", "grams", "available", "variant_id",
        ])
        for p in products:
            url = f"{base}/products/{p.get('handle')}"
            for v in p.get("variants", []):
                w.writerow([
                    p.get("title"), url, p.get("product_type"), v.get("title"),
                    v.get("price"), v.get("compare_at_price") or "", v.get("sku"),
                    v.get("grams"), v.get("available"), v.get("id"),
                ])

    n_var = sum(len(p.get("variants", [])) for p in products)
    print(f"\nWrote {len(products)} products / {n_var} variants to {out_dir}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("domain", help="store domain, e.g. purebulk.com")
    ap.add_argument("--name", help="output slug (default: derived from domain)")
    args = ap.parse_args()

    domain = args.domain.replace("https://", "").replace("http://", "").strip("/")
    base = f"https://{domain}"
    name = args.name or re.sub(r"[^a-z0-9]+", "_", domain.lower()).strip("_")

    products = scrape_all(base)
    if not products:
        print("No products fetched (is this a Shopify store?).", file=sys.stderr)
        return 1
    write_outputs(products, base, name)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
