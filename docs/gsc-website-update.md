# Google Search Console website update

Status: Approved by Mallory on October 15, 2026 (Pacific), including the reconstructed visual and page edits.
Date: October 15, 2026 (Pacific).

## Task and source

Help prospective merchants understand optional product-page search-query guidance and the connection between selecting phrases and editing a draft. Preserve the existing website design and broader product positioning.

Current website sources: index.html, product.html, pricing.html, use-cases.html, compare.html, support.html, buyer pages, and existing article templates. Approved imagery: penstack_logo.png, penstack-product-hero-liquid-snowboard.webp, and assets/illustrations/penstack-illustration-search-intent-v1.webp.

App behavior source: modom1123/penstack-app, src/components/GscQueries.tsx and docs/gsc-integration.md, retrieved from main October 15. Implemented behavior includes optional per-store read-only access, a matching property, exact public-product-page query guidance, clicks and impressions, up to five selected phrases before Generate Description, and empty/limited/reconnect states. Documentation specifies availability across plans. Live paid-store validation remains pending Shopify approval.

## Applicable design guide

Follow docs/penstack-design-system.md sections 4–6 (type, layout and components), 8–9 (actions and links), 18–19 (imagery and Home/Product), 20–24 (buyer pages, pricing/comparison, articles, help and claims), and 25–26 (frontend verification and review).

## Approved changes

- Home: a compact optional-GSC benefit section; preserve the hero.
- Product: replace generic search-context example with a concrete query-to-draft demonstration. Preserve existing Shopify before/after evidence.
- Pricing: name query guidance across plans within existing publishing allowances.
- Use Cases and buyer pages: connect existing listing-refresh/store-context tasks to optional GSC guidance.
- Compare: clarify Penstack’s own capability without making new competitor capability claims.
- Support: connection, property, empty-data, metrics, selected-phrase processing, and disconnect answers.
- Learning hub: setup/use guide plus contextual links from three existing SEO/listing articles.
- Sitemap and modified article dates: reflect changed pages and the added guide.

## Demo provenance and claims

The original conversation mockup was not recovered. The proposed visual is a native HTML reconstruction grounded in the implemented GSC component, with an adjacent editorial draft panel. It is not a pixel-exact app screenshot. All query rows, counts, dates, and draft copy are illustrative; labels disclose sample data. The product image and existing product name are reused. No real connected account, live query result, traffic improvement, reporting feature, experiment, or A/B testing result is asserted.

The UI is a static demonstration, not functional checkboxes or an active connection. Text is selectable and responsive. DM Sans files are self-hosted for the new feature sections, with license retained and a scoped font-family alias; fallbacks are DM Sans, Arial, sans-serif. Existing typography/layout is otherwise preserved.

## Review evidence

See docs/previews/gsc for full desktop/mobile page renders, GSC section closeups, baseline Home/Product renders, and validation.json. The JSON records viewport reflow, font loading, image loading, and link checks. Review the images before production publication.

Mallory approved these edits on October 15, 2026 (Pacific): “I'm good with these edits.” Production publication and live verification are authorized. The original app paid-store validation remains separate and pending Shopify approval.
