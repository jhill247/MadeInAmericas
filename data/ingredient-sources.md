# Ingredient Cost Database — Source Sites & Scraping Notes

Goal: build MadeInAmericas' own database of **supplement** and **cosmetic**
ingredient costs by collecting publicly displayed retail prices (with quantity
tiers) from ingredient retailers. This doc tracks the source sites, which are
easy vs. hard to scrape, and what data to capture.

> **Key finding:** many ingredient retailers run on **Shopify**, which exposes a
> public, read-only `/<store>/products.json` feed (paginated, 250/page) with
> every product and every variant (size tier) + price. Where that exists,
> collection is trivial and reliable. Use `scrapers/shopify_scraper.py <domain>`.
> Sites not on Shopify need a custom HTML scraper.

---

## ✅ Done: BulkSupplements.com

- Platform: **Shopify** (`/products.json`).
- Captured: **794 products / 4,767 variants** (size + price tiers).
- Example (matches the brief): *Collagen Peptides Powder* —
  100 g $18.97 · 250 g $21.97 · 500 g $27.97 · 1 kg $40.97 · 5 kg $187.97 ·
  20 kg $446.58 (with SKU, gram weight, sale price, availability per tier).
- Output: `data/bulksupplements/` →
  `bulksupplements_products.csv`, `bulksupplements_variants.csv`, `products_raw.json`.

---

## Sites that sell BOTH supplement + cosmetic ingredients (start here)

These give the most coverage per site and match the "involved with both" ask.

| Site | What they carry | Prices shown | Platform / scrape |
|---|---|---|---|
| **Bulk Apothecary** (bulkapothecary.com) | Bulk herbs & supplement powders **and** soap/cosmetic ingredients (carrier oils, butters, EOs) | Yes, with size tiers | Custom (not Shopify) |
| **Mountain Rose Herbs** (mountainroseherbs.com) | Organic herbs/powders (supplement-grade) **and** carrier oils, butters, clays, EOs (cosmetic) | Yes, with size tiers | Custom (not Shopify) |
| **Starwest Botanicals** (starwest-botanicals.com) | Botanical powders/extracts (supplement) **and** cosmetic-grade botanicals/oils | Yes, with size tiers | Custom (not Shopify) |
| **New Directions Aromatics** (newdirectionsaromatics.com) | Essential/carrier oils, butters (cosmetic) + some botanical extracts | Yes, with size tiers | Custom (not Shopify) |
| **Essential Wholesale & Labs** (essentialwholesale.com) | Cosmetic bases/actives, personal-care; some nutricosmetic | Yes | **Shopify** ✅ |

---

## Supplement ingredient retailers (prices displayed)

| # | Site | Notes | Platform / scrape |
|---|---|---|---|
| 1 | **BulkSupplements.com** | Done — 794 products | **Shopify** ✅ |
| 2 | **PureBulk.com** | Bulk vitamins, aminos, herbs; tiered sizes | **Shopify** ✅ |
| 3 | **Nutricost** (nutricost.com) | Mostly finished, but bulk powders too | **Shopify** ✅ |
| 4 | **N101 Nutrition** (n101nutrition.com) | Supplements & some bulk | **Shopify** ✅ |
| 5 | **Ingredi** (ingredi.com) | Bulk food/ingredients incl. supplement-grade | **Shopify** ✅ |
| 6 | **Bulk Apothecary** | Herbs + supplement powders | Custom |
| 7 | **Starwest Botanicals** | Botanical powders/extracts | Custom |
| 8 | **Mountain Rose Herbs** | Organic herbs/powders | Custom |
| 9 | **Monterey Bay Herb Co** (herbco.com) | Bulk herbs/botanicals | Custom |

## Cosmetic ingredient retailers (prices displayed)

| # | Site | Notes | Platform / scrape |
|---|---|---|---|
| 1 | **Lotioncrafter.com** | Actives, emulsifiers, oils | **Shopify** ✅ |
| 2 | **Formulator Sample Shop** (formulatorsampleshop.com) | INCI actives, sample + bulk sizes | **Shopify** ✅ |
| 3 | **WholesaleSuppliesPlus.com** | Soap/cosmetic base ingredients | **Shopify** ✅ |
| 4 | **Camden Grey Essential Oils** (camdengrey.com) | EOs, carrier oils | **Shopify** ✅ |
| 5 | **TKB Trading** (tkbtrading.com) | Pigments, micas, bases | **Shopify** ✅ |
| 6 | **MakingCosmetics.com** | Broad actives/emulsifiers catalog | Custom |
| 7 | **Bramble Berry** (brambleberry.com) | Soap/cosmetic ingredients | Custom (blocks bots) |
| 8 | **Ingredients to Die For** (ingredientstodiefor.com) | Actives, extracts | Custom |
| 9 | **The Herbarie** (theherbarie.com) | Emulsifiers, actives | Custom |
| 10 | **Skin Actives Scientific** (skinactives.com) | Cosmetic actives | Custom |

---

## What data to capture per ingredient (schema)

For a usable cost database, store at the **variant (size-tier) level** and derive
a normalized unit cost so different vendors/sizes are comparable:

- `ingredient_name` (raw product title) + `canonical_ingredient` (normalized,
  e.g. "Collagen Peptides (Bovine, Hydrolyzed)")
- `source_site`, `product_url`, `sku`, `vendor/brand`
- `size_label` (e.g. "1 Kilogram") + parsed `quantity` + `unit` (g/ml/oz)
- `price`, `compare_at_price` (sale), `currency`, `in_stock`
- **`price_per_kg` / `price_per_unit`** (computed — the key comparison field)
- `form` (powder/capsule/liquid/oil/extract), `grade` (food/USP/cosmetic),
  `certifications` (organic, non-GMO, GMP), `country_of_origin` if listed
- `category` (supplement vs cosmetic), `scraped_at` timestamp

A normalized `price_per_kg` is what powers the cost estimator and the public
"ingredient cost" SEO pages — it lets you show "market low / median / high."

---

## What else is useful (recommendations)

1. **Normalize to price-per-kg/unit** on ingestion — vendors use different size
   labels; the unit price is the only thing that's comparable and is what the
   calculator needs.
2. **Capture quantity-break curves**, not just one price. The 100 g → 20 kg
   curve (already captured for BulkSupplements) is exactly what makes a
   manufacturing estimate realistic at different production volumes.
3. **Track over time.** Re-run scrapers on a schedule (weekly/monthly) and keep
   `scraped_at` so you can build price-trend pages and a "Manufacturing Cost
   Index" (great for SEO/PR — see the growth plan).
4. **De-duplicate to a canonical ingredient.** Map "Vitamin C (Ascorbic Acid)",
   "L-Ascorbic Acid", etc. to one canonical record with synonyms + CAS number +
   INCI name. This is the hardest but highest-value step.
5. **Note grade & certifications.** Cosmetic-grade vs food/USP-grade vs
   pharma-grade differ a lot in price — don't blend them.
6. **Separate retail vs wholesale.** Retail ingredient prices (these sites) are
   higher than true contract-manufacturing input costs. Use retail as a *ceiling*
   and apply a discount factor, or supplement with B2B sources later
   (Alibaba/Made-in-China for benchmarking, Knowde, ChemicalBook, distributor
   line cards) — clearly label the source tier.
7. **Respect robots.txt & rate limits.** The Shopify `products.json` feed is
   public and we throttle (0.7s/page), but keep it polite and cache raw JSON so
   re-parsing doesn't re-hit the site.
8. **Watch for currency/localization.** `products.json` returns the store's
   default currency; record `currency` explicitly.
9. **Prefer structured endpoints over HTML.** Beyond Shopify `products.json`,
   check for `sitemap.xml`, JSON-LD `Product` schema in page source, or a
   `/collections/<x>/products.json` per-category feed before writing brittle
   HTML parsers.
10. **Cross-reference with Amazon/iHerb** for finished-product pricing if you
    later want to model retail margins end-to-end.

---

## How to add another source

```bash
# Confirm it's Shopify (look for products):
curl -s "https://<domain>/products.json?limit=1"

# If it returns JSON with a "products" array, scrape it:
python3 scrapers/shopify_scraper.py <domain> --name <slug>
```
