# Fabrera — Design System (`DESIGN.md`)

> Single source of truth for Fabrera's UI. Required prerequisite for the deterministic build (PLAN §39); all feature code builds against these tokens with no ad-hoc colors, spacing, or type.
>
> **Approved direction:** variant **A2** from `/design-shotgun` (2026-06-17) — clean navy/slate "Trust & Trade", **product-first** homepage (PLAN §7.0).
> Mockup: `~/.gstack/projects/jhill247-MadeInAmericas/designs/homepage-search-20260617/APPROVED-homepage.png`

---

## 1. Brand

- **Name / wordmark:** `Fabrera` (set in the display sans, weight 700, tight tracking). Coined from Spanish *fabricar*.
- **Mark:** geometric "F" glyph in brand blue; pairs left of the wordmark. Clear space around the lockup ≥ the cap-height of the "F".
- **Color usage:** navy lockup on light surfaces; white lockup on navy surfaces (top nav, footer). Never recolor the mark outside brand blue / white / navy, never stretch, never add effects.
- **Tagline (working):** "Source any product, made in the Americas."
- **Dark mode:** Phase 1 is **light-only**. Tokens are semantic so a dark theme can be added later without touching feature code.
- **Personality:** trustworthy, credible, modern, clean, data-confident, pan-American/warm. Avoid: cluttered, spammy, neon, generic-SaaS, AliExpress-busy.

---

## 2. Color

Primitive palette (hex) → semantic tokens. Neutrals use the Slate ramp.

### 2.1 Primitives
| Ramp | 50 | 100 | 200 | 300 | 400 | 500 | 600 | 700 | 800 | 900 | 950 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Navy** (brand ink / surfaces) | — | #E7ECF5 | #C5D2E6 | — | — | — | — | #1B3A6B | #122A52 | #0B1E3B | #07142B |
| **Blue** (interactive/accent) | #EFF6FF | #DBEAFE | #BFDBFE | #93C5FD | #60A5FA | #3B82F6 | #2563EB | #1D4ED8 | #1E40AF | #1E3A8A | — |
| **Slate** (neutral) | #F8FAFC | #F1F5F9 | #E2E8F0 | #CBD5E1 | #94A3B8 | #64748B | #475569 | #334155 | #1E293B | #0F172A | #020617 |
| **Emerald** (success/Actual) | #ECFDF5 | #D1FAE5 | — | — | — | #10B981 | #059669 | #047857 | — | — | — |
| **Amber** (warning/Estimated) | #FFFBEB | #FEF3C7 | — | — | — | #F59E0B | #D97706 | #B45309 | — | — | — |
| **Red** (danger) | #FEF2F2 | #FEE2E2 | — | — | — | #EF4444 | #DC2626 | #B91C1C | — | — | — |

> Navy is used mostly at 900/950 for the nav + footer + headings; the mid-navy steps are decorative only.

### 2.2 Semantic tokens (CSS custom properties)
```css
:root {
  /* surfaces */
  --bg:            #F8FAFC; /* slate-50  page background */
  --surface:       #FFFFFF; /* cards, inputs */
  --surface-2:     #F1F5F9; /* slate-100 subtle fills */
  --brand-surface: #0B1E3B; /* navy-900 nav + footer + hero band */
  --border:        #E2E8F0; /* slate-200 hairlines */
  --border-strong: #CBD5E1; /* slate-300 */

  /* text */
  --text:          #0F172A; /* slate-900 headings/body strong */
  --text-muted:    #475569; /* slate-600 body */
  --text-subtle:   #94A3B8; /* slate-400 captions, placeholders */
  --text-on-brand: #FFFFFF; /* text on navy */
  --text-on-primary:#FFFFFF;

  /* interactive */
  --primary:       #2563EB; /* blue-600 CTAs, links, Search */
  --primary-hover: #1D4ED8; /* blue-700 */
  --primary-tint:  #EFF6FF; /* blue-50 selected/hover bg */
  --focus-ring:    #3B82F6; /* blue-500 */

  /* status */
  --success:#059669; --success-bg:#ECFDF5;
  --warning:#D97706; --warning-bg:#FFFBEB;
  --danger:#DC2626;  --danger-bg:#FEF2F2;
}
```

### 2.3 Differentiator color treatments (PLAN §7.7, §8, §9)
- **Price tri-state** (always a dot + label):
  - **Actual** → `--success` dot, label "Actual".
  - **Estimated** → `--warning` dot, label "Estimated" + methodology tooltip.
  - **Unknown** → `--text-subtle` dot, label "Request quote".
- **Verification tiers** (shield/check badge): `Unverified` slate outline (or none) · `Basic` blue outline check · `Verified` blue solid shield-check · `Verified Facility` emerald solid shield-check.
- **Response tiers** (clock chip): `< 2h` emerald · `< 24h` blue · `< 7d` slate · `No data` muted.
- **Sponsored / Affiliate** labels: small uppercase `--text-subtle` pill, never disguised as organic (PLAN §15.4/§15.6).

Contrast: all text/background pairings meet WCAG AA (≥ 4.5:1 body, ≥ 3:1 large/UI). Status colors use the 600/700 step on light fills for legible text.

---

## 3. Typography

- **Sans (UI + body):** `Inter`, with `-apple-system, "Segoe UI", Roboto, sans-serif` fallback. Variable: `--font-sans`.
- **Display (headlines):** `Inter` at weight 700 with tight tracking (`-0.02em`). Optional swap to `Inter Tight` if loaded. Variable: `--font-display`.
- **Mono (data/code only):** `ui-monospace, "Geist Mono", monospace`. Variable: `--font-mono`. Body data (prices, scores, MOQ) uses Inter with `font-variant-numeric: tabular-nums; slashed-zero` rather than full mono.

### 3.1 Type scale (rem, mobile values; scale up at `lg`)
| Token | Size / line-height | Weight | Use |
|---|---|---|---|
| `display-xl` | 3rem / 1.05 | 700 | hero headline (lg+) |
| `display-lg` | 2.25rem / 1.1 | 700 | hero (mobile), section hero |
| `h1` | 1.875rem / 1.15 | 700 | page title |
| `h2` | 1.5rem / 1.2 | 600 | section |
| `h3` | 1.25rem / 1.3 | 600 | card/subsection |
| `h4` | 1.125rem / 1.4 | 600 | small heading |
| `body-lg` | 1.125rem / 1.6 | 400 | lead paragraph |
| `body` | 1rem / 1.6 | 400 | default |
| `body-sm` | 0.875rem / 1.5 | 400 | secondary |
| `caption` | 0.75rem / 1.4 | 500 | labels, meta, badges |
| `overline` | 0.6875rem / 1.3 | 600 | uppercase eyebrows, tracking 0.06em |

Data (prices, scores, tier counts): tabular-nums, weight 500-600.

---

## 4. Spacing, Grid, Radius, Shadow, Motion

- **Spacing scale (4px base):** `1=4 2=8 3=12 4=16 5=20 6=24 8=32 10=40 12=48 16=64 20=80 24=96`.
- **Container:** max-width `1280px` (`max-w-7xl`), centered. Inline padding: `16px` mobile, `24px` `md`, `32px` `lg`.
- **Grid:** 12-column, `24px` gutter. Card grids: 1 col mobile → 2 `sm` → 3 `md` → 4 `lg` (product/manufacturer cards); category tiles 2 → 4 → 6/8.
- **Radius:** `sm 6px`, `md 8px` (default for cards/inputs/buttons), `lg 12px`, `xl 16px`, `full 9999px` (chips/badges/avatars).
- **Borders:** default `1px` `--border`. Cards = hairline border first, shadow second.
- **Shadow:**
  - `xs` `0 1px 2px rgba(15,23,42,.05)`
  - `sm` `0 1px 3px rgba(15,23,42,.08)`
  - `md` `0 4px 12px rgba(15,23,42,.08)` (card hover, dropdowns)
  - `lg` `0 12px 32px rgba(15,23,42,.12)` (modals/popovers)
- **Breakpoints (mobile-first, Tailwind defaults):** `sm 640 · md 768 · lg 1024 · xl 1280 · 2xl 1536`.
- **Z-index:** base 0 · dropdown 1000 · sticky 1100 · header 1200 · drawer 1250 · modal 1300 · popover 1400 · toast 1500.
- **Motion:** durations `fast 150ms · base 200ms · slow 300ms`; easing `cubic-bezier(0.4,0,0.2,1)`. Honor `prefers-reduced-motion: reduce` (disable non-essential transitions).
- **Icons:** `lucide-react`, `1.5px` stroke, `20px` default (`16px` in chips, `24px` in tiles).

---

## 5. Component Inventory (+ required states)

> Single source in `components/ui/`. Every component documents: `default · hover · focus-visible · active · disabled · loading · empty · error` where applicable. Built on Radix primitives / shadcn-style for a11y.

**Primitives**
- **Button** — variants `primary` (blue), `secondary` (slate outline on white), `ghost`, `destructive`, `link`; sizes `sm/md/lg`; states incl. `loading` (spinner + disabled) and `disabled`.
- **Input / Textarea** — label, hint, error text, prefix/suffix icon; states `focus` (blue ring), `error` (red border+message), `disabled`.
- **Select / Combobox** — searchable; keyboard nav; empty + loading states.
- **Checkbox / Radio / Switch** — grouped; indeterminate for checkbox.
- **Label / FormField / FieldError** — wraps controls; ties `aria-describedby`.

**Search & faceting (homepage + /search)**
- **SearchBar (NL)** — large input + Search button (blue); inline filter chips: Category, Country/State, Certification, MOQ. Loading + no-results states.
- **FilterChip / FacetGroup** — toggle/selected (`--primary-tint` bg), count badge, clear-all.
- **FilterDrawer** — mobile-only off-canvas facets (`drawer` z-index), 44px targets, apply/clear footer.

**Trust & data (the moat)**
- **VerificationBadge** — tiered (§2.3); tooltip explains the level.
- **ResponseScoreChip** — clock icon + tier label + median time; "No data" muted state.
- **PriceIndicator** — tri-state dot+label (§2.3); Estimated opens a methodology tooltip; Unknown renders a "Request quote" link.
- **CompletenessMeter** — small % bar for listing completeness (PLAN §8.2).
- **SponsoredLabel / AffiliateDisclosure** — uppercase pills (§2.3).

**Content cards**
- **ProductCard** — thumbnail (with logo/AI-stock fallback), product/ingredient name, category tag, `PriceIndicator`, "from N verified makers". Links to product-hub/category. *Primary homepage unit.*
- **ManufacturerCard** — logo (fallback), name (truncate w/ tooltip for long names), location, `VerificationBadge`, `ResponseScoreChip`, category tags, `PriceIndicator`.
- **CategoryTile** — icon, vertical name, product/listing count; hover lift (`shadow-md`).
- **EntryTile** — Cost Estimator / Browse-by-Country, icon + copy + arrow.

**Detail & comparison (listings, hubs)**
- **Table** — spec table + tiered pricing table; sticky header; zebra optional; tabular-nums.
- **PricingTierTable** — qty break → unit price → lead time.
- **SpecAttributeList** — key/value grid.
- **Gallery** — product/facility images, thumbnail strip, lightbox.
- **ComparisonTable** — manufacturer × attribute matrix (PLAN §10).
- **CalculatorWidget** — inputs (progressive) + live line-item breakdown + estimate range (PLAN §24). Loading/elevated states.
- **SupplementFactsPanel / INCIPanel** — generated facts/ingredient panel (PLAN §24.8).

**Navigation & feedback**
- **TopNav** — navy bg, white wordmark left, links (Browse Products / Categories / Cost Estimator / For Manufacturers), Sign in (outline-on-navy). Sticky (`header` z). Mobile: hamburger → drawer.
- **Footer** — navy; product-category + country + resources + company link columns; newsletter capture (PLAN §10 internal-linking surface).
- **Breadcrumb** — for deep hierarchy (category/geo/hub).
- **Tabs · Accordion (FAQ) · Dialog/Modal · Tooltip · Toast · Pagination · Banner/Alert**.
- **Avatar / LogoFallback** — initials/monogram tile when a manufacturer logo is missing (AI-stock fallback per PLAN §25).

**System states**
- **Skeleton** — for cards, tables, search results.
- **EmptyState** — zero search results (with suggestions + clear filters), empty dashboard.
- **ErrorState** — inline + full-page (with retry).

---

## 6. Page Templates

Built from the components above; see PLAN §22 routes and §30.1.

1. **Home (product-first)** — TopNav · search hero (navy band, map motif) · **category grid** (verticals + counts) · trust strip · **Hot/Trending products** grid (`ProductCard`) · Cost Estimator + Browse-by-Country `EntryTile`s · SEO Footer. *Matches APPROVED A2.*
2. **Vertical / department landing** (`/v/[verticalSlug]`) — vertical hero · sub-category grid · trending products · top manufacturers (ranked) · SEO copy.
3. **Product / ingredient hub** (`/ingredients/[slug]`, PLAN §41) — overview · forms breakdown · embedded calculator · demand panel · ranked manufacturers (+ sponsored Top 5) · raw-ingredient suppliers · affiliate brands · FAQ.
4. **Search / results** (`/search`) — sticky facets (desktop) / `FilterDrawer` (mobile) · result list of `ManufacturerCard`/`ProductCard` · sort · pagination · `EmptyState`.
5. **Manufacturer profile** (`/m/[slug]`) — header (name, `VerificationBadge`, `ResponseScoreChip`) · capabilities/certs · product listings · contact CTA (RFQ).
6. **Product listing** (`/m/[slug]/p/[productSlug]`) — Alibaba-style (PLAN §8): gallery · pricing block (tri-state) · variations · specs · MOQ/lead-time · samples · certs · FAQ · related · "Request Quote" CTA.
7. **Category / Geo / Cert / Capability** — heading + intro copy · ranked results · facets · internal links.
8. **Ranking / Comparison** — `ComparisonTable` / ranked list (response-data powered).
9. **Cost guide** — editorial + `CalculatorWidget` + benchmark data.
10. **Calculator** (`/calculator`) — full `CalculatorWidget`, quick + custom modes, line-item breakdown.
11. **Dashboards** — buyer (sourcing CRM: saved, projects, RFQs, inbox) and manufacturer (listings, leads, analytics).
12. **Admin** (`/admin/*`) — dense tables, queues, editors (PLAN §27); utilitarian, same tokens, higher density.

---

## 7. Accessibility (target WCAG 2.1 AA — PLAN §37)

- Semantic HTML (`header/nav/main/section/footer`, real `button`/`a`); one `h1` per page; logical heading order.
- Visible focus: `2px` `--focus-ring` outline + offset on all interactive elements; never remove focus styles.
- Color is never the only signal: tri-state price, verification, and response tiers always pair color with an icon + text label.
- Touch targets ≥ `44px`; spacing prevents mis-taps on mobile filters.
- All images have alt text (incl. AI stock + logo fallbacks); decorative images `alt=""`.
- Forms: programmatic labels, `aria-describedby` for hints/errors, errors announced.
- Contrast meets AA; verified with axe in CI (PLAN §31).
- Respect `prefers-reduced-motion`.

---

## 8. Content & Tone

- Plain, confident, data-forward. Lead with what the user gets. No hype, no happy-talk, no filler.
- Scannable: short headings, bulleted specs, highlighted key terms (billboard, not brochure).
- Numbers are specific and sourced ("Median response under 24h", "from 18 verified makers"). Estimates are always labeled and explained.
- Sentence case for UI labels and headings; Title Case only for the wordmark and proper nouns.
- Trust language is precise, never overpromised (e.g., "Verified facility" only when actually validated).

---

## 9. Implementation

- **Stack:** Next.js (App Router) + React + **Tailwind CSS**. Tokens above map to `tailwind.config.ts` theme (`colors`, `fontFamily`, `fontSize`, `borderRadius`, `boxShadow`, `screens`) and CSS variables in `app/globals.css`.
- **Primitives:** Radix UI / shadcn-style components in `components/ui/` as the single source. No ad-hoc colors, spacing, or font sizes in feature code — only tokens.
- **Fonts:** `next/font` for Inter (and Inter Tight / Geist Mono if used); preloaded, `display: swap`.
- **Icons:** `lucide-react`.
- **States required:** every component ships documented `loading / empty / error / disabled` states (PLAN §30.2). No screen without skeleton + empty + error coverage.
- **SSR/SEO:** content pages render server-side with minimal client JS (PLAN §12.1, §37); interactive widgets (search, calculator, filters) hydrate as islands.
- **Theming:** semantic tokens enable a future dark theme; Phase 1 ships light-only.

---

## Changelog
- **2026-06-17:** Initial `DESIGN.md` derived from approved `/design-shotgun` variant **A2** (clean navy/slate "Trust & Trade", product-first homepage). Defines brand, color (primitives + semantic tokens + tri-state/verification/response treatments), typography, spacing/grid/radius/shadow/motion, component inventory with states, page templates, accessibility (WCAG 2.1 AA), content tone, and implementation (Tailwind tokens + Radix/shadcn).
