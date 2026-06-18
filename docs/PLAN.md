# Fabrera — Master Plan & Product Spec

> **Status:** Living document — we update this continuously as the plan evolves.
> **Name:** **Fabrera** — domain `fabrera.com` (purchased; DNS via Cloudflare). Repo currently `MadeInAmericas` (rename optional later).
> **One-liner:** The default destination for "I need a factory somewhere in the Americas."
> **Last updated:** 2026-06-17

---

## Table of Contents
1. [Vision](#1-vision)
2. [Problem & Core Insight](#2-problem--core-insight)
3. [Strategy & Differentiation](#3-strategy--differentiation)
4. [Personas](#4-personas)
5. [Scope & Phasing](#5-scope--phasing)
6. [Core Design Principle](#6-core-design-principle)
7. [Feature Specifications](#7-feature-specifications)
8. [Listing Detail Spec (Alibaba-style)](#8-listing-detail-spec-alibaba-style)
9. [Pricing Model](#9-pricing-model)
10. [SEO / GEO Architecture](#10-seo--geo-architecture)
11. [Object Models (Detailed)](#11-object-models-detailed)
12. [Tech Architecture](#12-tech-architecture)
13. [Data Acquisition & Enrichment Pipeline](#13-data-acquisition--enrichment-pipeline)
14. [Internationalization (US + Mexico)](#14-internationalization-us--mexico)
15. [Monetization (Design-to-Preserve)](#15-monetization-design-to-preserve)
16. [Success Metrics](#16-success-metrics)
17. [Non-Goals](#17-non-goals)
18. [Risks & Mitigations](#18-risks--mitigations)
19. [Roadmap](#19-roadmap)
20. [Resolved Decisions](#20-resolved-decisions)
21. [Supabase SQL Schema](#21-supabase-sql-schema)
22. [Next.js Route Map](#22-nextjs-route-map)
23. [Data Sourcing Strategy](#23-data-sourcing-strategy)
24. [Pricing Estimation Calculator (Flagship Deliverable)](#24-pricing-estimation-calculator-flagship-deliverable)
25. [AI Stock Image & Branded Media Standard](#25-ai-stock-image--branded-media-standard)
26. [Environment & Configuration](#26-environment--configuration)
27. [Admin / Ops Console & Automation](#27-admin--ops-console--automation)
28. [Definition of Done / Acceptance Criteria](#28-definition-of-done--acceptance-criteria)
29. [SEO Tools & Growth Engine](#29-seo-tools--growth-engine)
30. [Design System & UI Foundations](#30-design-system--ui-foundations)
31. [Testing & QA Strategy](#31-testing--qa-strategy)
32. [Infrastructure, CI/CD & Operations](#32-infrastructure-cicd--operations)
33. [Email, Notifications & Deliverability](#33-email-notifications--deliverability)
34. [Security, Privacy & Compliance](#34-security-privacy--compliance-consolidated)
35. [Search, Ranking & Recommendations Spec](#35-search-ranking--recommendations-spec)
36. [Analytics Event Taxonomy](#36-analytics-event-taxonomy)
37. [Quality Bars (Accessibility, Performance, i18n)](#37-quality-bars-accessibility-performance-i18n)
38. [Seed Data, Fixtures & Data Dictionary](#38-seed-data-fixtures--data-dictionary)
39. [Build Execution Contract (Determinism Guardrails)](#39-build-execution-contract-determinism-guardrails)
40. [Default Decisions Registry](#40-default-decisions-registry-no-questions-needed-defaults)
41. [Product / Ingredient Hub Pages (Pillar SEO + Monetization)](#41-product--ingredient-hub-pages-pillar-seo--monetization)

## 1. Vision

Become the default destination for the query **"I need a factory somewhere in the Americas."**

Start as a high-quality discovery engine + verified database for North, Central, and South American contract manufacturing, beginning in CPG verticals where the founder has domain expertise. Layer on RFQ workflow and a proprietary **responsiveness dataset** that no incumbent (ThomasNet, Google, LLMs) can replicate.

Listings are **rich and detailed, like Alibaba product pages** — specific products, specs, MOQ/lead-time/price tiers, media, and customization options — but anchored to *verified manufacturers in the Americas*.

Free at launch to prove the model, gain SEO/GEO authority, and accumulate the data moat; monetize later through TBD methods.

---

## 2. Problem & Core Insight

- Buyers genuinely **cannot find — or get callbacks from — manufacturers** in the Americas. This is a **workflow problem, not just a directory problem.** ThomasNet solved discovery; nobody solved procurement.
- Prior attempts (ThomasNet, MFG.com, Xometry, Maker's Row, IndustryNet) never became "Alibaba for the Americas" for structural reasons:
  1. Alibaba solved a uniquely Chinese discovery problem; North America's pain was less severe.
  2. US manufacturing is fragmented by **industry, not geography** → weak marketplace liquidity.
  3. Many US manufacturers are capacity-constrained and **don't want random leads**.
  4. RFQ marketplaces devolve into **race-to-the-bottom** that suppliers come to hate.
  5. ThomasNet trained the market to expect **directories** ("list me, buyers call me"), not transactions.
  6. The biggest opportunity today is in fragmented CPG verticals (supplements, cosmetics, food, packaging), not heavy industry.
- **Why now:** reshoring, nearshoring, tariff pressure, and supply-chain diversification push buyers to look beyond China — yet no consumer-grade discovery destination exists for the Americas. AI collapses the cost of building/enriching the supply-side dataset.

---

## 3. Strategy & Differentiation

1. **Discovery engine first, marketplace never (or much later).** Avoid the three-sided cold start (buyers + sellers + transactions simultaneously).
2. **The moat is response data**, not the listings. "Who replies, how fast, how often" is structurally un-scrapable by Google/LLMs.
3. **Rich listings are a second moat.** Alibaba-grade product detail (specs, tiered pricing, media, customization) for Americas manufacturers does not exist anywhere today.
4. **SEO + GEO is the growth engine** — but only works if every page carries *real, differentiated data*. Thin programmatic pages get penalized post-2024; our verified data is both the defense and the moat.
5. **Domain-led data quality.** Launch where the founder can personally vet records.

---

## 4. Personas

| Persona | Who | Primary need | Reason to engage |
|---|---|---|---|
| **Buyer / Sourcer** | Indie brand founder, procurement lead, product developer | Find qualified manufacturers + actually get responses | Sourcing CRM, RFQ distribution, response data |
| **Manufacturer** | Contract manufacturer (OEM/ODM/white-label) | Control public listing, qualified leads, reputation | Claim listing, lead dashboard, responsiveness badge |
| **Data buyer (future)** | Analyst, investor, brand strategist | Benchmarks & market intelligence | Reports, API, cost/lead-time benchmarks |

---

## 5. Scope & Phasing

**Build broad, launch narrow.** Architecture is general from day one (all verticals, US + Mexico, bilingual-ready). Live content launches narrow and expands by toggling data on.

- **Phase 1 (Launch):** Supplements/nutraceuticals, **US-first** SEO pages, English UI. Directory + faceted/AI search + detailed listings + claim + RFQ (on-platform inbox) + response-rate scores live. Review *capture* on (display gated).
- **Phase 1.5:** Switch on cosmetics, food & beverage, packaging content. Add Mexico geo pages + Spanish (`hreflang`).
- **Phase 2:** Public reviews (volume + moderation ready), comparison/ranking pages at scale, AI sourcing agent, data/market-intelligence products, first monetization experiments.

---

## 6. Core Design Principle

Every feature must do **at least one** of:
1. Create a highly indexable SEO/GEO page.
2. Give buyers a reason to create/maintain an account.
3. Give manufacturers a reason to claim/improve a listing.

**Every user action should generate new content, data, or pages** that improve discoverability.

## 7. Feature Specifications

### MVP = Phase 1

**7.0 Homepage / Discovery Landing (product-first)**
> Approved design direction: `~/.gstack/projects/jhill247-MadeInAmericas/designs/homepage-search-20260617/APPROVED-homepage.png` (variant A2, via `/design-shotgun` 2026-06-17). Clean navy/slate "Trust & Trade" aesthetic, category-grid hero. **The homepage leads with products and product categories, not manufacturers** — products are the high-intent entry point; manufacturers surface one layer deeper (on vertical, category, and product-hub pages).
- **Hero:** headline ("Source any product, made in the Americas") + prominent natural-language search bar with filter chips (Category, Country/State, Certification, MOQ). Faint Americas-map motif.
- **Category grid (centerpiece):** large tiles for the top **verticals** — Supplements, Beauty & Cosmetics, Food & Beverage, Packaging, Personal Care, Pet, Nutraceuticals, Household — each with an icon and a live product/listing count. Links to the vertical landing page (`/v/[verticalSlug]`).
- **Trust strip:** verified-manufacturer count, median response time, "Made in the Americas" nearshoring angle (the §7.7 responsiveness moat, surfaced globally).
- **Hot / Trending products:** a grid of **product cards** (not manufacturer cards) — e.g., Collagen Peptides Powder, Hyaluronic Acid Serum, Whey Protein, Vitamin D3 — each with thumbnail, product/ingredient name, category tag, tri-state price-availability indicator (§9), and a "from N verified makers" line. Cards link to the **product/ingredient hub page (§41)** or category page, which then funnels to ranked manufacturers + the calculator + RFQ.
- **Tool + geo entry points:** "Try the Cost Estimator" tile (rendering a live estimate range — the §24 SEO anchor) and "Browse by Country".
- **SEO footer:** product-category and country link columns (internal-linking surface for §10).
- **Determinism note:** product/category counts and "Hot products" selection are computed from seeded data (§38) + first-party demand signals (§36); the page renders fully from our own data with no dependency on live third-party calls (§39.3).

**7.1 Discovery & Search**
- Faceted search: vertical, category, capability/process, certification, country/state/city, MOQ range, capacity, verification level, **response-rate score**, price availability.
- **AI natural-language search (simple):** free-text query (e.g., *"US gummy maker, organic, 50k bottles/mo"*) → LLM parses into structured filters → results. Logs queries for demand intelligence + new page ideas.
- Saved searches + new-supplier alerts (account-gated → reason to sign up).

**7.2 Manufacturer Profile Pages** (`/m/[slug]`)
- Facility info, locations, capabilities, certifications (with verified flag), categories, capacity/MOQ/lead-time ranges, photos/videos, white-label/stock products, prominent **Response-Rate Score** + verification badge. Data-source provenance tracked internally.

**7.3 Detailed Product Listings** (`/m/[slug]/p/[product-slug]`)
- Alibaba-grade product detail pages (see §8). This is a core differentiator and a massive SEO surface.

**7.4 Claim Your Listing + Verification**
- Manufacturer claims a scraped/seeded profile; edits content.
- **Verification levels:** Unverified → Basic (email/domain) → Verified (business registration) → Verified Facility/cert validation. Verification = trust signal + future paywall lever.

**7.5 Buyer Accounts, Projects/Workspace**
- Buyer dashboard = sourcing CRM: saved manufacturers, projects, active RFQs, responses, notes.
- **Project/Workspace:** reusable sourcing project (product type, specs, artwork, packaging, certs needed, MOQ). Reduces effort on future sourcing → switching cost.

**7.6 RFQ + On-Platform Messaging (Inbox)**
- Buyer composes one RFQ → sends to N selected manufacturers. **All messaging flows through an on-platform inbox** (cleanest capture of the response-data moat). Email notifications drive manufacturers back in.
- Manufacturer **Lead Dashboard:** incoming RFQs/inquiries.

**7.7 Response-Rate Scoring (the moat) — live day one**
- Every RFQ/message emits **ResponseEvents** (`sent_at`, `first_reply_at`, replied?). Compute per-manufacturer: response rate, median first-response time, quote-conversion rate. Display tiers ("replies within 2h / 24h / 7d"). Bootstrap with verification-outreach replies before RFQ volume exists.

**7.8 Reviews & Ratings — capture now, display later**
- Build buyer→manufacturer (and manufacturer→buyer) rating capture **at launch** (communication, quality, timeliness, pricing); store it, **do not display publicly** until volume + moderation/right-of-reply guardrails are in place.

**7.9 Sample Request Management**
- Buyers request samples; track requested/received/rated. Creates switching costs and feeds response data.

**7.10 Admin / Ops Console (founder)**
- Internal tooling to review seeded data, approve claims/verifications, moderate content, merge duplicates, and manage taxonomy. Essential for a solo operator (see §20).

## 8. Listing Detail Spec (Alibaba-style)

Each manufacturer's listings contain **specific products**, presented with the depth of an Alibaba product page (reference: [Alibaba OEM Hydrolyzed Collagen Peptides listing](https://www.alibaba.com/product-detail/OEM-Hydrolyzed-Collagen-Peptides-Beauty-Protein_1601621077199.html)). A "product" here is a concrete offering a manufacturer makes (e.g., *"OEM Hydrolyzed Collagen Peptides Powder"*), not just a capability.

### 8.1 Anatomy of a product listing
1. **Header**
   - Product title (e.g., "OEM Hydrolyzed Collagen Peptides — Beauty Protein Powder")
   - Manufacturer name + verification badge + response-rate score
   - Product type tags (vertical, category, form/format)
2. **Media gallery**
   - Photos (product, packaging, facility, label mockups), videos, optional 360°. *(See media rights note in §20.)*
3. **Pricing block** (see §9)
   - Tiered price-by-quantity table, MOQ, unit, currency. Clearly flagged **Actual / Estimated / Unknown**.
4. **Variations / SKUs**
   - Flavor, size/fill, dosage/concentration, packaging type, color, formulation variant.
5. **Key attributes / specs table**
   - Form (powder, capsule, softgel, gummy, liquid, cream, sachet…), ingredients/actives, dosage, shelf life, storage, country of origin, allergen info, dietary tags (vegan, organic, non-GMO, gluten-free), regulatory class.
6. **Customization / OEM-ODM options**
   - Private label, custom formulation, custom packaging, logo printing, custom flavor/color, label design service. Each with availability + (optional) cost/lead-time impact.
7. **MOQ & lead-time table**
   - Quantity break → lead time (e.g., 1k–5k = 15 days; 5k–20k = 25 days).
8. **Samples**
   - Available? sample price, sample lead time, paid/free, sample policy.
9. **Packaging & delivery**
   - Packaging details, units/carton, carton dimensions/weight, supply ability (e.g., "500,000 units/month"), shipping/incoterms (FOB/EXW/DDP), origin port/city, est. delivery.
10. **Certifications relevant to this product**
    - NSF, cGMP, FDA-registered, USDA Organic, Halal, Kosher, etc., with verified flags.
11. **Supplier snapshot**
    - Years in business, response rate, on-time score (future), location, capacity.
12. **Reviews & Q&A** (capture now / display Phase 2)
13. **FAQ** (per product; great for SEO + LLM citation)
14. **Related products / "more from this manufacturer"**
15. **Primary CTA:** "Request Quote" / "Request Sample" (routes into RFQ inbox + response tracking)

### 8.2 Data completeness & confidence
- Every listing has a **completeness score** (% of key fields populated) and a **provenance/confidence** marker per field (scraped, AI-estimated, manufacturer-provided, founder-verified).
- Listings below a completeness threshold may be `noindex` until enriched (protects SEO quality — see §10).

---

## 9. Pricing Model

Pricing is first-class and explicitly **tri-state** so we never mislead buyers:

| State | Meaning | Source | UI treatment |
|---|---|---|---|
| **Actual** | Real price from manufacturer's site/catalog or manufacturer-provided | scraped-with-source / claimed | Show price + "Source: manufacturer site" |
| **Estimated** | Intelligently inferred when no public price exists | AI/heuristic model | Show range + "Estimated" badge + methodology tooltip |
| **Unknown** | Cannot responsibly estimate | — | "Request quote for pricing" CTA |

### 9.1 Estimation methodology (when Estimated)
- Inputs: product form/category, ingredients/actives, MOQ tier, packaging, region, certifications, and **anonymous benchmarks** from comparable listings + observed RFQ quotes over time.
- Output: a price **range** per quantity tier with a **confidence level** (low/med/high) and a stored **methodology snapshot** for transparency/legal cover.
- Always rendered as a range with a clear "estimate, not a quote" disclaimer.

### 9.2 Price structure
- Prices stored as **tiered breaks** (min qty, max qty, unit price, currency, unit of measure).
- Multi-currency (USD, MXN) with a captured FX timestamp; multi-unit (each, kg, L, case).
- Optional one-time charges: tooling/setup, plate/mold, design fee, sample fee.

### 9.3 Line-item cost breakdown (mandatory for estimates)
Every estimate must render a **transparent, line-item breakdown** so the buyer sees exactly how we arrived at the number. Example shape:

| Component | Basis | Est. cost / unit |
|---|---|---|
| Active ingredient(s) | qty × concentration × $/kg | $0.42 |
| Other ingredients / excipients | formula | $0.08 |
| Delivery form / processing (e.g., encapsulation, gummy depositing) | per-unit run cost | $0.15 |
| Primary packaging (bottle/pouch/blister) | packaging choice | $0.22 |
| Secondary packaging / labeling | label + box | $0.06 |
| Labor & fill | line rate ÷ throughput | $0.10 |
| Overhead & margin | % applied | $0.18 |
| **Estimated unit cost (range)** | | **$1.05 – $1.31** |

- This breakdown is produced by the **Pricing Estimation Calculator** (§24) and stored as a snapshot on the listing's `Pricing.estimate.lineItems`.
- One-time fees (tooling, mold/plate, design) are shown separately.

### 9.4 Why this matters
- Pricing transparency is the #1 thing missing from Americas sourcing today and a huge SEO/GEO draw ("collagen peptides manufacturing cost," etc.).
- Observed RFQ quotes feed back into the estimation model → compounding **cost-benchmark dataset** (future monetization).
- The interactive **Pricing Estimation Calculator** (§24) is both a standalone SEO/lead-gen asset and the engine behind every listing estimate.

## 10. SEO / GEO Architecture

**Rendering:** SSR/SSG (Next.js App Router). Fast Core Web Vitals, clean canonical URLs, XML sitemaps, robots rules.

### 10.1 Page types (each = indexable asset)
| Type | Example route | Powered by |
|---|---|---|
| Home (product-first) | `/` | Verticals + product hubs + demand signals (§7.0) |
| Vertical / department landing | `/v/supplements` | Vertical (top-tier taxonomy) |
| Product / ingredient hub (pillar) | `/ingredients/collagen` | **Product hub + cost DB (§41)** |
| Manufacturer profile | `/m/[slug]` | Manufacturer |
| Product listing | `/m/[slug]/p/[product-slug]` | Product |
| Category | `/c/gummy-manufacturers` | Category |
| Category × Geo | `/c/gummy-manufacturers/texas` | Category + Location |
| Certification | `/cert/nsf-certified-manufacturers` | Certification |
| Capability / equipment | `/cap/softgel-manufacturing` | Capability |
| Ranking ("fastest-responding / top / best") | `/best/fastest-responding-supplement-manufacturers` | **Response data (unique)** |
| Comparison | `/compare/[a]-vs-[b]` | Manufacturer × Manufacturer |
| Cost / pricing guides | `/cost/collagen-peptides-manufacturing` | **Pricing/benchmark data** |

### 10.2 GEO (LLM citability)
- schema.org JSON-LD: `Organization`, `LocalBusiness`, `Product`, `Offer`, `AggregateRating` (when reviews live), `FAQPage`.
- Factual, structured copy; accessible sitemaps; optional public read API. Goal: be the source ChatGPT / Perplexity / Gemini cite for Americas manufacturing queries.

### 10.3 Quality guardrails (anti-thin-content)
- Pages render only when backed by real data; low-completeness listings `noindex` until enriched.
- Rankings, comparisons, cost guides differentiate via our proprietary data — content competitors/LLMs cannot generate.

---

## 11. Object Models (Detailed)

> Representation below is TypeScript-style interfaces for precision; these map to Postgres tables in Supabase. IDs are UUIDs; timestamps `created_at`/`updated_at` implied on all entities. `*` = nullable/optional.

### 11.1 Provenance & confidence (shared)
```typescript
type DataSource = 'scraped' | 'ai_enriched' | 'manufacturer_provided' | 'founder_verified';
type Confidence = 'low' | 'medium' | 'high';

interface FieldProvenance {
  field: string;          // dot-path of the field, e.g. "pricing.tiers[0].unitPrice"
  source: DataSource;
  confidence: Confidence;
  sourceUrl?: string;     // where it was scraped from
  capturedAt: string;     // ISO timestamp
  methodology?: string;   // snapshot of how an estimate was derived
}
```

### 11.2 Manufacturer
```typescript
interface Manufacturer {
  id: string;
  slug: string;                 // unique, SEO
  domain: string;               // PRIMARY IDENTIFIER for v1 (normalized, unique)
  legalName: string;
  displayName: string;
  description?: string;
  yearFounded?: number;
  sizeEstimate?: 'micro' | 'small' | 'medium' | 'large';
  employeeCountRange?: string;
  websiteUrl?: string;
  logoUrl?: string;             // scraped public logo (re-hosted in Storage)
  locations: Location[];        // 1:N
  capabilities: Capability[];   // M:N
  certifications: CertificationAssertion[]; // M:N w/ verified flag
  categories: Category[];       // M:N
  products: Product[];          // 1:N
  media: MediaAsset[];
  contact: ContactInfo;
  verificationLevel: 'unverified' | 'basic' | 'verified' | 'verified_facility';
  claimStatus: 'unclaimed' | 'pending_claim' | 'claimed';
  claimedByUserId?: string;
  responseScore?: ResponseScore;
  completenessScore: number;    // 0–100
  provenance: FieldProvenance[];
  status: 'active' | 'merged' | 'hidden' | 'archived';
  mergedIntoId?: string;        // duplicate handling
}

interface ContactInfo {
  // INTERNAL-ONLY fields (never shown publicly in Phase 1; admin/RLS-protected).
  // Public listings display ONLY the domain. See §20.C.
  email?: string;               // scraped + stored for internal outreach
  phone?: string;               // scraped + stored for internal outreach
  contactName?: string;         // scraped + stored for internal outreach
  additionalEmails?: string[];
  additionalPhones?: string[];
  addressLine?: string;
  optedOut: boolean;            // takedown/opt-out flag
}
```

### 11.3 Location, Capability, Certification, Category
```typescript
interface Location {
  id: string;
  manufacturerId: string;
  country: 'US' | 'MX' | 'CA' | string; // ISO; Americas-wide ready
  stateRegion?: string;
  city?: string;
  postalCode?: string;
  lat?: number;
  lng?: number;
  isHeadquarters: boolean;
  isProductionSite: boolean;
}

interface Capability {        // controlled vocabulary (taxonomy)
  id: string;
  slug: string;               // e.g. "softgel-manufacturing"
  name: string;
  description?: string;
  parentId?: string;          // hierarchical
}

interface Certification {     // controlled vocabulary
  id: string;
  slug: string;               // e.g. "nsf"
  name: string;
  issuingBody?: string;
}

interface CertificationAssertion {
  certificationId: string;
  manufacturerId: string;
  verified: boolean;
  certificateUrl?: string;          // link on the manufacturer's site
  certificateFileUrl?: string;      // scraped cert document (image/PDF), re-hosted in Storage
  certificateFileType?: 'image' | 'pdf';
  expiresAt?: string;
  provenance: FieldProvenance;
}

interface Category {          // hierarchical taxonomy
  id: string;
  slug: string;               // e.g. "gummies"
  name: string;
  vertical: 'supplements' | 'cosmetics' | 'food_beverage' | 'packaging' | string;
  parentId?: string;
}
```

### 11.4 Product (Alibaba-style listing) & Variants
```typescript
interface Product {
  id: string;
  manufacturerId: string;
  slug: string;                 // SEO, unique within manufacturer
  title: string;
  summary?: string;
  description?: string;         // rich text
  categoryIds: string[];
  form?: string;                // powder, capsule, softgel, gummy, liquid, cream, sachet...
  attributes: ProductAttribute[];
  variants: ProductVariant[];
  pricing: Pricing;             // see §9 / 11.5
  moq?: number;
  moqUnit?: string;
  leadTimes: LeadTimeTier[];
  customization: CustomizationOption[];
  sample: SamplePolicy;
  packaging?: PackagingInfo;
  supplyAbility?: string;       // e.g. "500,000 units/month"
  incoterms?: ('FOB' | 'EXW' | 'DDP' | 'CIF' | string)[];
  certificationIds: string[];
  media: MediaAsset[];
  faqs: FAQ[];
  completenessScore: number;
  provenance: FieldProvenance[];
  status: 'active' | 'draft' | 'hidden';
}

interface ProductAttribute { key: string; value: string; unit?: string; }

interface ProductVariant {
  id: string;
  productId: string;
  name: string;                 // e.g. "Strawberry / 60ct / White bottle"
  optionValues: Record<string, string>; // {flavor:"strawberry", size:"60ct"}
  sku?: string;
  pricingOverride?: Pricing;    // variant-specific pricing if differs
}

interface LeadTimeTier { minQty: number; maxQty?: number; days: number; }

interface CustomizationOption {
  type: 'private_label' | 'custom_formula' | 'custom_packaging' | 'logo_print'
      | 'custom_flavor' | 'custom_color' | 'label_design' | string;
  available: boolean;
  notes?: string;
  oneTimeFee?: Money;
  leadTimeImpactDays?: number;
}

interface SamplePolicy {
  available: boolean;
  free: boolean;
  price?: Money;
  leadTimeDays?: number;
  notes?: string;
}

interface PackagingInfo {
  unitsPerCarton?: number;
  cartonDimensionsCm?: { l: number; w: number; h: number };
  cartonWeightKg?: number;
  packagingNotes?: string;
}
```

### 11.5 Pricing (tri-state, tiered, multi-currency)
```typescript
type Currency = 'USD' | 'MXN' | string;

interface Money { amount: number; currency: Currency; }

interface PriceTier {
  minQty: number;
  maxQty?: number;
  unitPrice: number;
  currency: Currency;
  unitOfMeasure: string;   // 'each', 'kg', 'L', 'case'
}

interface CostLineItem {
  component: string;          // e.g. "Active ingredient", "Primary packaging", "Labor & fill"
  basis: string;             // human-readable formula behind the number
  unitCost: number;          // contribution to per-unit cost
  currency: Currency;
  sourceCostTableVersion?: string; // links to versioned cost DB (§24)
}

interface Pricing {
  state: 'actual' | 'estimated' | 'unknown';
  tiers: PriceTier[];
  fxCapturedAt?: string;             // for non-USD conversions
  oneTimeFees?: { label: string; amount: Money }[];
  estimate?: {
    confidence: Confidence;
    methodology: string;             // snapshot string
    lineItems: CostLineItem[];       // transparent breakdown (§9.3) — REQUIRED when state==='estimated'
    rangeLow?: number;
    rangeHigh?: number;
    calculatorVersion?: string;      // which calculator/cost-DB version produced this
    computedAt?: string;
  };
  provenance: FieldProvenance;
}
```

### 11.6 Media & FAQ
```typescript
interface MediaAsset {
  id: string;
  ownerType: 'manufacturer' | 'product';
  ownerId: string;
  type: 'image' | 'video' | '360' | 'logo';
  role: 'logo' | 'product_photo' | 'facility' | 'label_mockup' | 'gallery';
  url: string;                 // stored in Supabase Storage (re-hosted)
  caption?: string;
  sourceUrl?: string;          // original source for rights tracking
  rightsStatus: 'manufacturer_provided' | 'scraped_public_logo' | 'ai_generated_stock' | 'licensed' | 'placeholder';
  // AI stock-image fields (see §25)
  isAiStock?: boolean;
  stockArchetypeId?: string;   // canonical archetype reused across manufacturers (e.g. "collagen-powder-pouch")
  brandWatermark?: string;     // e.g. "Fabrera.com" baked into the image
  sortOrder: number;
}

interface StockImageArchetype {  // one canonical AI image reused across unclaimed listings
  id: string;                    // e.g. "collagen-powder-pouch"
  label: string;
  promptSnapshot: string;        // prompt used to generate, for reproducibility
  url: string;                   // generated, watermarked asset in Storage
  appliesToCategoryIds: string[];
  createdAt: string;
}

interface FAQ { id: string; ownerType: 'manufacturer' | 'product'; ownerId: string; question: string; answer: string; }
```

### 11.7 Buyer, Project, RFQ, Messaging, Response data
```typescript
interface User {
  id: string;
  email: string;
  role: 'buyer' | 'manufacturer' | 'admin';
  displayName?: string;
  buyerReputationScore?: number;   // manufacturers rate buyers
  locale: 'en' | 'es';
}

interface Project {                // buyer sourcing workspace
  id: string;
  buyerUserId: string;
  name: string;                    // "Liposomal supplement"
  productType?: string;
  specs?: Record<string, string>;
  certificationsNeeded?: string[];
  moqTarget?: number;
  artifacts: MediaAsset[];         // artwork, packaging refs
  savedManufacturerIds: string[];
  notes?: string;
}

interface RFQ {
  id: string;
  buyerUserId: string;
  projectId?: string;
  title: string;
  details: string;
  targetManufacturerIds: string[]; // sent to N manufacturers
  quantity?: number;
  timeline?: string;
  status: 'open' | 'closed' | 'awarded';
  createdAt: string;
}

interface Message {                // on-platform inbox
  id: string;
  threadId: string;               // 1 thread per (rfq, manufacturer)
  rfqId?: string;
  fromUserId: string;
  toManufacturerId?: string;
  body: string;
  attachments?: MediaAsset[];
  sentAt: string;
}

interface ResponseEvent {          // THE MOAT
  id: string;
  manufacturerId: string;
  rfqId?: string;
  threadId: string;
  sentAt: string;
  firstReplyAt?: string;
  replied: boolean;
  source: 'rfq' | 'verification_outreach'; // bootstrap signal
}

interface ResponseScore {          // computed/cached per manufacturer
  manufacturerId: string;
  responseRatePct: number;
  medianFirstResponseHours: number;
  quoteConversionPct?: number;
  tier: 'within_2h' | 'within_24h' | 'within_7d' | 'rarely_responds' | 'unknown';
  sampleSize: number;
  computedAt: string;
}
```

### 11.8 Reviews (capture now, display Phase 2)
```typescript
interface Review {
  id: string;
  direction: 'buyer_to_manufacturer' | 'manufacturer_to_buyer';
  authorUserId: string;
  manufacturerId?: string;
  subjectUserId?: string;
  ratings: { communication?: number; quality?: number; timeliness?: number; pricing?: number };
  comment?: string;
  verifiedTransaction: boolean;
  displayStatus: 'hidden' | 'pending_moderation' | 'published'; // gated until Phase 2
  createdAt: string;
}
```

### 11.9 Saved searches & alerts
```typescript
interface SavedSearch {
  id: string;
  buyerUserId: string;
  query: string;            // raw NL query
  filters: Record<string, unknown>; // parsed structured filters
  alertEnabled: boolean;
  lastNotifiedAt?: string;
}
```

## 12. Tech Architecture

- **Frontend / SSR:** Next.js (App Router) — SSG/SSR for SEO control, ISR for large page sets.
- **Backend / DB / Auth:** Supabase (Postgres + Row-Level Security + Auth + Storage for media).
- **Search:** Postgres full-text search to start; **pgvector** for semantic/AI search and NL-query matching.
- **AI layer:** LLM for (a) NL-query → structured filters, (b) data enrichment/classification/dedup in the seeding pipeline, (c) pricing estimation. Providers: **OpenAI** (`OPENAI_API_KEY`) and **Vertex AI Gemini with Google Search grounding** (via the service account — **confirmed working**, model `gemini-2.5-flash`, location `us-central1`; `aiplatform.googleapis.com` enabled on project `bloom-platform-489223`). Vertex+Search is used for grounded discovery/enrichment of manufacturers; OpenAI for general extraction/classification.
- **Scraping technique:** prefer **structured public endpoints** over HTML parsing. Key finding: **many ingredient/product retailers run on Shopify, which exposes a public read-only `/products.json` feed** (paginated 250/page) with every product + variant (size/price tier). Also prefer JSON-LD, sitemaps, and `products.json` for manufacturer/product/pricing extraction; fall back to HTML/PDF parsing only when necessary.
- **Email:** transactional + relay/notifications (e.g., Resend/Postmark) tied to the on-platform inbox.
- **Hosting:** Vercel (natural Next.js fit).
- **Background jobs:** queue/cron (Supabase Edge Functions / scheduled jobs) for scraping, enrichment, score recomputation, alerts.
- **Analytics:** GA4 + Google Tag Manager + Google Search Console for marketing/SEO; **first-party Postgres event log** as source of truth for the RFQ→response→quote (moat) funnel. See §20.I.
- **Principle:** managed services over self-hosted infra — solo-maintainability first.

### 12.1 SEO rendering requirement (hard constraint)
Every public, indexable page **MUST serve fully-rendered SEO content in the initial HTML response — no waiting on client-side JavaScript** to render primary content or metadata. Concretely:
- Use **SSG/ISR or SSR** for all public content (manufacturer, product, category, geo, cert, capability, ranking, comparison, cost pages). No client-only data fetching for indexable content.
- All `<title>`, meta, canonical, `hreflang`, Open Graph, and **schema.org JSON-LD must be present in server-rendered HTML**.
- Interactivity (filters, calculator widgets) hydrates progressively but must not be required to see core content.
- Verify with "view source" / Googlebot fetch + Rich Results Test as part of Definition of Done (§28).

---

## 13. Data Acquisition & Enrichment Pipeline

The make-or-break workstream — a first-class system, not a footnote. See §23 for *where* to source data.

> **Extract-maximally principle:** when we crawl a source, capture **every available field**, not just what the current UI needs. Store the full raw payload (e.g., Shopify `products.json`) alongside the normalized rows. Backfilling hundreds/thousands of records later is expensive; over-capturing now is cheap. Unknown-future-use data is retained (subject to legal guardrails §13.2).

1. **Seed (scrape + AI):** ingest public sources → AI normalizes, classifies (category/capability), de-dupes **by domain**, geocodes, estimates size, extracts products + any public pricing. **Scrape and store the public logo, plus email(s), phone(s), and contact name(s) for internal use.** **Scrape certification documents (e.g., NSF / cGMP / USDA Organic / SQF certificate images or PDFs) and re-host them** (`manufacturer_certification.certificate_file_url`) as trust signals + verification evidence. Store provenance + confidence per field.
2. **Enrich:** AI fills gaps (estimated pricing via the calculator §24, attributes, AI stock images §25); flags low-confidence fields for review.
3. **Verify:** outreach to confirm contact/certs; **verification-outreach replies double as the first responsiveness signal**.
4. **Claim:** self-serve claiming layered on top (domain-email verification, §20.G) so manufacturers correct/enrich their own records.
5. **Refresh:** scheduled re-crawl to combat staleness; track `lastVerifiedAt` per record; recompute estimates when the cost DB (§24) changes.
6. **De-duplication:** **domain is the primary key** for v1; normalize domains (strip `www`, protocol, trailing slash, lowercase).

### 13.1 Volume targets (revised — 500 is too few)
500 verified records is insufficient for SEO surface area and credibility. Revised Phase-1 (supplements/US) targets:
- **Seeded manufacturers:** **3,000–5,000+** (everything we can responsibly enrich).
- **Indexed listings:** all that meet the completeness threshold (the rest `noindex` until enriched).
- **Detailed product listings:** **10,000+** across seeded manufacturers.
- **Founder-verified subset:** **300–500** highest-value records as a quality flagship (verification is a tier, not the floor).
- Quality tiers (Unverified → Basic → Verified → Verified Facility) let us scale **volume for SEO** while showcasing a **verified core** for trust.

### 13.2 Legal guardrails
- Only public data; honor takedown/opt-out (`optedOut`); store provenance; right-of-reply on any future public review; media rights tracked (§25). Public listings show **domain only** (no public PII); contact PII is internal/admin-only (§20.C).

---

## 14. Internationalization (US + Mexico)

- **Phase 1:** English UI, US content.
- **Phase 1.5:** Spanish locale, Mexico geo pages, proper `hreflang`. Listing content translatable per-locale.
- Multi-currency (USD/MXN) and multi-unit (metric/imperial) handled in the data model (§11.5) from day one.

---

## 15. Monetization (Design-to-Preserve)

Launch is 100% free. Architect so none of these are foreclosed:
1. **Paid / qualified leads & pay-per-RFQ** for manufacturers. *(selected)*
2. **Manufacturer subscriptions** — featured placement, analytics, verified badge. *(selected)*
3. **Transaction take-rate** — sampling/orders, much later. *(selected)*
4. **Sponsored placement / ads.** *(selected)* — incl. paid "Top 5 manufacturers/suppliers for {ingredient}" slots on hub pages (§41), always labeled.
5. **Data / market-intelligence products** — responsiveness + cost-benchmark datasets, reports, API. *(recommended to preserve — strongest long-term moat)*
6. **Affiliate revenue** — outbound links to finished-good brands/retailers (Amazon Associates, brand programs) from product/ingredient hub pages (§41). Lower-intent but monetizes top-of-funnel SEO traffic that isn't yet RFQ-ready.

---

## 16. Success Metrics (Phase 1)

- **Supply:** # verified manufacturers; % claimed; avg data completeness score; # detailed product listings.
- **SEO/GEO:** indexed pages, organic sessions, long-tail rankings, LLM citations.
- **Engagement:** buyer signups, projects created, RFQs sent, samples requested.
- **Moat:** RFQs with ≥1 response, median first-response time, % manufacturers with a response score, response-data coverage, # observed quotes feeding pricing model.

---

## 17. Non-Goals (Phase 1)

- No payments/escrow/transactions. No full marketplace mechanics. No public reviews. No full autonomous AI sourcing agent. No verticals/geos beyond the launch set going *live* (schema still supports them).

---

## 18. Risks & Mitigations

| Risk | Mitigation |
|---|---|
| Thin-content SEO penalty | Enforce real per-page data; `noindex` low-completeness pages |
| Responsiveness cold start | Bootstrap scores from verification outreach; founder routes early RFQs |
| Data seeding is the hard part | Treat pipeline as a primary workstream; quality over volume |
| Scope creep (broad CPG + bilingual + RFQ) | Broad schema, narrow live launch, phased toggles |
| Legal (scraped data/PII/reviews) | Public-only data, provenance, opt-out, gated reviews + right-of-reply |
| **Media/image copyright** | Track rights status; prefer manufacturer-provided/licensed/placeholder (§20) |
| **Estimated-pricing liability** | Always labeled estimate w/ disclaimer + methodology; never presented as a quote |
| Incumbents notice | Speed + proprietary response/pricing data they can't scrape |

---

## 19. Roadmap

- **Phase 1 (MVP):** Supplements/US. Pipeline seeds **3,000–5,000+ manufacturers** (300–500 founder-verified core) with **10,000+ detailed product listings** → directory + faceted/AI search + manufacturer & product pages + claim/verify + buyer accounts/projects + RFQ inbox + live response scores + review *capture* + **Pricing Estimation Calculator (§24)** + AI stock-image system (§25) + admin/ops console (§27). Full SSR SEO/GEO page types for the launch vertical. Legal pages live.
- **Phase 1.5:** Cosmetics/food/packaging content on; Mexico geo + Spanish i18n; ranking/comparison/cost-guide pages at scale; calculator extended to new verticals.
- **Phase 2:** Public reviews, AI sourcing agent, data/market-intelligence products, first monetization experiments.

> **Final flagship deliverable:** the **Pricing Estimation Calculator** (§24) — the most complex and highest-SEO-value asset — is the capstone of Phase 1.

## 20. Resolved Decisions

All Phase-1 decisions are **RESOLVED** below. These are binding for the build; `/goal` should not need to ask questions about them.

### A. Media & image rights — **RESOLVED**
- **Decision:** Generate our **own AI "stock" images** in a consistent house style (see §25). One canonical stock image per product archetype (e.g., "bag of collagen powder") is **reused across all manufacturers who have not uploaded their own media**. Every AI/stock image is **watermarked/branded with the site name** (`Fabrera.com`). The same standard applies to all AI product images.
- **Also:** **Scrape and store the manufacturer's logo** (public asset) and display it on listings. Manufacturers can replace stock images with their own on claim.
- Track `rightsStatus` per asset; never hotlink third-party product photography.

### B. Estimated-pricing liability & trust — **RESOLVED**
- **Decision:** All estimates are **clearly labeled as estimates** with a visible **methodology breakdown, including per-line-item cost components** showing how we arrived at the figure (ingredients, packaging, labor/fill, overhead, etc.). Manufacturers can override on claim. Where confidence is too low, fall back to "Unknown — Request quote." See §9 + §24 (calculator).

### C. PII & contact-data compliance — **RESOLVED**
- **Decision:** **Public listings display only the domain name** to start (no public emails/phones/contact names). We **scrape and store ALL available contact info internally** (emails, phones, contact names) in the database for internal use/outreach. Provide an opt-out/takedown flow (`optedOut` flag). Internal contact data is access-controlled (admin only; RLS-protected).

### D. Duplicate detection & merge — **RESOLVED**
- **Decision:** **Domain is the primary identifier for v1.** Dedup is performed by normalized domain. `status:'merged'` + `mergedIntoId` handle collisions; admin merge tool resolves edge cases.

### E. Taxonomy governance — **RESOLVED**
- **Decision:** Seed a curated taxonomy per vertical; AI maps free-text to controlled vocabulary; **admin approves new terms**. No free-form tag sprawl.

### F. Data freshness / staleness — **RESOLVED**
- **Decision:** `lastVerifiedAt` per record; scheduled re-crawl; "last updated" shown on pages; confidence decays over time. **Crucially, freshness is wired to the pricing calculator's cost database** (§24): the ingredient/packaging/labor cost tables are versioned and **updated regularly**, and estimates are recomputed when underlying costs change.

### G. Spam / abuse / fake claims — **RESOLVED**
- **Decision:** Rate limits, **domain-email verification for claims** (claiming a domain requires an email address at that domain), buyer reputation score, and a manual approval queue in admin. All suggestions adopted.

### H. Search ranking algorithm — **RESOLVED**
- **Decision:** Transparent, data-driven default: `relevance × responsiveness × completeness × verification`. A clearly-labeled "sponsored" slot is reserved for future monetization. All suggestions adopted.

### I. Analytics & event tracking — **RESOLVED**
- **Decision:** Use **Google Analytics 4 + Google Tag Manager + Google Search Console** for web/SEO analytics. **However, Google products are NOT sufficient alone** for the product/moat funnel — GA4 is sampled, not reliable for joining RFQ→response events to specific manufacturers, and has data-retention limits. We therefore **also keep a first-party event log in Postgres** as the source of truth for RFQ/response/quote funnels (the moat). GTM/GA4 cover marketing-side behavior; Postgres covers product-side truth. (PostHog optional later; not required for MVP.)

### J. Admin / ops console scope — **RESOLVED**
- **Decision:** First-class MVP deliverable. Full scope + **automation opportunities** detailed in §27.

### K. AI matchmaking guardrails — **RESOLVED**
- **Decision:** AI parses query → structured filters only. Results always come from the DB; no fabricated manufacturers/products.

### L. Legal pages & policy — **RESOLVED**
- **Decision:** Terms, Privacy Policy, takedown/DMCA, and data-source disclosure stood up before public launch. Included in Definition of Done (§28).

### M. Brand / domain — **RESOLVED**
- **Decision:** Name is **Fabrera**, domain **`fabrera.com`** (purchased; DNS on Cloudflare). Coined mark (evokes *fabricar* = "to manufacture") chosen for trademark strength over descriptive options. Stock-image watermark and `NEXT_PUBLIC_SITE_NAME`/`NEXT_PUBLIC_SITE_URL` use `Fabrera` / `https://fabrera.com`. Formal TM clearance (USPTO classes 35/42/9 + IMPI/CIPO) recommended before filing.

### N. Sample/quote-to-order handoff — **RESOLVED**
- **Decision:** Phase 1 buyer journey ends at "quote/response received in inbox." Ordering/escrow deferred to Phase 2+.

---

## 21. Supabase SQL Schema

> Concrete Postgres DDL (Supabase). Conventions: `uuid` PKs (`gen_random_uuid()`), `timestamptz` `created_at`/`updated_at` on every table (trigger-maintained), snake_case. RLS enabled on all tables; policies summarized in §21.4. This is the build target — `/goal` implements migrations from this.

### 21.1 Enums & extensions
```sql
create extension if not exists "pgcrypto";
create extension if not exists "vector";      -- pgvector for semantic search
create extension if not exists "pg_trgm";     -- fuzzy text search

create type data_source       as enum ('scraped','ai_enriched','manufacturer_provided','founder_verified');
create type confidence_level  as enum ('low','medium','high');
create type verification_level as enum ('unverified','basic','verified','verified_facility');
create type claim_status      as enum ('unclaimed','pending_claim','claimed');
create type entity_status     as enum ('active','merged','hidden','archived');
create type pricing_state     as enum ('actual','estimated','unknown');
create type user_role         as enum ('buyer','manufacturer','admin');
create type media_role        as enum ('logo','product_photo','facility','label_mockup','gallery');
create type media_rights      as enum ('manufacturer_provided','scraped_public_logo','ai_generated_stock','licensed','placeholder');
create type rfq_status        as enum ('open','closed','awarded');
create type review_direction  as enum ('buyer_to_manufacturer','manufacturer_to_buyer');
create type review_display    as enum ('hidden','pending_moderation','published');
create type response_tier     as enum ('within_2h','within_24h','within_7d','rarely_responds','unknown');
```

### 21.2 Core tables
```sql
-- Users (extends Supabase auth.users)
create table app_user (
  id uuid primary key references auth.users(id) on delete cascade,
  email text not null,
  role user_role not null default 'buyer',
  display_name text,
  buyer_reputation_score numeric(5,2),
  locale text not null default 'en',
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

-- Controlled vocabularies (taxonomy)
create table category (
  id uuid primary key default gen_random_uuid(),
  slug text unique not null,
  name text not null,
  vertical text not null,                 -- supplements | cosmetics | food_beverage | packaging
  parent_id uuid references category(id),
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table capability (
  id uuid primary key default gen_random_uuid(),
  slug text unique not null,
  name text not null,
  description text,
  parent_id uuid references capability(id),
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table certification (
  id uuid primary key default gen_random_uuid(),
  slug text unique not null,
  name text not null,
  issuing_body text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

-- Manufacturer (domain = primary business identifier for v1)
create table manufacturer (
  id uuid primary key default gen_random_uuid(),
  slug text unique not null,
  domain text unique not null,            -- normalized; PRIMARY dedup key
  legal_name text,
  display_name text not null,
  description text,
  year_founded int,
  size_estimate text,                     -- micro|small|medium|large
  employee_count_range text,
  website_url text,
  logo_url text,                          -- scraped public logo, re-hosted
  verification_level verification_level not null default 'unverified',
  claim_status claim_status not null default 'unclaimed',
  claimed_by_user_id uuid references app_user(id),
  completeness_score int not null default 0,
  response_tier response_tier not null default 'unknown',
  status entity_status not null default 'active',
  merged_into_id uuid references manufacturer(id),
  last_verified_at timestamptz,
  search_vector tsvector,                 -- FTS
  embedding vector(1536),                 -- semantic search
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);
create index on manufacturer using gin (search_vector);
create index on manufacturer using gin (domain gin_trgm_ops);

-- Internal-only contact PII (admin/RLS-restricted; NEVER exposed publicly in Phase 1)
create table manufacturer_contact (
  manufacturer_id uuid primary key references manufacturer(id) on delete cascade,
  email text,
  phone text,
  contact_name text,
  additional_emails text[],
  additional_phones text[],
  address_line text,
  opted_out boolean not null default false,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table location (
  id uuid primary key default gen_random_uuid(),
  manufacturer_id uuid not null references manufacturer(id) on delete cascade,
  country text not null,                  -- ISO: US, MX, CA...
  state_region text,
  city text,
  postal_code text,
  lat double precision,
  lng double precision,
  is_headquarters boolean not null default false,
  is_production_site boolean not null default false,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

-- M:N joins
create table manufacturer_capability (
  manufacturer_id uuid references manufacturer(id) on delete cascade,
  capability_id uuid references capability(id) on delete cascade,
  primary key (manufacturer_id, capability_id)
);
create table manufacturer_category (
  manufacturer_id uuid references manufacturer(id) on delete cascade,
  category_id uuid references category(id) on delete cascade,
  primary key (manufacturer_id, category_id)
);
create table manufacturer_certification (
  manufacturer_id uuid references manufacturer(id) on delete cascade,
  certification_id uuid references certification(id) on delete cascade,
  verified boolean not null default false,
  certificate_url text,                   -- link on manufacturer's site
  certificate_file_url text,              -- scraped cert document (image/PDF), re-hosted
  certificate_file_type text,             -- 'image' | 'pdf'
  expires_at date,
  primary key (manufacturer_id, certification_id)
);
```

### 21.3 Products, pricing, media, RFQ, response, reviews
```sql
create table product (
  id uuid primary key default gen_random_uuid(),
  manufacturer_id uuid not null references manufacturer(id) on delete cascade,
  slug text not null,
  title text not null,
  summary text,
  description text,
  form text,                              -- powder|capsule|softgel|gummy|liquid|cream|sachet
  moq int,
  moq_unit text,
  supply_ability text,
  incoterms text[],
  completeness_score int not null default 0,
  status entity_status not null default 'active',
  search_vector tsvector,
  embedding vector(1536),
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  unique (manufacturer_id, slug)
);
create index on product using gin (search_vector);

create table product_attribute (
  id uuid primary key default gen_random_uuid(),
  product_id uuid not null references product(id) on delete cascade,
  key text not null, value text not null, unit text
);

create table product_variant (
  id uuid primary key default gen_random_uuid(),
  product_id uuid not null references product(id) on delete cascade,
  name text not null,
  option_values jsonb not null default '{}',
  sku text,
  created_at timestamptz not null default now()
);

create table product_category (
  product_id uuid references product(id) on delete cascade,
  category_id uuid references category(id) on delete cascade,
  primary key (product_id, category_id)
);

create table lead_time_tier (
  id uuid primary key default gen_random_uuid(),
  product_id uuid not null references product(id) on delete cascade,
  min_qty int not null, max_qty int, days int not null
);

create table customization_option (
  id uuid primary key default gen_random_uuid(),
  product_id uuid not null references product(id) on delete cascade,
  type text not null, available boolean not null default true,
  notes text, one_time_fee_amount numeric(12,2), one_time_fee_currency text,
  lead_time_impact_days int
);

create table sample_policy (
  product_id uuid primary key references product(id) on delete cascade,
  available boolean not null default false, free boolean not null default false,
  price_amount numeric(12,2), price_currency text, lead_time_days int, notes text
);

-- Pricing: one row per product (or variant), tri-state
create table pricing (
  id uuid primary key default gen_random_uuid(),
  product_id uuid references product(id) on delete cascade,
  variant_id uuid references product_variant(id) on delete cascade,
  state pricing_state not null default 'unknown',
  fx_captured_at timestamptz,
  estimate_confidence confidence_level,
  estimate_methodology text,
  estimate_range_low numeric(12,4),
  estimate_range_high numeric(12,4),
  calculator_version text,
  computed_at timestamptz,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);
create table price_tier (
  id uuid primary key default gen_random_uuid(),
  pricing_id uuid not null references pricing(id) on delete cascade,
  min_qty int not null, max_qty int,
  unit_price numeric(12,4) not null, currency text not null default 'USD',
  unit_of_measure text not null default 'each'
);
create table pricing_one_time_fee (
  id uuid primary key default gen_random_uuid(),
  pricing_id uuid not null references pricing(id) on delete cascade,
  label text not null, amount numeric(12,2) not null, currency text not null default 'USD'
);
create table cost_line_item (              -- transparent breakdown for estimates (§9.3, §24)
  id uuid primary key default gen_random_uuid(),
  pricing_id uuid not null references pricing(id) on delete cascade,
  component text not null, basis text not null,
  unit_cost numeric(12,4) not null, currency text not null default 'USD',
  source_cost_table_version text
);

create table media_asset (
  id uuid primary key default gen_random_uuid(),
  owner_type text not null,               -- 'manufacturer' | 'product'
  owner_id uuid not null,
  type text not null,                     -- image|video|360|logo
  role media_role not null default 'gallery',
  url text not null,
  caption text, source_url text,
  rights_status media_rights not null default 'placeholder',
  is_ai_stock boolean not null default false,
  stock_archetype_id text,
  brand_watermark text,
  sort_order int not null default 0,
  created_at timestamptz not null default now()
);

create table stock_image_archetype (
  id text primary key,                    -- e.g. 'collagen-powder-pouch'
  label text not null, prompt_snapshot text not null, url text not null,
  applies_to_category_ids uuid[],
  created_at timestamptz not null default now()
);

create table faq (
  id uuid primary key default gen_random_uuid(),
  owner_type text not null, owner_id uuid not null,
  question text not null, answer text not null,
  created_at timestamptz not null default now()
);

-- Buyer workspace
create table project (
  id uuid primary key default gen_random_uuid(),
  buyer_user_id uuid not null references app_user(id) on delete cascade,
  name text not null, product_type text, specs jsonb default '{}',
  certifications_needed text[], moq_target int, notes text,
  saved_manufacturer_ids uuid[],
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table rfq (
  id uuid primary key default gen_random_uuid(),
  buyer_user_id uuid not null references app_user(id) on delete cascade,
  project_id uuid references project(id),
  title text not null, details text not null,
  target_manufacturer_ids uuid[] not null,
  quantity int, timeline text,
  status rfq_status not null default 'open',
  created_at timestamptz not null default now()
);

create table message_thread (
  id uuid primary key default gen_random_uuid(),
  rfq_id uuid references rfq(id) on delete cascade,
  manufacturer_id uuid not null references manufacturer(id),
  buyer_user_id uuid not null references app_user(id),
  created_at timestamptz not null default now()
);

create table message (
  id uuid primary key default gen_random_uuid(),
  thread_id uuid not null references message_thread(id) on delete cascade,
  from_user_id uuid references app_user(id),
  from_manufacturer_id uuid references manufacturer(id),
  body text not null,
  sent_at timestamptz not null default now()
);

create table response_event (              -- THE MOAT
  id uuid primary key default gen_random_uuid(),
  manufacturer_id uuid not null references manufacturer(id) on delete cascade,
  rfq_id uuid references rfq(id),
  thread_id uuid references message_thread(id),
  sent_at timestamptz not null,
  first_reply_at timestamptz,
  replied boolean not null default false,
  source text not null default 'rfq'       -- rfq | verification_outreach
);

create table response_score (              -- cached/computed per manufacturer
  manufacturer_id uuid primary key references manufacturer(id) on delete cascade,
  response_rate_pct numeric(5,2), median_first_response_hours numeric(8,2),
  quote_conversion_pct numeric(5,2), tier response_tier not null default 'unknown',
  sample_size int not null default 0, computed_at timestamptz not null default now()
);

create table review (                      -- captured now, displayed Phase 2
  id uuid primary key default gen_random_uuid(),
  direction review_direction not null,
  author_user_id uuid not null references app_user(id),
  manufacturer_id uuid references manufacturer(id),
  subject_user_id uuid references app_user(id),
  rating_communication int, rating_quality int, rating_timeliness int, rating_pricing int,
  comment text, verified_transaction boolean not null default false,
  display_status review_display not null default 'hidden',
  created_at timestamptz not null default now()
);

create table saved_search (
  id uuid primary key default gen_random_uuid(),
  buyer_user_id uuid not null references app_user(id) on delete cascade,
  query text not null, filters jsonb not null default '{}',
  alert_enabled boolean not null default true, last_notified_at timestamptz,
  created_at timestamptz not null default now()
);

-- Provenance (per-field source/confidence), generic
create table field_provenance (
  id uuid primary key default gen_random_uuid(),
  entity_type text not null, entity_id uuid not null, field text not null,
  source data_source not null, confidence confidence_level not null,
  source_url text, methodology text, captured_at timestamptz not null default now()
);

-- First-party analytics event log (moat funnel source of truth)
create table analytics_event (
  id bigint generated always as identity primary key,
  event_name text not null, user_id uuid, manufacturer_id uuid, rfq_id uuid,
  properties jsonb default '{}', created_at timestamptz not null default now()
);

-- Domain-email claim verification
create table listing_claim (
  id uuid primary key default gen_random_uuid(),
  manufacturer_id uuid not null references manufacturer(id) on delete cascade,
  user_id uuid not null references app_user(id),
  claim_email text not null,              -- must match manufacturer.domain
  verification_token text not null,
  verified_at timestamptz,
  status text not null default 'pending', -- pending | verified | rejected
  created_at timestamptz not null default now()
);
```

### 21.4 Cost database tables (powering §24 calculator)
```sql
create table cost_table_version (
  id text primary key,                    -- e.g. '2026-06'
  notes text, effective_at timestamptz not null default now()
);
create table ingredient_cost (
  id uuid primary key default gen_random_uuid(),
  version_id text not null references cost_table_version(id),
  ingredient_slug text not null, name text not null,
  cost_per_kg numeric(12,4) not null, currency text not null default 'USD',
  grade text,                             -- quality tier
  confidence confidence_level not null default 'medium',
  source_url text
);
create table packaging_cost (
  id uuid primary key default gen_random_uuid(),
  version_id text not null references cost_table_version(id),
  packaging_slug text not null, name text not null,
  unit_cost numeric(12,4) not null, currency text not null default 'USD',
  size_spec text, confidence confidence_level not null default 'medium'
);
create table process_cost (               -- per-unit run cost by delivery form
  id uuid primary key default gen_random_uuid(),
  version_id text not null references cost_table_version(id),
  form text not null,                     -- capsule|gummy|tablet|liquid_fill...
  per_unit_cost numeric(12,4) not null, currency text not null default 'USD',
  moq_breakpoint int, confidence confidence_level not null default 'medium'
);
create table overhead_assumption (
  id uuid primary key default gen_random_uuid(),
  version_id text not null references cost_table_version(id),
  label text not null, pct numeric(5,2) not null   -- overhead/margin % assumptions
);
```

### 21.5 RLS policy summary
- **Public read:** `manufacturer`, `product`, `location`, taxonomy tables, `media_asset` (non-internal), `price_tier`/`pricing`/`cost_line_item`, `faq`, published `review`. **Public read excludes `manufacturer_contact`** (internal PII).
- **Buyer:** read/write own `project`, `rfq`, `saved_search`, `message` (own threads), `review` (authored).
- **Manufacturer (claimed):** read/write own `manufacturer`/`product`/`media_asset`/`pricing`; read own threads/leads; read own `response_score`.
- **Admin:** full access incl. `manufacturer_contact`, `listing_claim`, cost tables, provenance, analytics.
- **Triggers:** maintain `updated_at`; refresh `search_vector`/`embedding`; recompute `response_score` + `completeness_score`.

### 21.6 Formulation & ingredient-master tables (powering §24.7–24.10)
```sql
create table ingredient_master (
  id uuid primary key default gen_random_uuid(),
  slug text unique not null,
  name text not null,
  inci_name text,                          -- cosmetics
  synonyms text[],
  default_grade text,
  density_g_per_ml numeric(8,4),           -- capsule/softgel capacity math
  daily_value_amount numeric(12,4),        -- % DV basis; null => "†"
  daily_value_unit text,
  upper_limit_amount numeric(12,4),        -- UL / safe ceiling
  upper_limit_unit text,
  topical_max_pct numeric(6,3),            -- cosmetics concentration cap
  allergen_tags text[],
  notes text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table formulation_template (
  id uuid primary key default gen_random_uuid(),
  slug text unique not null,               -- e.g. 'collagen-powder', 'nad-capsules'
  name text not null,
  vertical text not null,
  category_id uuid references category(id),
  default_form text not null,
  default_count int,
  default_serving_size text,
  default_packaging_slug text,
  trending_score numeric(8,2) default 0,   -- ranked from demand data
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table formulation_template_ingredient (
  id uuid primary key default gen_random_uuid(),
  template_id uuid not null references formulation_template(id) on delete cascade,
  ingredient_id uuid not null references ingredient_master(id),
  amount_per_serving numeric(12,4) not null,
  unit text not null,                      -- mg|mcg|g|IU
  is_active boolean not null default true
);

create table capsule_capacity (            -- reference table for fill validation
  size text primary key,                   -- '000','00','0','1','2','3','4'
  volume_ml numeric(6,3) not null,
  typical_fill_mg_at_density numeric(8,2) not null
);
```
- `ingredient_master` is versionable via the same cadence as the cost DB (§20.F); link to `ingredient_cost` (§21.4) by `slug` for pricing.
- Constraints engine (§24.9) reads `density_g_per_ml`, `upper_limit_*`, `topical_max_pct`, `capsule_capacity`.

### 21.7 Ingredient price observations (raw scraped pricing — §23.3, §24.11)
> Tier-level raw observations from ingredient retailers. We **preserve the full price curve** (every size/qty break) — never collapse to one price/tier. `ingredient_cost` (§21.4) becomes the *normalized/derived* layer the calculator reads; `ingredient_price_observation` is the *raw* layer feeding it + the price-index over time.
```sql
create table ingredient_source (
  id uuid primary key default gen_random_uuid(),
  site_domain text unique not null,        -- e.g. 'bulksupplements.com'
  vendor_name text,
  platform text,                           -- 'shopify' | 'custom' | 'woocommerce' ...
  endpoint_type text,                      -- 'products_json' | 'json_ld' | 'sitemap' | 'html'
  channel text,                            -- 'retail' | 'wholesale'
  ingredient_category text,                -- 'supplement' | 'cosmetic' | 'both'
  robots_ok boolean default true,
  crawl_cadence text,                      -- e.g. 'weekly'
  last_scraped_at timestamptz,
  notes text,
  created_at timestamptz not null default now()
);

create table ingredient_price_observation (
  id bigint generated always as identity primary key,
  source_id uuid references ingredient_source(id),
  source_site text not null,
  canonical_ingredient_id uuid references ingredient_master(id),  -- null until canonicalized
  ingredient_name_raw text not null,        -- as listed on the site
  product_url text,
  vendor text,
  sku text,
  variant_id text,
  size_label text,                          -- '1 kg', '100 g', '16 oz'
  quantity numeric(14,4),                   -- parsed amount
  unit text,                                -- 'g','kg','ml','l','oz','lb','count'
  price numeric(12,4),
  compare_at_price numeric(12,4),           -- sale/original
  currency text not null default 'USD',
  in_stock boolean,
  price_per_kg numeric(14,4),               -- computed/normalized
  price_per_unit numeric(14,6),             -- computed/normalized
  form text,                                -- powder | capsule | liquid | oil
  grade text,                               -- food | USP | cosmetic | pharma
  certifications text[],
  country_of_origin text,
  category text,                            -- supplement | cosmetic
  raw_payload jsonb,                        -- full original record (extract-maximally)
  scraped_at timestamptz not null default now()
);
create index on ingredient_price_observation (canonical_ingredient_id);
create index on ingredient_price_observation (source_site, ingredient_name_raw);
create index on ingredient_price_observation (scraped_at);
```
- Repeated scrapes over time build a **price index** (trend) per ingredient/tier.
- Canonicalization maps `ingredient_name_raw` → `ingredient_master` (synonyms/CAS/INCI); unmapped rows queue for admin review (§27).

### 21.8 Operational & admin tables (powering §27, §33, §36, §39)
```sql
create table feature_flag (
  key text primary key,                 -- e.g. 'vertical.cosmetics', 'geo.mx', 'tool.tariff_lookup'
  enabled boolean not null default false,
  description text,
  updated_at timestamptz not null default now()
);

create table site_setting (
  key text primary key,
  value jsonb not null,
  updated_at timestamptz not null default now()
);

create table seo_meta_override (         -- per-page meta/canonical/noindex overrides
  id uuid primary key default gen_random_uuid(),
  path text unique not null,
  title text, description text, canonical text,
  noindex boolean not null default false,
  updated_at timestamptz not null default now()
);

create table redirect (                  -- 301 manager
  id uuid primary key default gen_random_uuid(),
  from_path text unique not null,
  to_path text not null,
  status_code int not null default 301,
  created_at timestamptz not null default now()
);

create table notification (
  id bigint generated always as identity primary key,
  user_id uuid not null references app_user(id) on delete cascade,
  type text not null,                    -- rfq_received|message|claim_status|alert|system
  payload jsonb not null default '{}',
  read_at timestamptz,
  created_at timestamptz not null default now()
);
create index on notification (user_id, read_at);

create table notification_preference (
  user_id uuid primary key references app_user(id) on delete cascade,
  email_enabled boolean not null default true,
  in_app_enabled boolean not null default true,
  prefs jsonb not null default '{}'
);

create table email_template (
  key text primary key,                  -- 'claim_verify','rfq_received','message','alert','digest'
  subject text not null, body_html text not null, body_text text,
  updated_at timestamptz not null default now()
);

create table admin_audit_log (
  id bigint generated always as identity primary key,
  actor_user_id uuid references app_user(id),
  action text not null,                  -- 'merge','publish_cost_version','impersonate','edit', ...
  entity_type text, entity_id text,
  detail jsonb default '{}',
  created_at timestamptz not null default now()
);

create table lead_magnet (
  id uuid primary key default gen_random_uuid(),
  slug text unique not null, title text not null,
  asset_url text, category text, gated boolean not null default true,
  created_at timestamptz not null default now()
);

create table lead_capture (
  id bigint generated always as identity primary key,
  email text not null, lead_magnet_id uuid references lead_magnet(id),
  source text, captured_at timestamptz not null default now()
);

create table tool_widget (               -- embeddable calculator/tool registry (§29.5)
  id uuid primary key default gen_random_uuid(),
  slug text unique not null, name text not null,
  enabled boolean not null default true,
  embed_allowed boolean not null default true,
  config jsonb not null default '{}',
  created_at timestamptz not null default now()
);

create table widget_embed (              -- track where widgets are embedded (backlinks)
  id bigint generated always as identity primary key,
  tool_slug text not null, host_domain text, first_seen timestamptz not null default now(),
  load_count int not null default 0
);
```
- RLS: `feature_flag`/`site_setting`/`seo_meta_override`/`redirect`/`email_template`/`admin_audit_log`/`tool_widget` are **admin-only**; `notification`/`notification_preference` are per-user; `lead_capture` admin-only write via public form endpoint.

---

## 22. Next.js Route Map

> App Router. **All public routes are SSG/ISR or SSR (no client-only content rendering — §12.1).** `(group)` = route group.

### 22.1 Public (SEO-critical, server-rendered)
```
/                                   Home / product-first discovery landing (§7.0): category grid + hot products + search
/search                             Faceted + AI NL search results (SSR)
/v/[verticalSlug]                   Vertical / department landing (Supplements, Beauty, Packaging…) — products + categories, manufacturers deeper
/ingredients/[slug]                 Product / ingredient hub page (§41) — "hot products" target
/m/[slug]                           Manufacturer profile
/m/[slug]/p/[productSlug]           Product listing (Alibaba-style)
/c/[categorySlug]                   Category page
/c/[categorySlug]/[stateOrCountry]  Category × Geo
/cert/[certSlug]                    Certification page
/cap/[capabilitySlug]               Capability / equipment page
/best/[rankingSlug]                 Ranking page (response-data powered)
/compare/[a]-vs-[b]                 Comparison page
/cost/[costGuideSlug]               Cost / pricing guide page
/calculator                         Pricing Estimation Calculator (§24) — interactive, SSR shell + hydrated UI
/calculator/[categorySlug]          Pre-scoped calculator landing (SEO: "collagen manufacturing cost calculator")
/about /how-it-works
/legal/terms /legal/privacy /legal/takedown /legal/data-sources
/sitemap.xml /robots.txt
```

### 22.2 Auth & buyer/manufacturer app (mostly CSR behind auth)
```
/login /signup /auth/callback
/claim/[manufacturerSlug]           Start claim (domain-email verification)
/dashboard                          Buyer dashboard (sourcing CRM)
/dashboard/projects/[projectId]     Project workspace
/dashboard/rfqs /dashboard/rfqs/[rfqId]
/dashboard/inbox /dashboard/inbox/[threadId]
/dashboard/saved
/manufacturer                       Manufacturer dashboard (claimed)
/manufacturer/listings /manufacturer/listings/[productId]/edit
/manufacturer/leads /manufacturer/analytics
```

### 22.3 Admin (gated, §27)
```
/admin                              Ops overview
/admin/manufacturers                Review/edit/merge seeded records
/admin/claims                       Approve claims
/admin/moderation                   Reviews/content queue
/admin/taxonomy                     Manage categories/capabilities/certs
/admin/pipeline                     Scrape/enrich/verify jobs + status
/admin/cost-tables                  Manage cost DB versions (§24)
/admin/stock-images                 Manage AI stock archetypes (§25)
```

### 22.4 API / route handlers
```
/api/search                         Structured + semantic search
/api/ai/parse-query                 NL query → structured filters (DB-bounded, §20.K)
/api/calculator/estimate            Pricing estimate (line-item breakdown)
/api/rfq                            Create/send RFQ → seeds response_event
/api/messages                       Inbox send/receive (response capture)
/api/claim/verify                   Domain-email claim verification
/api/webhooks/email                 Inbound email relay → response tracking
/api/cron/recrawl                   Scheduled refresh
/api/cron/recompute-scores          Response/completeness recompute
/api/events                         First-party analytics ingest
/api/sitemap                        Dynamic sitemap generation
```

---

## 23. Data Sourcing Strategy

> *Where* we obtain manufacturer + cost data before/while building. Goal: responsibly assemble 3,000–5,000+ supplements/US manufacturers and the cost tables behind the calculator. All sources are **public**; respect robots.txt/ToS; store provenance.

### 23.1 Manufacturer discovery sources
**Industry directories & associations (highest-yield seeds):**
- ThomasNet, IndustryNet, Kompass, GlobalSpec, MFG.com (discovery only).
- Trade associations: **CRN** (Council for Responsible Nutrition), **NPA** (Natural Products Association), **AHPA** (American Herbal Products Association), **UNPA**, **IPA** (probiotics), **PCPC** (cosmetics), **IFT** (food tech).
- Trade-show exhibitor lists: **SupplySide West/East**, **Expo West/East (New Hope)**, **Vitafoods**, **MakeUp in LA**, **PACK EXPO**.
- Contract-manufacturer roundup lists & "top X manufacturers" blog posts (seed list → verify).

**Government / registry data (authoritative, great for verification):**
- **FDA registries:** Dietary Supplement / Food Facility Registration, Drug Establishment (NDC/DRLS), and **FDA Dun & Bradstreet (DUNS)** facility data.
- **USDA Organic Integrity Database** (certified-organic handlers/processors).
- **NSF, UL, SQF, BRCGS certified-facility directories** (cert verification + discovery).
- State business registries / Secretary of State filings; OpenCorporates.
- For Mexico (Phase 1.5): **SIEM**, **ProMéxico/secretaría de economía** exporter directories, **COFEPRIS** registrations.

**Web & search-derived:**
- **Google Search Console** (once live): mine actual queries hitting our pages to discover demand + gaps; reverse-engineer long-tail manufacturer/category terms to target.
- **Google Programmable Search / SERP scraping** for "contract manufacturer + {category} + {state}" to find sites, then crawl each manufacturer's own site (products, certs, public pricing, logo, contact).
- **Web searches / LLM-assisted discovery** to expand seed lists and cross-check.
- Maps/Places data (Google Places, OpenStreetMap) for geocoding + facility validation.
- LinkedIn company pages (size/employee signals — respect ToS, no auth-scraping).
- Crunchbase / business-data APIs for firmographics.

**Enrichment APIs (optional, paid):**
- Clearbit/People Data Labs/Apollo-style firmographic enrichment; email/phone discovery for internal contact records.

### 23.2 Product, spec & pricing sources
- Each manufacturer's **own website**: product/catalog pages, spec sheets (PDF parsing), MOQ/lead-time, any public pricing, logo, and **certification documents (downloadable cert images/PDFs — e.g., NSF, cGMP, USDA Organic — re-hosted as verification evidence).**
- Marketplaces as comps for *estimation only* (e.g., Alibaba listings like the reference) — used to calibrate the calculator, not copied.
- Ingredient cost benchmarks: supplier price lists, **ingredient marketplaces** (e.g., Knowde, chemical/ingredient distributors), trade publications, USDA/commodity indices, and **observed RFQ quotes over time** (proprietary, compounding).
- Packaging cost benchmarks: packaging suppliers' public pricing, MOQ-based quote pages.

### 23.3 Ingredient-pricing data sources (work already started — cloud branch `cursor/seo-growth-tools-plan-cf5e`, PR #1)
A separate workstream built the foundation of the **ingredient pricing database** that powers the calculator's cost DB (§21.4, §21.7). Key results to fold into the build:

**Technical finding — Shopify `/products.json`:** many ingredient retailers run Shopify, exposing a public read-only `/products.json` feed (paginated, 250/page) with every product + every variant (size tier) + price. Trivial, reliable, no HTML parsing. Reusable scraper: `scrapers/shopify_scraper.py <domain> --name <slug>`.

**Data captured (DONE):** **BulkSupplements.com — 794 products / 4,767 variant price tiers.** Per tier: product name, URL, product_type, size_option, price, compare_at_price (sale), SKU, grams, availability, variant_id. Example — *Collagen Peptides Powder:* 100 g $18.97 · 250 g $21.97 · 500 g $27.97 · 1 kg $40.97 · 5 kg $187.97 · 20 kg $446.58. Stored in `data/bulksupplements/` (products CSV, variants CSV, raw JSON).

**Confirmed Shopify (✅ trivially scrapable via `/products.json`):**
`bulksupplements.com` (done), `purebulk.com`, `nutricost.com`, `n101nutrition.com`, `ingredi.com`, `lotioncrafter.com`, `formulatorsampleshop.com`, `wholesalesuppliesplus.com`, `essentialwholesale.com`, `camdengrey.com`, `tkbtrading.com`.

**NOT Shopify (need custom scrapers — investigate sitemap/JSON-LD/HTML):**
`mountainroseherbs.com`, `starwest-botanicals.com`, `bulkapothecary.com`, `makingcosmetics.com`, `newdirectionsaromatics.com`, `brambleberry.com` (blocks bots), `ingredientstodiefor.com`, `theherbarie.com`, `skinactives.com`.

**Priority sites selling BOTH supplement + cosmetic ingredients:** Bulk Apothecary, Mountain Rose Herbs, Starwest Botanicals, New Directions Aromatics (custom), Essential Wholesale (Shopify ✅).

> **Repo reconciliation note:** the cloud work lives on remote branch `cursor/seo-growth-tools-plan-cf5e` (PR #1) and includes `seo-growth-plan.md`, `scrapers/`, and `data/`. Our local `docs/PLAN.md` and `.env.local` were not visible to that agent and are not yet committed. **Action:** merge PR #1 and reconcile `seo-growth-plan.md` into this master plan; bring `scrapers/` + `data/` into the main tree. (Not done here — no git operations performed.)

### 23.4 Method
1. Build a **source registry** (each source: type, URL, crawl cadence, robots/ToS status, endpoint type: products.json | JSON-LD | sitemap | HTML).
2. Crawl → AI extract → normalize to taxonomy → dedup by domain → score completeness → store provenance. **Persist full raw payloads** (extract-maximally principle, §13).
3. Queue low-confidence/critical fields for **admin review** (§27).
4. Seed cost tables (§21.4, §21.7) from the ingredient-price observations; version them; refresh on cadence (§20.F).

### 23.5 Pre-build data tasks (do now, before `/goal`)
- [ ] Assemble initial **seed source registry** (directories, associations, registries above).
- [ ] Pull FDA/USDA/NSF facility datasets for supplements/US.
- [ ] Stand up GSC + GA4 properties so query data starts accruing on day one.
- [ ] Collect 50–100 manufacturer sites manually to validate the scrape/enrichment schema.
- [ ] Run `shopify_scraper.py` across the 10 remaining confirmed Shopify ingredient sites (§23.3).
- [ ] Build custom scrapers for the priority non-Shopify "both" sites (Mountain Rose Herbs, Starwest Botanicals, Bulk Apothecary, New Directions Aromatics).
- [ ] Add the normalization step (price_per_kg/price_per_unit per tier) into the unified ingredient-price table (§21.7) — no single-discount/single-tier assumption (§24.11).
- [ ] Merge PR #1 and reconcile cloud `scrapers/` + `data/` + `seo-growth-plan.md` into the main tree.

---

## 24. Pricing Estimation Calculator (Flagship Deliverable)

> The capstone Phase-1 deliverable: an interactive, **transparent, line-item** cost estimator for CPG manufacturing — and a major SEO/lead-gen asset. It is both a **standalone tool** (`/calculator`) and the **engine** behind every listing's estimated price (§9).

### 24.1 What it does
A buyer configures a product and gets an **estimated unit-cost range with a full line-item breakdown** + downstream price tiers by MOQ. Every number links to its basis and cost-table version. Clearly labeled **"Estimate — not a quote."**

**Two entry modes:**
1. **Quick mode (preset formulations)** — for buyers who don't know ingredients/dosages. They pick a **stock/standard formulation** (especially popular & trending products) and get an instant estimate. See §24.7.
2. **Custom mode** — full ingredient/packaging configuration (§24.2). Presets pre-fill custom mode, so a buyer can start from a preset and then adjust.

### 24.2 Inputs (progressive, category-aware)
- **Vertical & category** (supplements → e.g. capsule/gummy/powder; cosmetics → cream/serum; food/bev; packaging).
- **Delivery form / format** (capsule, softgel, tablet, gummy, powder/sachet, liquid, cream).
- **Active ingredient(s)** with **dosage/concentration** (search across a large ingredient DB — thousands of supplement ingredients), plus excipients/other ingredients.
- **Quality grade** (standard / premium / branded-ingredient).
- **Serving config:** count per bottle/unit, serving size, fill weight/volume.
- **Packaging:** primary (bottle type/material/size, pouch, blister), closure, secondary (label, box), inserts.
- **Certifications/processing requirements** (organic, NSF, vegan, allergen-free → cost adders).
- **MOQ / order quantity** (drives per-unit run cost + tiering).
- **Region** (US/MX) & currency.

### 24.3 Calculation model
```
# ingredient $/kg is selected at the price tier matching the order quantity (§24.11),
# starting from retail-as-ceiling × adjustable wholesale_discount_factor (user-overridable)
ing_cost_per_kg(ingredient) = price_per_kg[tier matching order_qty, grade, version]
                              × (1 − wholesale_discount_factor)
unit_cost = Σ(active_ingredients: qty_per_unit × ing_cost_per_kg)
          + Σ(other_ingredients)
          + process_cost[form, moq_breakpoint, version]
          + primary_packaging[version] + secondary_packaging[version]
          + labor_fill (line_rate ÷ throughput)
          + certification_adders
unit_cost_with_overhead = unit_cost × (1 + overhead_pct + margin_pct)
range = unit_cost_with_overhead × [1 − band, 1 + band]   // band from aggregate confidence
price_tiers = apply MOQ-based discount curve to unit_cost_with_overhead
```
- Cost inputs come from the **versioned cost DB** (§21.4): `ingredient_cost`, `packaging_cost`, `process_cost`, `overhead_assumption`.
- Output persists to `pricing` + `cost_line_item` (snapshot incl. `calculator_version`).
- **Confidence** = function of how many inputs came from high-confidence cost rows vs defaults; low aggregate confidence → wider band or "Unknown."

### 24.4 Output (UI)
- Headline estimated unit-cost **range** + per-MOQ price tiers.
- **Line-item table** (§9.3) with each component, its basis, and cost-table version.
- Prominent **"Estimate, not a quote"** disclaimer + methodology explainer.
- CTA: "Find manufacturers who make this" (pre-filters search) / "Request quotes" (RFQ).

### 24.5 SEO / GEO value
- `/calculator/[categorySlug]` landing pages target high-intent queries ("collagen manufacturing cost calculator," "gummy supplement cost per unit").
- Generates shareable, citable, data-backed content LLMs can reference.

### 24.6 Maintenance
- Cost DB versioned + refreshed on cadence (§20.F); estimates recomputed when versions change; old snapshots retained for transparency.

### 24.7 Stock / standard formulations & trending presets
Most buyers don't know exactly which ingredients/dosages they need. We provide a library of **ready-made formulation templates** they can pick to get a fast estimate, then adjust.
- **Examples / popular & trending presets:** "Curcumin Pills — 30 count," "NAD+ Capsules," "Collagen Powder," "Ashwagandha Gummies," "Magnesium Glycinate," "Creatine Monohydrate," "Electrolyte Stick Packs," "Vitamin D3+K2 Softgels."
- Each preset is a `FormulationTemplate` (§24.10 / §21.6): a set of ingredients at standard dosages + default form, count, and packaging.
- **Trending presets** are surfaced/ranked using our own demand data (search queries, calculator usage, RFQ volume) — a self-reinforcing SEO + product loop.
- Presets power dedicated SEO landing pages (e.g. `/calculator/collagen-powder`, "cost to manufacture NAD+ supplement").
- Presets are **fully adjustable**: change dosages, swap ingredients, change count/size/packaging — recalculates live within the constraints engine (§24.9).

### 24.8 Supplement Facts / Cosmetic Ingredient panel generation
The calculator renders a **regulatory-style panel** from the chosen ingredients, updating live as inputs change.
- **Supplements:** a **Supplement Facts panel** — serving size, servings per container, each ingredient with amount per serving, **% Daily Value** (computed from the ingredient master's DV/RDA where established; "†" when no DV established), and "Other Ingredients" (excipients).
- **Cosmetics:** an **Ingredients (INCI) list** ordered by concentration (descending), with actives flagged.
- Panels are generated, **adjustable**, and exportable; they also enrich the listing/product pages and are great structured content for SEO/GEO.
- Panel output is advisory (clearly labeled) — not a substitute for regulatory review.

### 24.9 Constraints & safe-limits engine
Adjustments are validated against real-world manufacturing and safety constraints so estimates stay physically and legally plausible.
- **Capacity constraints:**
  - **Capsule fill:** each capsule size has a max fill mass by powder density (e.g., size 00 ≈ 735 mg @ ~0.8 g/mL); the engine validates total fill ≤ capacity and suggests larger size, more capsules/serving, or a different form when exceeded.
  - **Liquid/softgel fill:** each softgel/liquid cap holds a bounded volume; validate actives + carrier ≤ fill volume.
  - **Gummy/tablet:** max actives per piece by weight; powder/stick-pack max fill weight.
- **Safe / regulatory limits:**
  - Per-ingredient **Upper Limits / Tolerable Upper Intake (UL)**, max label claims, and topical concentration caps (e.g., regulated actives in cosmetics) flagged with warnings (hard block vs soft warning).
  - Allergen/excipient incompatibilities flagged.
- **Behavior:** violations produce inline warnings + suggested fixes; hard limits block an estimate from being presented as plausible. All limits sourced from the ingredient master (§24.10) and versioned (§20.F).

### 24.10 Data behind the calculator (object models)
```typescript
interface FormulationTemplate {       // a preset like "Collagen Powder" or "NAD+ Capsules"
  id: string;
  slug: string;                       // SEO, e.g. "collagen-powder"
  name: string;
  vertical: string;
  categoryId: string;
  defaultForm: string;                // capsule | gummy | powder | softgel | tablet | liquid | cream
  defaultCount?: number;              // e.g. 30 (count per bottle)
  defaultServingSize?: string;
  defaultPackagingSlug?: string;
  trendingScore?: number;             // ranked from demand data
  ingredients: FormulationIngredient[];
  createdAt: string;
}

interface FormulationIngredient {
  ingredientId: string;
  amountPerServing: number;
  unit: string;                       // mg, mcg, g, IU
  isActive: boolean;
}

interface IngredientMaster {          // the ingredient knowledge base
  id: string;
  slug: string;
  name: string;
  inciName?: string;                  // for cosmetics
  synonyms?: string[];
  defaultGrade?: string;
  densityGPerMl?: number;             // for capsule/softgel capacity math
  dailyValue?: { amount: number; unit: string };   // for % DV; null => "†"
  upperLimit?: { amount: number; unit: string };    // UL / safe ceiling
  topicalMaxPct?: number;             // cosmetics concentration cap
  allergenTags?: string[];
  notes?: string;
}

interface CapsuleCapacity {           // reference table for fill math
  size: string;                       // '000','00','0','1','2','3','4'
  volumeMl: number;
  typicalFillMgAtDensity: number;     // at a reference density
}
```
> These map to SQL in §21.6.

### 24.11 Ingredient cost normalization (RESOLVED approach)
How raw scraped ingredient prices (§21.7) become calculator inputs. Open question was: *what wholesale discount to apply, and which size tier to normalize against?* — both vary by ingredient, manufacturer, whether they already stock it, and order quantity.

**Decision (do NOT hardcode a discount or a single tier):**
1. **Preserve the entire price curve.** Store every size/qty tier per ingredient per vendor (`ingredient_price_observation`).
2. **Compute `price_per_kg` / `price_per_unit` at every tier** so the estimator can select the tier matching the buyer's order quantity (e.g., 1 kg for a small run vs 25 kg for a large run).
3. **Treat retail prices as a ceiling.** Apply an **adjustable wholesale discount factor** surfaced as a calculator input (default by ingredient/category, user-overridable), rather than a baked-in constant.
4. **Separate by grade** (food/USP/cosmetic/pharma) and **flag retail vs wholesale** channel; prefer wholesale observations when available.
5. **Track over time** (scheduled re-scrapes + `scraped_at`) to build a **price index**; the calculator uses the latest version but retains history.
6. **Canonicalize across vendors** (synonyms/CAS/INCI) so multiple vendor prices roll up to one canonical ingredient, enabling min/median/spread per tier.

This makes estimates quantity-aware and defensible, and the per-tier curve + price index becomes part of the proprietary cost-benchmark dataset (future monetization).

---

## 25. AI Stock Image & Branded Media Standard

> Resolves §20.A. We avoid third-party image copyright risk by generating our **own** product imagery in a consistent house style, reused across listings, and branded.

### 25.1 Principles
- **One canonical AI "stock" image per product archetype** (e.g., `collagen-powder-pouch`, `gummy-bottle`, `softgel-bottle`, `cream-jar`). Stored once as a `stock_image_archetype` (§21.3) and **reused across all manufacturers who have not uploaded their own media**.
- **Every AI/stock image is watermarked/branded** with the site name (`Fabrera.com`). Branding is baked into the asset.
- **Consistent house style:** neutral/seamless background, centered product, soft studio lighting, consistent aspect ratio + resolution, no real brand names/logos on the depicted product.
- Applies uniformly to **all AI product images**.

### 25.2 Logos (separate from stock images)
- **Scrape the manufacturer's public logo**, re-host in Supabase Storage (`rights_status = 'scraped_public_logo'`), and display it on the listing. Logos are the one scraped visual we display.

### 25.3 Lifecycle
1. On seed, a product is mapped to the closest archetype → shows the shared, watermarked AI stock image + the scraped logo.
2. On claim, the manufacturer can **upload real product/facility media** (`rights_status = 'manufacturer_provided'`), which overrides the stock image for that listing only.
3. New archetypes are created/managed via admin (`/admin/stock-images`), storing the generation `prompt_snapshot` for reproducibility/consistency.

### 25.4 Implementation notes
- Generation via an image model; watermark applied in a deterministic post-process step (so branding is identical across images).
- Archetype → category mapping lives in `stock_image_archetype.applies_to_category_ids`.
- Open Graph/social images can reuse the same branded assets.

---

## 26. Environment & Configuration

> `.env.local` (gitignored) holds real values; `.env.example` is the committed template. Files created in this step with placeholders; **you will populate real values before build.** `NEXT_PUBLIC_*` are browser-exposed — never put secrets there.

### 26.1 Variable inventory
| Variable | Purpose | Secret? |
|---|---|---|
| `NEXT_PUBLIC_SITE_URL` | Canonical site URL (SEO, OG, sitemap) — `https://fabrera.com` | no |
| `NEXT_PUBLIC_SITE_NAME` | Brand name / image watermark text — `Fabrera` | no |
| `NEXT_PUBLIC_SUPABASE_URL` | Supabase project URL | no |
| `NEXT_PUBLIC_SUPABASE_ANON_KEY` | Supabase anon (RLS-bound) key | no |
| `SUPABASE_SERVICE_ROLE_KEY` | Server-side admin (bypasses RLS — server only) | **yes** |
| `SUPABASE_JWT_SECRET` | Verify Supabase JWTs server-side | **yes** |
| `DATABASE_URL` | Direct Postgres connection (migrations/jobs) | **yes** |
| `OPENAI_API_KEY` | NL query parsing, enrichment, estimates | **yes** |
| `IMAGE_GEN_API_KEY` | AI stock-image generation (§25) | **yes** |
| `RESEND_API_KEY` (or `POSTMARK_*`) | Transactional email + inbox relay | **yes** |
| `INBOUND_EMAIL_WEBHOOK_SECRET` | Verify inbound email webhooks (response tracking) | **yes** |
| `GOOGLE_SERVICE_ACCOUNT_KEY` | Full service-account JSON — auths **Vertex AI Gemini (Google Search grounding)** + GSC. **Confirmed working.** | **yes** |
| `GOOGLE_CLOUD_PROJECT` | GCP project id (`bloom-platform-489223`) | no |
| `VERTEX_LOCATION` | Vertex region (`us-central1`) | no |
| `VERTEX_MODEL` | Gemini model (`gemini-2.5-flash`; note `gemini-2.0-flash-001` NOT available in this project) | no |
| `GOOGLE_SERVICE_ACCOUNT_EMAIL` | (optional) convenience copy of client_email | no |
| `GOOGLE_SEARCH_CONSOLE_SITE_URL` | GSC property to query | no |
| `NEXT_PUBLIC_GA4_MEASUREMENT_ID` | Google Analytics 4 | no |
| `NEXT_PUBLIC_GTM_ID` | Google Tag Manager container | no |
| `GOOGLE_SITE_VERIFICATION` | Search Console site verification meta | no |
| `GOOGLE_MAPS_API_KEY` | Geocoding / Places (facility validation) | **yes** |
| `SERP_API_KEY` (or Programmable Search) | Discovery crawling (§23) | **yes** |
| `SCRAPER_API_KEY` | Managed scraping/proxy (optional) | **yes** |
| `ENRICHMENT_API_KEY` | Firmographic/contact enrichment (optional) | **yes** |
| `CRON_SECRET` | Protect `/api/cron/*` endpoints | **yes** |
| `VERCEL_URL` / `VERCEL_ENV` | Provided by Vercel at runtime | no |

### 26.2 Notes
- **Service account (`GOOGLE_SERVICE_ACCOUNT_KEY`) — CONFIRMED WORKING:** authenticates to **Vertex AI** (`aiplatform.googleapis.com` enabled on `bloom-platform-489223`). Tested call: `POST https://us-central1-aiplatform.googleapis.com/v1/projects/bloom-platform-489223/locations/us-central1/publishers/google/models/gemini-2.5-flash:generateContent` with `tools:[{"googleSearch":{}}]` returns grounded, structured manufacturer JSON. Scope `https://www.googleapis.com/auth/cloud-platform`.
- Use **`gemini-2.5-flash`** (the `2.0-flash-001` publisher model is not accessible in this project).
- The same service account is used for **GSC**; grant it access to the GSC property.
- The JSON key contains a PEM `private_key` with literal newlines — parse with a lenient JSON reader (Python `json.loads(..., strict=False)`) or base64-encode the whole blob; document the chosen approach in the build.
- Vercel project env vars mirror `.env.example`; secrets set in Vercel dashboard, not committed.

---

## 27. Admin / Ops Console & Automation

> Resolves §20.J. A solo founder cannot run the data pipeline manually — the console must make the operator 10x. Below: console scope + **what can be automated** vs. what needs a human-in-the-loop.

### 27.1 Console modules (`/admin/*`)
**Data & catalog**
- **Overview:** pipeline health, queue sizes, new claims, flagged items, data-quality KPIs, freshness/staleness summary.
- **Manufacturers:** browse/search/edit; view provenance per field; **merge duplicates** (domain-based); set verification level; hide/archive; trigger re-crawl/re-enrich for one record.
- **Products/listings:** edit listings, fix mis-classifications, manage variants, override AI fields, bulk edit.
- **Claims:** review domain-email claim requests; approve/reject; see verification token status.
- **Taxonomy:** manage categories/capabilities/certs; **approve AI-proposed new terms**; merge/rename; reorder/featured.
- **Pipeline & sources:** run/schedule scrape, enrich, verify jobs; view logs, errors, success rates; manage the **source registry** (§23.3/§23.4) incl. robots/ToS + endpoint type.
- **Cost tables:** create/edit cost-DB versions; bulk-import ingredient/packaging/process costs; publish a version → triggers estimate recompute (§24.6); manage `ingredient_master`, `formulation_template`, `capsule_capacity`.
- **Ingredient price observations:** browse scraped pricing, canonicalization queue (map raw → `ingredient_master`), spot-check tiers.
- **Stock images:** manage AI archetypes; regenerate; map to categories (§25).

**Trust, users & content**
- **Moderation:** queue for reviews (gated), Q&A, user reports; takedown/opt-out requests (§34).
- **Users & roles:** list users, assign roles (buyer/manufacturer/admin), suspend/ban, **support impersonation** (read-only, audit-logged) for debugging buyer/manufacturer views.
- **RFQ & leads oversight:** view RFQs/threads (for support + anti-abuse), spam flags, re-route/refund (future monetization).
- **Outreach:** send verification/claim-invite emails; manage templates; track responses (feeds `response_event`).
- **Content / editorial CMS:** edit the templated + unique copy on SEO pages (category/geo/cert/cost/guide intros, FAQs), manage guides/reports/lead-magnet assets (§29).

**Growth, SEO & config**
- **SEO management:** per-page meta/canonical/`noindex` overrides, `301` redirect manager, sitemap controls, structured-data preview, broken-link/crawl-error report (from GSC).
- **Search & ranking tuning:** adjust ranking weights (relevance × responsiveness × completeness × verification) and the reserved sponsored slot; preview impact (§35).
- **Calculators/tools admin:** manage formulation presets + trending order, tool config, embeddable-widget allowlist (§29).
- **Feature flags & settings:** toggle features/verticals/geos live (drives the "build broad, launch narrow" phasing), site settings, maintenance mode.
- **Email templates & notifications:** edit transactional/notification templates, preview, test-send (§33).
- **Integrations & secrets health:** show which env-gated integrations are configured/healthy (Supabase, Vertex, OpenAI, Resend, Maps, GSC/GA4/GTM) without exposing secret values.

**Observability & governance**
- **Jobs & queues monitor:** cron/job runs, failures, retries, durations; manual re-run.
- **Analytics dashboard:** first-party moat funnel (RFQ→response→quote), top searches/queries (demand intel feeding new presets/pages), SEO KPIs.
- **Audit log:** every admin/destructive action recorded (who/what/when), incl. impersonation and cost-version publishes.
- **Data export/import:** CSV/JSON export of any table; bulk import with provenance tagging.
- **Legal/compliance:** takedown/opt-out request tracker, data-source disclosure management, retention controls.

### 27.2 What to AUTOMATE (no human needed)
- **Crawling & extraction:** scheduled crawl of source registry + manufacturer sites; AI extraction → structured fields.
- **Classification:** AI maps free-text → taxonomy; confidence-scored.
- **Dedup by domain:** automatic normalize + merge of exact-domain collisions.
- **Completeness scoring:** auto-computed on write.
- **Estimated pricing:** calculator auto-runs for every product lacking actual pricing; auto-recompute on cost-version publish.
- **Stock-image assignment:** auto-map product → nearest archetype.
- **Geocoding:** auto via Maps API.
- **Response/score recompute:** cron recomputes response_score + tiers.
- **Alerts:** saved-search alert emails.
- **Sitemap regeneration:** on content change.
- **Staleness flags:** auto-flag records past freshness threshold for re-crawl.
- **Verification outreach:** auto-send templated outreach + auto-log replies via inbound email webhook.

### 27.3 HUMAN-IN-THE-LOOP (review queue, not full auto)
- Approving **new taxonomy terms** the AI proposes.
- Approving **listing claims** (anti-fraud; though domain-email match can auto-approve low-risk cases).
- **Merging fuzzy duplicates** that aren't exact-domain matches.
- **Moderating** reviews/Q&A and handling takedown/opt-out requests.
- Spot-checking **low-confidence** extracted fields and **founder-verified** tier promotions.
- Publishing **cost-table versions** (sanity check before estimates shift site-wide).

### 27.4 Design principle
Default to **"automate + queue exceptions."** Every automated step writes provenance + confidence; anything below a confidence threshold or flagged as risky lands in a review queue rather than going live silently.

---

## 28. Definition of Done / Acceptance Criteria

> **Two gates (read with §39.1).** `/goal` drives **Code-DoD** to completion: every feature, schema, pipeline, tool, and test implemented and **passing CI against the seed sample + fixtures (§38)**. This is finite and is what "the build is done" means. **Data-DoD** items (real-world volume like "≥3,000 manufacturers / ≥10,000 listings") are an **ops ramp produced by running the already-built, tested pipeline over time — they are NOT build blockers and must never stall a `/goal` run.** Items below tagged **[DATA]** are Data-DoD (capability built + tested against fixtures = done for the build; real volume accrues later); everything else is Code-DoD.
>
> Each feature requires automated tests (unit/integration) + a manual verification note. "Done" is binary per §39.3 (test or documented check); no subjective polishing.

### 28.1 Global "done" bar (applies to every feature)
- [ ] Implemented per this spec; no TODO stubs in shipped paths.
- [ ] Automated tests written and passing (unit + integration where applicable).
- [ ] RLS policies enforced and tested (no public access to internal PII / `manufacturer_contact`).
- [ ] Lint + typecheck + build pass with zero errors.
- [ ] Public pages pass the **SSR no-JS SEO check** (§12.1): content + meta + JSON-LD present in raw HTML; validated via Rich Results Test.
- [ ] Analytics events fire (GA4/GTM + first-party `analytics_event`).
- [ ] Mobile-responsive + basic a11y (semantic HTML, alt text, keyboard nav).

### 28.2 Feature acceptance checklist
**Data & pipeline**
- [ ] Supabase schema (§21) migrated; enums, indexes, triggers, RLS in place.
- [ ] Ingestion pipeline implemented + **tested against recorded fixtures** (dedup by domain, provenance/confidence written). **[DATA]** Live target ≥3,000 supplements/US manufacturers accrues by running it (ops ramp, not a build blocker).
- [ ] Listing generation implemented (logos scraped/re-hosted, PII stored internal-only) + tested on the seed sample. **[DATA]** Live target ≥10,000 product listings accrues via the pipeline.
- [ ] Completeness scoring + `noindex` gating for thin listings working (verified on seed sample).
- [ ] Cost tables (§21.4) seeded + versioned.
- [ ] **Ingredient pricing DB:** `ingredient_source` + `ingredient_price_observation` populated from confirmed Shopify `/products.json` sites (§23.3); `price_per_kg`/`price_per_unit` normalized per tier (§24.11); full raw payloads retained.
- [ ] **Shopify scraper** (`scrapers/shopify_scraper.py`) + custom scrapers for priority non-Shopify sites in the tree; scheduled re-runs build the price index.
- [ ] **Vertex AI Gemini + Google Search grounding** wired via service account (`gemini-2.5-flash`) for grounded discovery/enrichment.

**Discovery & SEO**
- [ ] Faceted search (all facets) + AI NL search (DB-bounded, §20.K) working.
- [ ] All public page types (§22.1) render server-side with schema.org JSON-LD.
- [ ] `sitemap.xml`, `robots.txt`, canonical, `hreflang` scaffolding present.
- [ ] Ranking/comparison/cost pages generate from real data.

**Listings**
- [ ] Alibaba-style product pages (§8) render all sections.
- [ ] Tri-state pricing (§9) with **line-item breakdown** for estimates; "estimate, not a quote" labeling.
- [ ] AI stock images (§25): one branded archetype reused across unclaimed listings; logo displayed.

**Calculator (flagship, §24)**
- [ ] `/calculator` + `/calculator/[categorySlug]` live, SSR shell + hydrated UI.
- [ ] Inputs, calculation model, line-item output, confidence/range all implemented.
- [ ] Estimates persist to `pricing` + `cost_line_item`; recompute on cost-version publish.
- [ ] **Quick mode** with stock/standard + trending formulation presets (§24.7); presets adjustable and pre-fill custom mode.
- [ ] **Supplement Facts / cosmetic INCI panel** generated live from ingredients with % DV (§24.8).
- [ ] **Constraints & safe-limits engine** (§24.9): capsule/softgel fill capacity, max per-piece actives, UL/topical caps — warnings + hard blocks.
- [ ] `ingredient_master`, `formulation_template`, `capsule_capacity` tables seeded.

**Certifications**
- [ ] Certification documents (NSF/cGMP/USDA Organic/SQF images or PDFs) scraped, re-hosted, and displayed on listings as trust signals.

**Accounts & workflow**
- [ ] Buyer accounts, dashboard (CRM), projects/workspace.
- [ ] RFQ creation → send to N manufacturers → on-platform inbox messaging.
- [ ] **ResponseEvent capture** on send/reply; response_score computed + displayed (day one).
- [ ] Sample request tracking.
- [ ] Review **capture** (all four ratings) stored, display gated (`hidden`).
- [ ] Manufacturer claim via **domain-email verification**; manufacturer dashboard + leads.

**Admin & ops (§27)**
- [ ] All `/admin/*` modules functional; automations running; review queues working.

**Compliance & infra (§26, §20.C/L)**
- [ ] Public listings show **domain only**; no public PII.
- [ ] Opt-out/takedown flow works.
- [ ] Legal pages (terms, privacy, takedown, data-sources) published.
- [ ] `.env` wired; GSC (service account) + GA4 + GTM connected; cron endpoints protected.
- [ ] Deployed to Vercel; Supabase prod configured.

### 28.3 Gates (build vs public launch)
- **Code-complete gate (the `/goal` target):** all 28.1 + all non-`[DATA]` items in 28.2 checked against the seed sample + fixtures; site passes a Googlebot fetch / Rich-Results review on a sample of each public page type; §37 budgets met. **When this passes, the build is done** — `/goal` stops here and reports, it does not wait on data volume.
- **Public-launch gate (ops, after the code-complete gate):** the `[DATA]` items have accrued via the live pipeline and the dataset meets §13.1 targets. This is an operational ramp tracked separately and is **not** part of the unattended build.

---

## 29. SEO Tools & Growth Engine

> Folded in from the cloud `seo-growth-plan.md` (now retired). Strategy: free interactive tools rank for high-intent, bottom-of-funnel keywords and earn backlinks; programmatic pages own the long tail; gated assets convert traffic into emails/RFQs; original data reports earn digital-PR backlinks. **The Pricing Estimation Calculator (§24) is the anchor — everything feeds it traffic and feeds off its data.** Open questions from that doc are resolved by our chat decisions: audience = both buyers + manufacturers (tools skew buyer-side first); verticals = supplements → cosmetics/food/packaging; geo = US → Mexico; ingredient DB seeded (§21.7).

### 29.1 Free interactive tools (link magnets + high-intent SEO)
Each tool page: intro copy + FAQ block + related tools + a "Get real quotes from vetted Americas manufacturers" CTA (routes to RFQ). Each tool **ships as an embeddable widget** (see §29.5).
- **Anchor — Manufacturing Cost Estimator** (supplements & cosmetics) — §24. Phase 1.
- **Nearshoring savings calculator** — China vs Mexico vs USA *total landed cost* (unit + tariffs + freight + lead time + MOQ + risk). Rides the reshoring tailwind; highly shareable.
- **Landed cost / TCO calculator** — unit + duties + freight + insurance + brokerage.
- **Tariff / HTS duty-rate lookup** — product or HTS code + country of origin → estimated duty.
- **Private-label margin & retail pricing calculator** — COGS → wholesale → MSRP.
- **MOQ & break-even calculator** — units until profitable.
- **"Made in USA" labeling compliance checker** — interactive quiz vs FTC "all or virtually all" rules.
- **Cost-per-serving / cost-per-unit calculator** (supplements).
- **Supplement Facts panel generator** + **Cosmetic INCI builder** — already specced in §24.8; also standalone tools.
- **Secondary:** Amazon FBA profitability, freight/container estimator, lead-time estimator, reorder-point/safety-stock, supplier comparison scorecard (PDF export), nearshoring carbon-footprint comparison.

### 29.2 Programmatic SEO (own the long tail)
Built on the §10 page taxonomy + our data. Adds explicitly:
- **Directory pages:** `[category] manufacturers in [state/country]`.
- **Capability pages:** "gummy supplement manufacturers", "vegan capsule manufacturers", "organic skincare manufacturers".
- **Certification landing pages** (GMP/FDA/NSF/USDA Organic/Leaping Bunny) — filters + standalone pages.
- **Ingredient cost pages (from our DB):** "cost of ashwagandha extract", "bulk price of hyaluronic acid" — SEO real estate nobody else has (powered by §21.7). High-demand ones graduate into full **pillar hub pages (§41)**.
- **Comparison pages:** "[Country A] vs [Country B] manufacturing for [product]".
- All quality-gated (unique data per page; `noindex` thin pages — §10.3).

### 29.3 Gated lead magnets (email + RFQ capture)
Trade a downloadable for an email; route hot leads into the marketplace.
- RFQ / spec-sheet templates (supplement & cosmetic), manufacturer vetting checklist, supplier/quality (cGMP) audit checklist, legal templates (NDA/MSA/quality agreement), compliance checklists (FDA labeling, cosmetic MoCRA, FTC Made-in-USA), nearshoring playbook ebook, product-launch Gantt, cost-benchmark mini-report (teaser of our DB), ingredient glossary/INCI decoder.

### 29.4 Data-driven content & digital PR (backlinks at scale)
Original data → journalists link. Powered by our proprietary cost/response data:
- Annual **"State of Nearshoring in the Americas"** report; **Manufacturing Cost Index** (by category/region, quarterly); **"Made in USA premium"** study; **Tariff impact tracker**; **Ingredient price trend pages** (from §21.7 over time).

### 29.5 Distribution: embeddable widgets (backlink engine)
- Every calculator/tool ships with an **"Embed this calculator"** snippet (iframe or script) → bloggers/agencies embed → free do-follow backlinks + brand exposure.
- Requires: a sandboxed embeddable build of each tool, an allowlist/branding (watermark + link back), and lightweight analytics on embeds. Managed in admin (§27.1).

### 29.6 Phasing
- **Phase 1:** anchor cost estimator (§24) + its SEO landing pages.
- **Phase 1.5:** nearshoring savings, tariff/HTS lookup, private-label margin, MOQ/break-even; embeddable-widget wrapper; programmatic directory v1; gated RFQ templates + vetting checklist.
- **Phase 2:** Made-in-USA checker, ingredient cost pages from DB, Manufacturing Cost Index + first report, remaining calculators.

---

## 30. Design System & UI Foundations

> The UI must be consistent and buildable without per-screen guesswork. **`DESIGN.md` is a prerequisite for the deterministic UI build** (§39) and is produced via `/design-shotgun` **before** `/goal` runs (see answer to design question).

### 30.1 DESIGN.md must define
- Brand: name/logo usage, color palette (semantic tokens: primary, surface, text, success/warn/danger), dark mode stance.
- Typography scale (font families, sizes, weights, line-heights).
- Spacing/grid, radius, shadows, breakpoints (mobile-first).
- Component inventory + states (buttons, inputs, selects, cards, tables, badges, tabs, modals, toasts, empty states, skeletons, pagination, filters/facets, rating/score chips, verification badges, calculator widgets, facts-panel component, comparison table, listing gallery).
- Page templates: home (**product-first** — see §7.0; approved mockup `designs/homepage-search-20260617/APPROVED-homepage.png`), vertical/department landing, product/ingredient hub (§41), search/results, manufacturer profile, product listing, category/geo/cert/capability, ranking/comparison, cost guide, calculator, dashboards (buyer/manufacturer), admin.
- Accessibility + content tone guidelines.

### 30.2 Implementation
- Component library: React + Tailwind (tokens map to Tailwind config) with a headless primitive set (e.g., Radix) for a11y; or shadcn/ui. Single source of truth in `components/ui/`.
- Storybook-style states optional; required: every component has documented states incl. loading/empty/error.
- Built against tokens from `DESIGN.md` — no ad-hoc colors/spacing in feature code.

---

## 31. Testing & QA Strategy

> DoD (§28) requires tests; this defines the *how*. Tests must be deterministic (no live network in CI — use fixtures/mocks).

- **Unit (Vitest):** pricing/calculator math (incl. line-item breakdown + constraints engine §24.9), domain normalization/dedup, completeness/response scoring, taxonomy mapping, currency/unit conversion. High coverage on pure logic.
- **Integration (Vitest + Supabase local / Postgres test container):** RLS policies (public cannot read `manufacturer_contact`; buyers/manufacturers scoped correctly), migrations apply cleanly, search queries, RFQ→response_event capture, claim/domain-email verification, calculator persistence.
- **E2E (Playwright):** core journeys — search → listing → RFQ → inbox; claim flow; calculator quick + custom modes; admin approve/merge. Run against a seeded fixture DB.
- **SEO render tests:** assert each public page type returns content + `<title>`/meta/canonical/`hreflang` + schema.org JSON-LD **in server-rendered HTML** (no-JS fetch), and validates against schema (§12.1).
- **Accessibility tests:** axe checks on key templates (§37).
- **Performance budgets:** Lighthouse CI thresholds (§37).
- **Scraper tests:** run against **recorded fixtures** (saved `products.json`/HTML snapshots), not live sites — keeps CI deterministic.
- **Data-quality checks:** assertions that seeded sample meets completeness gating and no public PII leaks.

---

## 32. Infrastructure, CI/CD & Operations

- **Repo/CI:** GitHub Actions — on PR: install, typecheck, lint, unit+integration tests, build, Lighthouse CI, axe; block merge on failure. Preview deploys via Vercel per PR.
- **Migrations:** versioned SQL migrations (Supabase CLI). CI applies migrations to an ephemeral DB and runs RLS/integration tests. Forward-only; never edit a shipped migration.
- **Environments:** local → preview (Vercel) → production. Separate Supabase projects (or schemas) for dev/prod. Env via `.env.local` / Vercel project vars (§26).
- **Background jobs:** Supabase scheduled functions / cron route handlers (protected by `CRON_SECRET`) for crawl/enrich/verify/score-recompute/sitemap/alerts. Idempotent (safe to re-run without double effects).
- **Observability:** error tracking (Sentry), structured logs, uptime check on home + a sample of each page type, job-run dashboard in admin (§27).
- **Backups & DR:** rely on Supabase automated backups; document restore steps; export critical tables (manufacturers, ingredient observations) to object storage weekly. Retain raw scrape payloads.
- **Media/CDN:** Supabase Storage + `next/image` optimization; watermark pipeline (§25) runs at ingest; serve responsive sizes.

---

## 33. Email, Notifications & Deliverability

- **Sending domain auth:** configure **SPF, DKIM, DMARC** on the sending domain so outreach/notifications land in inboxes (critical for the responsiveness moat — outreach must be delivered).
- **Transactional email (Resend/Postmark):** auth (magic link/verify), claim verification, RFQ received, new message in thread, saved-search alerts, weekly digest.
- **Inbound email relay:** tracked addresses / webhook (`INBOUND_EMAIL_WEBHOOK_SECRET`) parse manufacturer replies → write `message` + `response_event` (powers response scoring even for email-only manufacturers).
- **In-app notifications:** `notification` table + bell UI; types: rfq_received, message, claim_status, alert, system. Read/unread state.
- **Preferences:** per-user notification settings; unsubscribe links (CAN-SPAM compliance).
- **Anti-abuse:** rate-limit outbound; suppression list for opt-outs/bounces.

---

## 34. Security, Privacy & Compliance (consolidated)

- **AuthN/AuthZ:** Supabase Auth; **RLS on every table** (policies in §21.5), tested (§31). Admin role gated; service-role key server-only.
- **PII handling:** public listings show **domain only**; `manufacturer_contact` (emails/phones/names) is internal/admin-only, RLS-locked. Encrypt at rest (Supabase default); restrict export to admin + audit-logged.
- **Compliance:** CAN-SPAM (unsubscribe + sender identity), **CASL** (Canada), **LFPDPPP** (Mexico), **CCPA/CPRA** (California). Honor opt-out/takedown via `optedOut` + request tracker (§27).
- **Legal pages:** Terms, Privacy Policy, Cookie/consent banner (GA4/GTM), DMCA/takedown, **data-source disclosure** (how we collect public data). Live before public launch (§28).
- **Scraping ethics:** public data only; respect robots.txt/ToS in source registry; identify our crawler UA; backoff/rate-limit; store provenance + source URL for every field.
- **App security:** input validation, output escaping (XSS — malicious script injection via user input), CSRF protection on mutations, parameterized queries (SQL injection defense), secrets never in `NEXT_PUBLIC_*`, dependency audit in CI, rate limits on auth/RFQ/claim/calculator endpoints.
- **Abuse:** fake RFQs/claims/reviews → rate limits, domain-email claim verification, buyer reputation, moderation queue (§20.G).

---

## 35. Search, Ranking & Recommendations Spec

- **Index:** Postgres FTS (`search_vector`) for keyword; **pgvector** embeddings (OpenAI `text-embedding-3-small`, 1536-dim) for semantic/NL search on manufacturers + products.
- **NL query path (§20.K):** AI parses query → structured filters (category, capability, cert, geo, MOQ, capacity); results come **only** from the DB (no fabrication). Falls back to FTS+vector hybrid.
- **Ranking formula (default, tunable in admin §27):**
  `score = w1·relevance + w2·responsiveness + w3·completeness + w4·verification (+ sponsored boost, clearly labeled)`
  with documented default weights (e.g., 0.4/0.25/0.2/0.15). Deterministic given inputs.
- **Facets:** vertical, category, capability, certification, country/state/city, MOQ range, capacity, verification level, response tier, price availability.
- **Recommendations:** "similar manufacturers", "more from this manufacturer", "manufacturers who make {preset}" — vector similarity + shared category/capability.

---

## 36. Analytics Event Taxonomy

> First-party events (`analytics_event`, §21.2) are the moat's source of truth; GA4/GTM mirror marketing behavior. Canonical event names:
- `search_performed` (query, parsed_filters, results_count, mode)
- `listing_viewed` (manufacturer_id, product_id)
- `calculator_started` / `calculator_estimated` (preset_id?, category, confidence, est_range)
- `rfq_created` / `rfq_sent` (rfq_id, manufacturer_count)
- `message_sent` / `message_replied` → also writes `response_event`
- `sample_requested`
- `claim_started` / `claim_verified`
- `signup` / `login` (role)
- `saved_search_created` / `alert_clicked`
- `lead_magnet_downloaded` (asset_id, email_captured)
- `widget_embedded` / `widget_loaded` (tool, host_domain)
- `outbound_cta_clicked` (target)
Each event: timestamp, user_id?, session_id, properties jsonb. Used for funnels, demand intel (top searches → new presets/pages), and SEO/tool ROI.

---

## 37. Quality Bars (Accessibility, Performance, i18n)

- **Accessibility:** target **WCAG 2.1 AA** — semantic HTML, labeled controls, keyboard nav, focus states, alt text (incl. AI stock images), color contrast, 44px touch targets. axe checks in CI (§31).
- **Performance (Core Web Vitals budgets):** LCP < 2.5s, CLS < 0.1, INP < 200ms on public pages; Lighthouse CI perf ≥ 90 mobile on key templates. SSG/ISR for content; image optimization; minimal client JS on content pages.
- **i18n:** English (Phase 1) → Spanish (Phase 1.5) with `next-intl`-style message catalogs + `hreflang`; multi-currency (USD/MXN) and multi-unit handled in data (§11.5/§24); locale-aware formatting.

---

## 38. Seed Data, Fixtures & Data Dictionary

> So the build is testable from day one without scraping thousands of records.
- **Taxonomy seeds:** curated category/capability/certification lists for supplements (Phase 1), then cosmetics/food/packaging. Committed as seed SQL/JSON.
- **Cost-DB seed:** initial `cost_table_version` + ingredient/packaging/process costs (bootstrapped from BulkSupplements data §21.7 + benchmarks). `capsule_capacity` reference table seeded with standard sizes.
- **Formulation presets seed:** the trending presets in §24.7 (Collagen Powder, NAD+, Curcumin 30ct, etc.).
- **Manufacturer fixtures:** the 5 validated manufacturers (Captek, GMP Labs, Cpack, Certified Nutra, Vitaquest) + ~20 more as a **seed sample** for tests/E2E and initial launch content. The build **may synthesize this seed sample deterministically** (committed seed SQL/JSON) where real records aren't in the repo — flagged `confidence='seed'` with `provenance='seed'` so it's distinguishable from scraped data and replaceable by the pipeline. **Do not block the build hunting for real records** (§39.1).
- **Stock-image archetypes seed:** core archetypes (collagen-powder-pouch, gummy-bottle, softgel-bottle, cream-jar, capsule-bottle).
- **Data dictionary:** §11 (object models) + §21 (SQL) are the canonical dictionary; every field has provenance/confidence semantics (§11.1).

---

## 39. Build Execution Contract (Determinism Guardrails)

> **Purpose (answers "can agents finish without looping or asking questions?"):** this section makes the build a *finite, ordered, verifiable* task. The build is **complete when §28 DoD checks pass against the seed/fixture data** — not when thousands of real records are acquired (that's a separate ops ramp, §39.3).

### 39.1 Code-complete vs Data-complete (the key distinction)
- **Code-complete (deterministic, the build target):** all features, schema, pipelines, tools, tests, and SEO rendering implemented and **passing CI against fixtures + the seed sample** (§38). This is achievable without external uncertainty and is what `/goal` drives to.
- **Data-complete (ops ramp, NOT a build blocker):** reaching 3,000–5,000+ manufacturers / 10,000+ listings (§13.1) happens by running the (already-built, tested) pipeline over time. Agents must **not** block "done" on acquiring live data volume.

### 39.2 Ordered milestones (dependencies explicit)
1. **M0 Foundations:** Next.js + Supabase + Tailwind scaffold; CI; env wiring; `DESIGN.md` present (from `/design-shotgun`).
2. **M1 Schema & seeds:** all migrations (§21) + RLS + seed data/fixtures (§38); integration tests green.
3. **M2 Discovery & listings:** search (FTS+vector), manufacturer + product pages, SSR/SEO + schema.org; render tests green.
4. **M3 Calculator:** cost estimator (quick + custom), facts panel, constraints engine, line-item output, persistence; unit tests green.
5. **M4 Accounts & RFQ:** auth, buyer/manufacturer dashboards, projects, RFQ + inbox, response_event capture + scoring, claim/domain-email.
6. **M5 Pipeline & admin:** scrapers (Shopify + custom), enrichment (OpenAI + Vertex), dedup, stock-image + cert-doc ingest, full admin console (§27).
7. **M6 SEO growth:** programmatic page types, additional calculators + embeddable widgets, lead magnets, sitemaps (§29).
8. **M7 Compliance & launch:** legal pages, notifications/email auth (SPF/DKIM/DMARC), analytics wiring, a11y/perf budgets, final DoD pass.

### 39.3 Determinism guardrails (so agents don't stall or ask)
- **Missing optional API key →** feature degrades gracefully behind an env check; tests use mocks/fixtures; mark with a tracked `TODO(env: VAR)` but do **not** block the milestone. Required keys for a milestone are listed in `.env.example`.
- **Live third-party sites →** never in the test gate; use recorded fixtures (§31). Real crawling is an ops job.
- **Ambiguity →** consult the **Default Decisions Registry (§40)** instead of asking. If a needed decision is genuinely absent there, pick the documented-convention default, record it in §40 via changelog, and continue.
- **Un-designed screen →** approved `/design-shotgun` mockups exist for **home, vertical landing, manufacturer profile, and product listing** (`DESIGN.md` §6). Every other screen (hub §41, calculator §24, search/results, dashboards, admin, auth, legal) is built **directly from the `DESIGN.md` component system + its §6 page-template spec**. **Never pause the build to run `/design-shotgun` or ask for a design** — `DESIGN.md` is sufficient and authoritative.
- **Scope →** Phase 1 only; anything Phase 1.5/2 is explicitly deferred (don't gold-plate). Feature flags gate not-yet-launched verticals/geos/tools.
- **"Done" is binary:** every item in §28 is a checkbox with an automated test or a documented manual check. No subjective "polish forever."
- **No infinite loops:** if a test can't pass after 3 distinct attempts, the agent records a `BLOCKED` note (what was tried + recommendation) and moves to the next independent task rather than looping.

### 39.4 What could still block determinism — and the resolution
| Potential blocker | Resolution |
|---|---|
| Design not decided | `DESIGN.md` (M0 gate) is the authority. 4 key screens have approved mockups; all others build from `DESIGN.md` directly. **Do not pause mid-build for design** (§39.3). |
| Real data volume (3–5k records) | Separated as ops ramp (§39.1); build uses seed sample. |
| Third-party scraping flakiness | Fixtures in CI; live crawl is ops. |
| Missing keys (image-gen, Maps, Resend) | Graceful degradation + mocks; required vs optional listed in `.env.example`. |
| Subjective "good enough" | Replaced by §28 binary checks + §37 numeric budgets. |
| Open product questions | Pre-answered in §40 registry. |

---

## 40. Default Decisions Registry (no-questions-needed defaults)

> Canonical answers so `/goal` never needs to stop and ask. If reality contradicts one, follow it and note the change in the Changelog.
- **Framework:** Next.js (App Router, TypeScript). **Styling:** Tailwind + shadcn/ui (Radix primitives). **DB/Auth/Storage:** Supabase.
- **Package manager:** `pnpm`. **Node:** LTS. **Lint/format:** ESLint + Prettier. **Tests:** Vitest + Playwright.
- **Rendering:** SSG/ISR for content, SSR where dynamic; never client-only for indexable content (§12.1).
- **IDs:** UUIDv4. **Timestamps:** `timestamptz`, UTC. **Money:** integer-safe `numeric`; currency stored explicitly; default USD.
- **Slugs:** kebab-case, ASCII-folded, unique per scope. **Domain normalization:** lowercase, strip protocol/`www`/trailing slash.
- **Units:** metric in storage (g/kg/ml/L) with display conversion; counts as integers.
- **AI models:** OpenAI for extraction/classification/embeddings (`text-embedding-3-small`); **Vertex `gemini-2.5-flash` + Google Search** for grounded discovery (§26).
- **Pricing default state:** `unknown` until actual scraped or estimated; estimates require line-item breakdown (§9.3).
- **Wholesale discount factor:** default per-category value, user-overridable (§24.11); never hardcoded site-wide.
- **Ranking weights:** 0.40 relevance / 0.25 responsiveness / 0.20 completeness / 0.15 verification (admin-tunable §35).
- **Completeness index threshold for `noindex`:** < 60/100 is `noindex` until enriched.
- **Reviews:** captured, `display_status='hidden'` until Phase 2.
- **Locale:** `en` default; `es` Phase 1.5. **Geo launch:** US first; Mexico Phase 1.5.
- **Launch vertical:** supplements; cosmetics/food/packaging behind feature flags.
- **Image strategy:** AI branded stock per archetype reused for unclaimed; scraped public logo displayed; manufacturer uploads override (§25).
- **Accessibility/perf:** WCAG 2.1 AA; CWV budgets in §37.
- **Brand:** **Fabrera** (`fabrera.com`); `NEXT_PUBLIC_SITE_NAME=Fabrera`, `NEXT_PUBLIC_SITE_URL=https://fabrera.com`; image watermark `Fabrera.com`.
- **Design coverage:** approved mockups exist for 4 screens (`DESIGN.md` §6); all other screens build from `DESIGN.md` directly — no mid-build design exploration, no design questions (§39.3).
- **Done = code-complete:** the unattended build finishes at the §28.3 code-complete gate (against seed/fixtures); real data volume (`[DATA]` items) is a separate ops ramp and never blocks "done" (§39.1).
- **DB connection:** `DATABASE_URL` is a real `postgresql://` string; migrations use the direct connection (`DIRECT_POSTGRES_URL`, port 5432). For Vercel serverless, prefer the Supabase pooled (Supavisor, port 6543) URL for `DATABASE_URL` once available.

---

## 41. Product / Ingredient Hub Pages (Pillar SEO + Monetization)

> Upgrades the "ingredient cost pages" idea (§29.2) into rich **pillar pages** for high-demand products/ingredients (e.g., collagen, ashwagandha, creatine, hyaluronic acid, magnesium). These are the top-of-funnel SEO anchors that capture broad-intent traffic ("collagen", "collagen powder") and funnel it to calculators, RFQs, affiliate links, and ranked manufacturers. One page = one ingredient/product; spun up programmatically + editorially enriched (§27 CMS).

### 41.1 Selection (which ingredients get a hub)
Prioritize by demand signals: high Google search volume/Trends, high Amazon sales rank, our own first-party top-searches (§36), and ingredient-DB coverage (§21.7). Start with a curated set (~25-50), expand as data warrants. Tracked in `product_hub`.

### 41.2 Page anatomy (e.g., `/ingredients/collagen`)
- **Hero / overview:** what it is, primary benefits/uses, quick stats (market size, typical dose).
- **Forms & delivery-method breakdown:** powder, capsules, liposomal, liquid, drinks/RTD, gummies, softgels — each with typical dose, pros/cons, and **why a form may be impractical** (e.g., collagen capsules need ~5-10 g/day → 10+ huge capsules; the **constraints engine §24.9 generates this automatically** from `capsule_capacity`). This "why not capsules" insight is genuinely useful + uniquely ours.
- **Cost + embedded calculator:** the anchor estimator (§24) pre-loaded with this ingredient/preset; live `price_per_kg` curve + tier table + trend from our DB (§21.7).
- **Demand & popularity panel:** Google Trends, related/long-tail search terms, Amazon best-seller rank (BSR) — see §41.4 for data-source feasibility.
- **"Why explore {ingredient}?"** buyer angle (margin, demand, differentiation) + seller/manufacturer angle (capacity utilization, repeat orders).
- **Manufacturers who make it:** filtered, ranked listing (organic, §35) + an optional **paid "Top 5 {ingredient} manufacturers in the Americas"** block (clearly labeled sponsored, §15.4).
- **Raw-ingredient suppliers** in the Americas (from `ingredient_source`, §21.7).
- **Popular finished-good brands** (affiliate links/payouts, §15.6) — labeled as affiliate.
- **FAQ + related ingredients**, internal links to category/geo/cert pages.
- **Schema:** `FAQPage`, `ItemList`/`Product`, `BreadcrumbList`; SSR (§12.1).

### 41.3 Why this works
Captures broad keywords the directory pages can't, then routes traffic three ways: RFQ (lead-gen §15.1), sponsored ranking (§15.4), affiliate (§15.6) — monetizing visitors at every intent level. Differentiated by our cost DB + constraints engine, so it's not thin content.

### 41.4 External demand-data feasibility (so this is buildable, not blocked)
- **Google Trends:** no official API. Use `pytrends` (unofficial, rate-limited, fragile) or a paid provider (Glimpse, DataForSEO); **cache results in `popularity_signal`** and refresh on a schedule. Page renders from cache → deterministic, never blocks on a live call.
- **Amazon BSR / product data:** Amazon **Product Advertising API** requires an active Associates account with qualifying sales; BSR coverage is limited. Practical path: third-party (Keepa, Rainforest API, Jungle Scout) — paid. **Treat as optional, env-gated**; degrade gracefully if no key (hide the panel). Cache in `popularity_signal`.
- **Keyword/search volume:** Google Keyword Planner (needs Ads account) or Ahrefs/Semrush/DataForSEO (paid). Optional; our **first-party search log (§36) is a free, defensible substitute**.
- **Determinism:** all external signals are cached and optional (§39.3). The page is complete with our own data (cost, forms, manufacturers, suppliers); third-party panels are progressive enhancement.

### 41.5 Data model (adds to §21.8)
```sql
create table product_hub (
  id uuid primary key default gen_random_uuid(),
  slug text unique not null,                 -- 'collagen'
  ingredient_master_id uuid references ingredient_master(id),
  title text not null, overview_md text,
  forms jsonb not null default '[]',         -- [{form, typical_dose, pros, cons, feasible}]
  buyer_angle_md text, seller_angle_md text,
  status text not null default 'draft',      -- draft|published
  noindex boolean not null default true,     -- until enriched (§10.3)
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table popularity_signal (
  id bigint generated always as identity primary key,
  product_hub_id uuid references product_hub(id) on delete cascade,
  source text not null,                      -- 'google_trends'|'amazon_bsr'|'keyword_volume'|'first_party'
  metric text not null,                      -- 'trend_index'|'bsr'|'monthly_volume'|'search_count'
  value numeric, payload jsonb default '{}',
  observed_at timestamptz not null default now()
);
create index on popularity_signal (product_hub_id, source, observed_at);

create table affiliate_link (
  id uuid primary key default gen_random_uuid(),
  product_hub_id uuid references product_hub(id) on delete cascade,
  brand text not null, url text not null,    -- includes affiliate tag
  network text,                              -- 'amazon'|'brand'|...
  payout_note text, sort int default 0, enabled boolean not null default true
);
```
- Manufacturer ranking on the hub reuses §35; sponsored "Top 5" reuses `tool_widget`/sponsored-slot config + `admin_audit_log`.

---

## Changelog
- **2026-06-17 (9):** **Pre-GO readiness pass** (so `/goal` runs unattended without stalling). Reconciled §28 DoD into **Code-DoD** (the finite build target, verified against seed sample + fixtures) vs **Data-DoD** (real volume = ops ramp, tagged `[DATA]`, never a build blocker); rewrote the §28.3 gate as code-complete (build stops/reports here) vs public-launch. Added a hard **"never pause mid-build for design"** guardrail (§39.3/§39.4): 4 screens have approved mockups, all others build from `DESIGN.md` directly. Added §38 note that the seed manufacturer sample may be **synthesized deterministically** (`confidence/provenance='seed'`). Added §40 defaults for design coverage, code-complete done-definition, and DB connection (`DATABASE_URL` is real `postgresql://`; prefer Supabase pooled URL on Vercel serverless). Generated `INBOUND_EMAIL_WEBHOOK_SECRET` (local + Vercel). Verified `DATABASE_URL` + `CRON_SECRET` already valid.
- **2026-06-17 (8):** **Homepage pivoted to product-first** via `/design-shotgun` (4 directions → picked clean navy/slate "Trust & Trade", then refined to a category-grid-hero, product-led layout; approved variant A2 saved under `designs/homepage-search-20260617/`). Homepage now leads with **verticals** (Supplements, Beauty/Cosmetics, Food & Bev, Packaging, Personal Care, Pet…) and a **Hot/Trending products** grid that funnels into product/ingredient hub pages (§41) and category pages; manufacturers surface one layer deeper. Added **§7.0 Homepage / Discovery Landing** spec, new routes `/v/[verticalSlug]` (vertical landing) + `/ingredients/[slug]` in the route map (§22.1), Home/Vertical/Product-hub rows in SEO page types (§10.1), and marked the home page template product-first in §30.1 (with approved-mockup reference). DESIGN.md still pending (prereq for `/goal`, §39).
- **2026-06-17 (1):** Initial plan created from ChatGPT brainstorm + Cursor brainstorm session. Added Alibaba-style listing spec, tri-state pricing model, detailed object models, and gaps/suggestions.
- **2026-06-17 (2):** Resolved all §20 decisions. Added Supabase SQL schema (§21), Next.js route map (§22), data sourcing strategy (§23), Pricing Estimation Calculator (§24), AI stock image standard (§25), environment config (§26), admin/automation (§27), and Definition of Done (§28). Raised data volume targets, added SSR no-JS SEO constraint, line-item cost breakdowns, logo/PII scraping rules, domain-as-primary-key, and domain-email claim verification. Created `.env.local`, `.env.example`, `.gitignore`.
- **2026-06-17 (3):** Calculator expanded with **stock/standard + trending formulation presets** (quick mode), **Supplement Facts / cosmetic INCI panel generation**, and a **constraints & safe-limits engine** (capsule/softgel fill capacity, UL/topical caps); added `ingredient_master`, `formulation_template(_ingredient)`, `capsule_capacity` models (§24.10) + SQL (§21.6). Added **certification-document (image/PDF) scraping** to the pipeline + models (§11, §21, §23). Verified the Google service account authenticates but `aiplatform.googleapis.com` was disabled on project `bloom-platform-489223`; used web/LLM search to pull 5 sample supplement manufacturers.
- **2026-06-17 (4):** **Agent Platform API now enabled** — Vertex AI Gemini + Google Search grounding **confirmed working** via the service account (`gemini-2.5-flash`, `us-central1`); documented in §12, §26 (+ `GOOGLE_CLOUD_PROJECT`/`VERTEX_LOCATION`/`VERTEX_MODEL` in env files). Added **extract-maximally principle** (§13). Folded in the cloud-branch ingredient-pricing work (PR #1): **Shopify `/products.json` technique**, confirmed/non-Shopify source-site lists, BulkSupplements dataset (794 products / 4,767 tiers), `scrapers/` + `data/` references (§23.3). Added **ingredient price-observation schema** (`ingredient_source`, `ingredient_price_observation`, §21.7) and the **cost-normalization decision** — preserve full price curve, `price_per_kg` per tier, retail-as-ceiling with adjustable wholesale discount (§24.11). Updated calculation model (§24.3) + DoD. Noted repo reconciliation (merge PR #1; local `docs/PLAN.md`/`.env.local` uncommitted).
- **2026-06-17 (7):** **Name locked: Fabrera** (`fabrera.com`, purchased; Cloudflare DNS). Coined mark chosen over descriptive options (Onshorely/Manufera) for trademark strength + cleaner clearance (no same-class collision; nearest neighbor "Fabera" is a small French entity, different spelling). Updated title, §20.M, §25 watermark, `MediaAsset.brandWatermark`, §26 env rows, and §40 brand defaults to Fabrera / `Fabrera.com`. Set `NEXT_PUBLIC_SITE_NAME=Fabrera`, `NEXT_PUBLIC_SITE_URL=https://fabrera.com` in env files. Repo rename optional/deferred.
- **2026-06-17 (6):** Added **§41 Product/Ingredient Hub Pages** — rich pillar pages for high-demand ingredients (collagen, etc.): forms/delivery breakdown (with constraints-engine "why not capsules" logic), embedded calculator + live price curve, demand panel (Google Trends/Amazon BSR/keyword volume — all cached + optional/env-gated for determinism), ranked manufacturers + sponsored "Top 5" slot, Americas raw-ingredient suppliers, affiliate brand links, FAQ/schema. Added `product_hub`, `popularity_signal`, `affiliate_link` (§41.5). Added **affiliate** as monetization lane #6 + sponsored hub slots to #4 (§15).
- **2026-06-17 (5):** Comprehensiveness + determinism pass. **Expanded admin/ops console** (§27.1) with products, users/roles + impersonation, RFQ/leads oversight, editorial CMS, SEO management (meta/redirects/sitemaps), search/ranking tuning, calculators/widgets admin, feature flags & settings, email-template & notification mgmt, integrations/secrets health, jobs/queues monitor, analytics dashboard, audit log, export/import, legal/compliance. Added new sections: **§29 SEO Tools & Growth Engine** (folded in retired `seo-growth-plan.md` — calculators, programmatic SEO, lead magnets, digital PR, embeddable widgets), **§30 Design System / `DESIGN.md`**, **§31 Testing & QA**, **§32 Infra/CI/CD/Ops**, **§33 Email/Notifications/Deliverability (SPF/DKIM/DMARC)**, **§34 Security/Privacy/Compliance**, **§35 Search & Ranking spec** (weights formula), **§36 Analytics Event Taxonomy**, **§37 Quality Bars** (WCAG 2.1 AA + CWV budgets), **§38 Seed Data/Fixtures**, **§39 Build Execution Contract** (code-complete vs data-complete distinction, ordered milestones M0–M7, determinism guardrails), **§40 Default Decisions Registry** (no-questions-needed defaults). Added **§21.8 operational/admin tables** (feature_flag, site_setting, seo_meta_override, redirect, notification(_preference), email_template, admin_audit_log, lead_magnet, lead_capture, tool_widget, widget_embed). Retired `seo-growth-plan.md` (content absorbed into §29).

