# Penstack standards: mandatory execution contract

Read `docs/penstack-design-system.md` before any applicable design, frontend, product, marketing, copy, image, or artifact work. The user's current instructions take precedence. Preserve existing framework and repository instructions.

## Source of truth and scope
- Inspect the current repository implementation, approved assets, and relevant design rules before creating or editing.
- Preserve accepted elements and change only the authorized scope. Reuse existing components and asset files.
- Keep Current, Established, Proposed, and Pending decisions distinct. Do not treat a proposal as approved.
- Website rules are website scope. Apply shared brand rules to the app, but verify app behavior separately. App Generate / Penstack-native actions use navy; Publish to Shopify uses green.
- Mallory owns approval of new design decisions. The executing agent owns implementation and verification.

## Every visual must be Penstack-branded and font-safe
- Use the approved lowercase wordmark, Penstack P, pen, sneaker, shirt, palette, and appropriate source assets. Never invent substitute logos or silently use a different illustration style.
- Use the approved DM Sans typography with correctly loaded or embedded fonts. Web output must include reliable fallbacks such as `"DM Sans", Arial, sans-serif`. Fallbacks protect rendering; they do not authorize changing the brand typography.
- Render and inspect the delivered visual. Verify complete artwork, intrinsic image proportions, text legibility, contrast, clipping, overflow, and relevant desktop/mobile layouts.
- Missing assets or font access must be disclosed before presenting a substitute. Do not label an unverified visual fully branded or finished.

## No image without context
- Every visual presented to the user needs an adjacent caption or explanation: what it shows, why it matters, and its Current / Proposed / Approved status.
- Identify the affected page or component. Explain what changed when presenting a revision.
- Add meaningful alt text where applicable. Decorative interface assets may have empty alt text; the surrounding page supplies their context.
- Distinguish editorial illustrations, functional UI icons, photographs, and actual product evidence.

## Preview before download or publication
- Show a rendered preview directly in the conversation before download links.
- Show enough of the artifact to review the whole result, plus readable closeups when necessary. Never make the user download a file just to understand what was created.
- For a new visual direction or unresolved design decision, obtain the user's approval before publication. An existing explicit approval remains valid; do not repeatedly request it.
- Routine fixes within approved scope can proceed after a contextual preview without adding a redundant permission loop.

## Complete execution
- Complete all authorized implementation, conversions, resizing, naming, repository/file updates, appropriate checks, and delivery yourself unless the user explicitly assigns an action elsewhere.
- Do not substitute instructions or snippets for work you can perform. Do not ask the user to upload, paste, or run a command you can execute.
- Continue through reversible necessary steps. If access truly blocks an action, identify the exact action, blocker, work already completed, and minimum missing access or input.
- Never claim that a commit, deployment, test, approval, or file save occurred without verifying its result.

## Required workflow and evidence
1. Identify the requested change and applicable guide sections.
2. Inspect current source and approved assets.
3. Build the scoped change and present a contextual preview.
4. Verify the rendered result and relevant behavior; run checks appropriate to the change.
5. Complete the authorized repository/publication/file steps and verify their outcome.
6. Report the result, guide sections used, preview, validation, and any actual unresolved issue.
7. Update the standards when an explicitly approved change establishes a new rule. Keep full specifications and decision status intact.

This file is persistent project instruction, not an automated guarantee of compliance. Human review and rendered evidence remain required.


---

# Supporting design-system reference

The following text is the source-grounded website reference. Website-specific geometry does not automatically become app approval. Visual examples remain in the companion illustrated guide; the repository copy retains the written rules.

# Penstack website design system and team direction

**Owner:** Mallory Odom  
**Working edition:** October 9, 2026 (Pacific)  
**Applies to:** Product Design, Frontend and Marketing  
**Status:** Source-grounded working guide. Website-wide proposals require review.

## 1. One website. A shared system.

Penstack website design system and team direction | Working edition | October 9, 2026 (Pacific)

**Purpose:** Give Product Design, Frontend, and Marketing a common set of rules for the marketing website. Preserve recognizable Penstack elements while making each page clearer, more compact, and easier to use.

| Layer | What belongs here |
| --- | --- |
| Foundations | Logo, font, color, spacing, geometry and accessibility. |
| Components | Navigation, buttons, cards, proof panels, tables, filters and CTA. |
| Page patterns | A distinct reader question, content sequence and evidence for each page. |
| Governance | Source references, approval status, review evidence and recorded exceptions. |

### Scope and status

Covers Home, Product, Use Cases, Compare, Pricing, About, Blog/library, article templates, buyer landing pages, Support, Privacy and Terms. The app is a connected destination; its dashboards and onboarding require a separate product system.

| Label | Meaning |
| --- | --- |
| Current | Observed in retrieved HTML/CSS or existing asset bytes. |
| Established direction | Explicit decisions from this working session. |
| Proposed | Website-wide guidance requiring review before implementation. |
| Pending | An unresolved reference, exception or final composition. |

This guide is an expansion of the About direction. It documents standards and proposed adoption work. It does not mean that every page has been migrated or that all live pages have passed visual QA.

Source basis: live HTML/CSS and selected assets retrieved October 9 Pacific / October 10 UTC. Document diagrams are specifications, not screenshots of a deployed redesign.


## 2. Identity: logo, P and pen

The actual Penstack identity assets, shown together as first-class brand elements.

### Three assets with different jobs

| Asset | Role | Source |
| --- | --- | --- |
| Full logo | Primary signature for website headers and identifying the brand. | penstack_logo(4).png; byte-identical to live penstack_logo.png. |
| Penstack P | Compact recognition when the full name does not fit. | penstack 512x512(1).png; actual image is 244 x 512px. |
| Penstack pen | Standalone identity symbol for applicable brand/icon contexts. | Colorful Minimal Pen App Icon.png; 1254 x 1254px. |

Keep the lowercase wordmark, pen construction, colors and proportions intact. Reuse these source assets rather than redrawing the P, substituting a generic pen or typing the logo in a font.

### Reference status and file quality

The full logo is verified against the current website. The P and pen were retrieved from the existing asset collection. Their placement rules below are proposed system guidance, not evidence that every website context already uses them.

The pen source includes a rounded tile outline, shading and visible edge effects. Preserve this reference in the guide. Before a production export, review edge quality and the desired background treatment against the intended size. Do not silently redraw or remove features.

Source copies are included unchanged in the editable bundle under brand-assets/. The asset filename alone does not establish its pixel size, transparency quality or approval status.


## 3. Identity: placement and handling

Proposed usage rules for Design, Frontend and Marketing, grounded in the existing assets.

| Context | Use | Handling |
| --- | --- | --- |
| Website header | Full logo | Keep proportions. Shared sizing: 180px desktop / 160px on smaller screens. |
| Compact brand context | Penstack P | Use when the wordmark does not fit. Show the complete pen and letter. |
| Standalone brand symbol | Penstack pen | Use the actual reference for brand contexts; avoid generic feature-icon use. |
| Document / team guide | Full logo + reference gallery | Identify the brand prominently. Include all three in the identity reference. |
| Dark footer / dark surface | Reviewed inverse treatment | Review the inverse treatment. Use an approved variant or a deliberate white container. |

### Clear space and size

Proposed clear space: at least one pen-body width around visible artwork. Transparent file padding does not define clear space. Validate readability at actual size before setting a minimum for the P or pen.

### Use and avoid

- Show the complete cap and tip. Preserve proportions with intrinsic sizing and contain behavior. Do not stretch, rotate, recolor, crop or rebuild the marks.

- Do not add glow, outlines, tile shapes or shadows. Changes to existing source effects require a separately reviewed asset edit.

- Decorative marks use empty alt text. Linked logos need an accessible Penstack/home name. Avoid duplicate adjacent naming.

### Handoff contract

Record source/version, backgrounds, size, export quality, accessible name and approval. Retain masters. Use the same identity references across site and campaign materials.


## 4. Foundations: color and type

Current shared tokens come from brand.css. Use semantic roles rather than choosing a new color for each page.

| Role / token | Current value | Rule |
| --- | --- | --- |
| Primary ink / --navy | #1b2a4a | Headings and primary hierarchy |
| Supporting text / --muted | #526078 | Readable body context |
| Brand green / --green | #1a5c3a | Primary site action and links |
| Yellow / --yellow | #f0a500 | Accent; navy text on yellow |
| Orange / --orange | #c94b2a | Editorial accent / small labels |
| Red / --red | #c92f1e | Existing About labels |
| Border / --line | #d8dee8 | Grouping and structural edges |
| Canvas / --white | #ffffff | Primary page surface |

| Type token | Current shared scale | Use |
| --- | --- | --- |
| --type-display | 48-76px (fluid) | Hero H1 |
| --type-section | 36-56px (fluid) | Major section H2 |
| --type-subsection | 24-32px (fluid) | Subsections / plan headings |
| --type-card | 20px | Card heading |
| --type-body / --type-lead | 16px / 18px | Body / introductory copy |
| --type-label / --type-meta | 14px / 12px | Navigation / secondary labels |

**Font:** DM Sans. Use the real font in designs and implementation. Preserve text as selectable text. Shared line heights: display 1.02, section 1.10, subsection 1.20, body 1.60.

**Exceptions:** The About proposal uses 38-42px supporting headings and 17px body copy. Home has an Inter-first font stack in local CSS. These are explicit differences to resolve; the About values are not universal shared tokens.

Accent colors are not automatically suitable for small text. Verify the actual foreground/background pairing, including hover, focus and CTA reassurance text.


## 5. Layout: compact, intentional sections

Proposed website-wide grouping rule: white canvas, meaningful panels and height determined by content.

| Geometry | Current shared token | Application |
| --- | --- | --- |
| Control radius | 10px | Buttons and form controls |
| Card / panel radius | 16px / 20px | Cards / grouped sections |
| Hero / section vertical | 68px / 72px | Current general defaults |
| Compact section vertical | 48px | Current compact desktop default |
| Card padding | 24px / 20px compact | Avoid shrinking text to fit |
| Grid / split gap | 18px / 48px | Card rows / two-column compositions |

Current mobile section rules are 56px standard and 40px compact at 760px. The approved About exception remains 48px desktop / 32px mobile, with a 40px desktop split gap.

### A grouping rule, not a box around every paragraph

- Use a light outline to group a story, related proof, or a decision. Let ordinary sections remain open. Avoid page-spanning divider lines; retain necessary table rows and control separators.

- Colored top accents follow rounded corners. Use full color accents. Keep card interiors white or navy where the pairing has been reviewed.

- Do not force equal pixel heights across unrelated sections. Row cards may stretch together. Images retain the complete intended scene.

### Responsive contract

Proposed content frame: max 1180px with 24px desktop / 16px mobile gutters. This is a consolidation target, not the current width of every page. Stack before content becomes cramped. Preserve a useful reading order; do not move copy visually while leaving a conflicting DOM order.


## 6. Components: reuse meaning and behavior

The same component should mean the same thing wherever a visitor encounters it.

| Component | Required behavior |
| --- | --- |
| Header + footer | Same destinations, active page, logo proportions and accessible navigation. Retain working mobile navigation during consolidation. |
| Primary site CTA | Start free uses the existing app destination. Green/white on a white surface; yellow/navy in the existing green closing band. |
| Secondary action | A useful Product, Pricing or guide destination. Visible hierarchy below the main action. |
| Story / proof panel | Heading, concrete evidence, explanation and an optional relevant link. Content determines height. |
| Card grid | Consistent interior spacing, full scene images and readable text. Distinguish clickable cards from static content. |
| Closing CTA | One useful next step plus accurate reassurance. Keep the action visible without repeating the whole page. |

### States are part of the specification

Document default, hover, keyboard focus, active/selected, expanded/collapsed and unavailable states where applicable. A disabled/loading state is only needed for an action that actually performs work; do not invent a spinner for a normal link.

Current shared focus outline is 3px navy with a 3px offset. Dark closing bands and footers use a yellow focus treatment. Check that outlines remain visible and are not clipped.

The examples below are component specifications based on current tokens. They are not screenshots. Website CTA colors do not redefine the app’s Generate / Publish action semantics.


## 7. Component lookup: choose by purpose

Start with the decision you need to make, then consult the visual guide.

| Question | Guide | Page |
| --- | --- | --- |
| What color and emphasis should this action use? | Buttons: intent and states | 8 |
| Is this a link, button, tab or navigation item? | Links and navigation | 9 |
| Do these sections need a divider, panel or whitespace? | Section separation and grouping | 10 |
| Is this success, warning, error, information or pending? | Status and feedback | 11 |
| Which text style fits this content? | Typography and hierarchy | 12 |
| Should I use a brand mark or a functional icon? | Icons and brand marks | 13 |
| How should comparison information be structured? | Tables and comparisons | 14 |
| How should selection and empty results behave? | Filters and selection controls | 15 |
| What changes on a narrow screen? | Responsive component behavior | 16 |
| What about forms, dialogs, notifications or tooltips? | App components: scoped proposals | 17 |
| Should this be artwork, photography or a screenshot? | Imagery: purposeful formats | 18 |

### The contract for every component guide

Choose this when: purpose and decision rule. Visual examples: variants and states. Specifications: shared tokens, spacing and typography. Use / avoid: visible mistakes and alternatives. Accessibility and mobile: required behavior. Status / source: established rule versus proposal.

The current website uses multiple implementations. Component examples in this edition are specifications. New semantic conventions and app state treatments are proposed unless explicitly described as established direction.

### Do not use color as the only decision

First identify the action or information. Then choose hierarchy, wording and behavior. A component may share a color with another component without sharing its meaning; the label and context must stay clear.

## 8. Buttons: intent and states

Choose the action’s purpose first. Keep website and app rules explicitly scoped.

| Intent / scope | Treatment | Status |
| --- | --- | --- |
| Website: primary action on white | Green background / white label | Current site pattern |
| Website: primary action in green closing band | Yellow background / navy label | Current site pattern |
| App: Generate / Penstack-native action | Navy background / white label | Established; verify app tokens |
| App: Publish to Shopify | Green background / white label | Established; verify app tokens |
| Secondary / cancel | White surface / navy label and outline | Current secondary; cancel proposed |
| Destructive / delete | Red label / outline; confirm consequential deletion | Proposed |

### Specifications and states

Website baseline: 10px control radius, 16px label, 1.5 line height, 14px vertical / 22px horizontal padding. Primary hover: #14482d; yellow closing CTA hover: #ffba2a. Keyboard focus: 3px contrasting outline with 3px offset. Proposed practical target: at least 44px control height.

Loading preserves intent color, stable width and an action-specific label such as “Generating…”. Prevent duplicate submission and announce progress. Disabled means unavailable; use a readable neutral treatment and explain the dependency nearby. Do not show unavailable controls as active.

### Use / avoid

Use one dominant action per decision group. Keep “Publish to Shopify” explicit. Avoid choosing green merely because a feature is new, using warning yellow for unrelated actions, or making cancel as prominent as confirm. On mobile, wrap groups without reversing reading order.

State examples below are proposed variants. Website tokens shown: navy #1b2a4a, green #1a5c3a, yellow #f0a500, red #c92f1e. This does not certify current app CSS.


## 9. Links and navigation

Use links to go somewhere. Use buttons to change a state or perform an action.

| Need | Choose | Required cue |
| --- | --- | --- |
| Visit Product, Pricing or an article | Text link or CTA-styled anchor | Useful destination label; real href |
| Switch visible content in place | Tab or filter button | Selected state and correct keyboard behavior |
| Jump within a long page | Anchor / contents link | Meaningful section label and stable target |
| Change a setting, submit or expand | Button | Action label; state and feedback |
| Show current page | Navigation item | Visible active treatment and aria-current |

### Specifications

Current shared navigation: 14px. Inline links remain visually distinguishable; proposed default is underlined text in green, with a visible focus ring. Do not rely on hover to reveal that text is interactive. Preserve header destinations and logo/home accessible naming.

### Use / avoid

Use “Read the alt text guide” rather than several indistinguishable “Learn more” links. Avoid clickable-looking static labels. A whole clickable card has one clear destination; do not nest competing links inside the same anchor. External-link indicators only belong where they communicate a meaningful change of context.

### Accessibility and mobile

Tab order follows the reading order. Every destination remains reachable on narrow screens. Preserve existing horizontal header navigation during consolidation. Tabs and filter chips are different controls; do not give a filter a tab role solely for its appearance.

Source: current header/navigation and shared focus styles. Inline-link conventions and detailed interaction rules are proposed consolidation guidance.


## 10. Section separation and grouping

Whitespace separates ideas. Outlined panels group related content. Internal separators clarify structure.

| Situation | Treatment | Purpose |
| --- | --- | --- |
| Ordinary change of section | Whitespace on the white canvas | Separate ideas without extra decoration |
| Related story, proof or decision | Light outlined panel | Make a meaningful group visible |
| Parallel principles or feature cards | Outlined cards; optional approved color accents | Show peers and restrained emphasis |
| Rows in a table or items in a control | Internal separators where useful | Preserve scanability and relationships |
| Page-spanning section boundary | Avoid a horizontal divider line | Use spacing or an intentional group instead |

### Specifications

Outline: 1px --line (#d8dee8). Card radius: 16px; panel radius: 20px. Use 20-24px card padding; reviewed larger panels may use 24-32px. Colored card accents follow the curved top corners. Keep interiors white or a reviewed navy treatment. Ordinary sections do not all need a box.

### Use / avoid

Use one panel around a coherent story or proof pair. Avoid boxing every paragraph, stacking borders inside borders or adding lines to fill empty space. The no-section-divider rule does not remove necessary table gridlines, control separators or navigation structure.

### Responsive and acceptance

Panels and cards grow with real content. Stack peers when cramped. Preserve grouping without fixed section heights. Compare the full desktop and mobile page: separation should be clear without a succession of oversized boxes.

Established direction: use meaningful boxes instead of full-width section dividers. Existing shared CSS still contains divider rules; this document does not claim those have all been removed.


## 11. Status and feedback

Identify the meaning in words. Color and an icon reinforce it.

| Meaning | Proposed visual role | Example |
| --- | --- | --- |
| Success | Green accent + success label | Published to Shopify |
| Warning / review needed | Yellow accent + navy text | Review this claim before publishing |
| Error / blocked task | Red accent + specific error label | Could not connect this store |
| Information | Navy accent + information label | Your allowance is shared across stores |
| Pending / in progress | Muted accent + progress wording | Publishing… |

### Specifications

Proposed semantic message surface: white, 1px shared border, 16px radius, 16-20px padding. Use a short title and useful next action where possible. Do not fill the entire page with a status color. A yellow warning always uses navy text. Failure wording explains what happened and what the user can do.

### Use / avoid

Show success after the operation actually succeeds. Keep persistent problems visible until resolved. Use a temporary notification for brief confirmation; use an inline message for a field-specific problem. Avoid color-only dots, generic “Something went wrong” messages and disappearing critical errors.

### Accessibility and mobile

Announce meaningful asynchronous status changes without moving focus unnecessarily. Reserve assertive alerts for urgent interruption. Keep message text and recovery controls visible at narrow widths. Do not imply a visual green state proves a backend operation succeeded.

These semantic status mappings are proposed. The website palette is established; current app status components have not been audited in this guide.


## 12. Typography: choose the hierarchy

Choose a role based on the content’s job, not how much empty space is available.

| Role | Shared specification | Choose this when |
| --- | --- | --- |
| H1 / display | 48-76px fluid, leading 1.02 | The one primary page message |
| H2 / section | 36-56px fluid, leading 1.10 | A major new idea or page section |
| H3 / subsection | 24-32px fluid, leading 1.20 | A subdivision or plan heading |
| Card heading | 20px, leading about 1.30 | A concise peer item |
| Body / lead | 16px / 18px, leading 1.60 | Explanation / short introduction |
| Label / caption | 14px / 12px | Secondary context, never essential body copy |

### Use / avoid

Keep long explanations in body copy. Labels remain subordinate to headings. Do not use a huge H2 to disguise a paragraph, shrink important reassurance text to fit, or replace actual text with generated lettering. Use the actual DM Sans font.

### Exceptions and mobile

About has its approved smaller supporting heading direction and proposed 17px body. Articles need a readable prose hierarchy; do not blindly apply marketing heading sizes to every article subsection. Remove forced line breaks when they create awkward narrow-screen wrapping.

### Accessibility

Heading levels describe structure independently of visual size. Maintain sufficient contrast and support text resizing. The typography table is a token reference, not an instruction to change existing approved page copy.

Source: brand.css and the About companion. Article measure and page-specific consolidation remain proposals.


## 13. Icons: function and identity have different jobs

A functional icon explains an action or state. A brand mark identifies Penstack.

| Need | Choose | Rule |
| --- | --- | --- |
| Identify the brand | Full logo, P or pen | Use the identity reference and exact source asset |
| Explain an action | Functional icon plus label | Use recognizable meaning; preserve an accessible name |
| Show a status | Status icon plus wording | Pair with the feedback guide; do not rely on color |
| Set the editorial tone | Approved illustration | Use the imagery guide and existing references |
| Decorate without information | Optional decorative accent | Keep subordinate; omit if it adds no useful value |

### Specifications

Current shared .brand-icon is 24 x 24px. Existing icon tiles are 44 x 44px with a 12px radius. Proposed functional family: consistent navy treatment, line weight and optical size. Reuse existing functional assets before adding another style. Do not recreate the P or pen as interface glyphs.

### Use / avoid

Use icon + text for unfamiliar or consequential actions. Avoid an unexplained pen icon as a universal “edit” command when it is also a brand symbol. Use an ordinary functional edit icon instead. Do not mix emoji, filled symbols and line icons arbitrarily.

### Accessibility and mobile

Decorative icons are hidden from assistive technology. Icon-only controls need a meaningful accessible label and a practical target size. Tooltips can clarify; they cannot supply the only accessible name.

Source: illustrations.css and the actual logo/P/pen assets. Functional-family consolidation is proposed.


## 14. Tables: comparisons remain understandable

Use a table when row and column relationships are the information.

| Visual choice | Choose this when | Rule |
| --- | --- | --- |
| Neutral row/column structure | Plan or feature comparison | Use captions and real headers |
| Recommendation emphasis | A documented reader-specific fit | Use text explaining the reason; avoid implying universal superiority |
| Supported / limited / unavailable | Capability or plan status | Use explicit wording plus optional icon |
| Internal gridline | Rows or columns need distinction | Retain it; this is not a section divider |
| Narrow-screen scroll region | Two-dimensional structure needs space | Provide a visible cue and keyboard access |

### Specifications

Use a white surface, shared border and 16-20px outer radius. Start with the existing table spacing and validate real content. Keep row labels readable. Show currency, billing period and allowance unit in text. Use navy on yellow emphasis.

### Use / avoid

Use “Limited” with an explanation rather than an ambiguous dot. Do not turn every missing capability into a red error. Do not hide key plan differences to make the table narrower. Comparison claims need sources and review dates.

### Accessibility and mobile

Associate cells with row/column headers. Keep the complete comparison available when scrolling. Do not claim a responsive transformation preserves meaning until it has been checked with the actual content.

Source: current Pricing/Compare structures. Semantic labels and narrow-screen behavior must be verified during implementation.


## 15. Filters: make selection and recovery visible

Use filters to narrow results. Use tabs only when switching a defined content view.

| State | Treatment | Behavior |
| --- | --- | --- |
| Unselected | White, navy label, shared outline | Available option |
| Selected | Navy background / white label | Expose selection programmatically |
| Expanded / collapsed | Label + directional cue | Expose expanded state |
| Empty results | Plain explanation + recovery | Clear filters or choose another option |
| Unavailable | Readable neutral treatment | Explain why it cannot be chosen |

### Specifications

Keep level and topic labels distinct. Current learning filters use navy/white for active or selected state. Proposed chip geometry: shared 10px control radius and a practical target size; do not copy a badge’s tiny dimensions into an interactive control.

### Use / avoid

Keep the selected option visible in text. Avoid a color-only selection, unexplained counts or an empty blank region. Counts must reflect the actual result set. Add clear/reset behavior only where there is a filter to reset.

### Accessibility and mobile

Use buttons with pressed state for toggle filters where appropriate. Use actual radio/checkbox semantics for exclusive/multiple selection. Apply a tab pattern only when its behavior is implemented. Wrap controls without hiding the current selection; maintain keyboard focus after results update.

Source: blog hub filters and brand.css. Detailed state semantics and recovery patterns are proposed pending implementation review.


## 16. Responsive: specify what changes

A smaller screen changes the composition, not the information a reader needs.

| Component | Narrow-screen contract |
| --- | --- |
| Story / proof panels | Stack before either column becomes cramped; meaningful copy order first. |
| Card grids | Reduce columns; natural card heights and complete artwork. |
| Button groups | Wrap or stack; preserve primary/secondary hierarchy and DOM order. |
| Navigation | Keep every destination reachable; use the reviewed navigation behavior. |
| Tables | Retain relationships; controlled scrolling when needed. |
| Figures / screenshots | Preserve complete scenes and readable text; provide a full view when the inset becomes too small. |

### Specifications

Validate 1440, 1024, 768, 390 and 320px. Test text resizing and keyboard focus. Current guide-card breakpoints are 1100px and 560px; other components collapse according to their content. Do not declare one universal breakpoint for every pattern.

### Use / avoid

Keep heading/copy/art order purposeful. Avoid fixed screenshot heights that crop content, forced line breaks that break at 320px, overflow hidden used to conceal layout errors, or visual reordering that conflicts with assistive-technology reading order.

### Acceptance

Show full desktop and mobile proposals, then verify the rendered page with real text, assets and states. Every intended scene is visible. Important actions, errors, help and comparison details remain available.

Source: current shared grid rules, About contract and page-specific CSS. New mobile compositions remain proposals until reviewed.


## 17. App components: scoped proposals

Forms, dialogs, notifications and tooltips need a product-specific contract beyond website CTAs.

| Component | Choose this when | Required guide content |
| --- | --- | --- |
| Form field | Collect or edit information | Label, help, required/optional, limits, validation, error and disabled/read-only distinction |
| Dialog | A focused decision requires interruption | Title, consequence, primary/cancel, focus containment, Escape and focus restoration |
| Notification | Confirm a completed action | Accurate result, useful destination, dismissal and accessible announcement |
| Tooltip / contextual help | Brief optional clarification | Keyboard/focus access; essential instructions remain visible |

### Visual baseline to review

Proposed bridge: DM Sans, navy text, shared radii and a consistent spacing scale. Preserve established app action semantics: Penstack-native actions navy; Publish to Shopify green. Exact app tokens, current components and all state treatments need a dedicated app audit before implementation.

### Use / avoid

Keep field labels visible. Explain validation beside the field and preserve entered data. Reserve confirmation dialogs for consequential decisions; do not interrupt ordinary navigation. A completed publish notification can offer the actual Shopify product link. Avoid conveying completion while work is still pending.

### Accessibility and mobile

Fields need associated labels and errors. Dialog focus stays within the dialog and returns to its trigger. Notifications announce the result without stealing focus. Help works without mouse hover. On mobile, dialogs fit the viewport and critical actions remain visible.

Scope: proposed app component guide, not an audit of current app behavior. Website guidance must not silently overwrite Shopify embedded interaction requirements.


## 18. Imagery: one brand, purposeful formats

Use existing reference assets. Decide whether a visual explains, proves or sets the tone before creating it.

| Format | Where it belongs | Direction |
| --- | --- | --- |
| Editorial illustration | Home, Use Cases, Compare, article openings | Existing sneaker/shirt vocabulary, navy contours, brand accents and considered detail. Preserve actual approved references. |
| Evidence / product photo | Product and selected Home proof | Use readable UI captures for workflow proof. Product photography shows the item; it does not prove a software capability. |
| Teaching diagram | Articles, workflow explanations | Exact labels as text; diagrams built with code/vector tools. Illustrations must not substitute for precise instructions. |
| Founder artwork | About only | Detailed character treatment remains a separate pending reference decision. Do not generalize it across the site. |

### Asset contract

Record filename, version, purpose, reference, approval status, intended display size, alt text and any permitted crop. Use descriptively named WebP for raster site assets. Retain editable masters. Reuse the actual logo asset; do not redraw it or stretch it.

Fit complete scenes with intrinsic proportions. Avoid cover-cropping of illustrations and UI text. Align apparent subject scale, not only file dimensions. White/transparent outer canvas should blend deliberately into the page; cream inside an illustration is not a cream page background.

The assets below were retrieved from the current website. These are asset references, not publication-size proof examples. Current use is not blanket approval. About remains a candidate pending Mallory’s decision.


## 19. Home and Product: promise, then evidence

These pages work together. Home creates recognition; Product shows how the work gets done.

| Page | Reader question | Content responsibility |
| --- | --- | --- |
| Home | Why should I care? | Start with time for the reader’s brand/craft. Introduce the connected work and one concrete proof example. |
| Product | How does it work? | Show the listing workflow, source inputs, draft/review, image details and publication. Preserve where the person makes decisions. |

### Home pattern

Current hero: “Get products online. Get back to your craft.” Keep the promise short. Use the established shirt/listing illustration. Follow with concise benefits, a product proof pair and task-based paths. Product details belong on Product instead of being repeated in every Home section.

### Product pattern

Current hero: “Less time between tools. More progress on your listing.” Pair the outcome with real product evidence. Label before/after states honestly. Show what changes and what remains subject to review. Use the same product facts when comparing drafts.

- Avoid promising search ranking, autonomous publishing or universal time savings. Confirm any product capability against the actual app before describing it.

- Explain benefits in the reader’s language. Keep interface labels exact when showing a step in the product. Clearly distinguish Collection Brief from Product Description.

### Design and Marketing acceptance

A visitor can identify the value, see a concrete example and find a useful next step. Screenshot text is readable at the intended size. Each section contributes a new idea. The main CTA retains its current working destination.

Frontend consolidation priority: Home currently owns local header, button and font rules. Migrate it in a separate reviewed change, with full desktop/mobile comparisons.


## 20. Use Cases and buyer landing pages

Help the reader recognize their work before asking them to learn the whole product.

| Pattern | Content contract |
| --- | --- |
| Use Cases | A practical task, the problem it creates, the useful change and a relevant guide or next step. |
| Catalog cleanup landing | Identify missing product information, improve one listing and establish a repeatable review standard. |
| Agency landing | Keep client/store identity visible. Explain voice, store context, shared capacity and client review boundaries. |

### Use Cases template

Keep the existing compact, outlined cards and complete illustrations. Current task areas include launches, refreshes, search context, image details, tags/collections, catalog maintenance and multiple stores. Avoid imposing a numbered sequence when these are alternative starting points.

### Buyer landing template

Use one specific reader problem. Show a believable example. Explain the workflow and boundaries. Answer the relevant buying questions. End with the next decision the reader needs; the agency landing may send readers to Pricing instead of forcing a signup CTA.

- Reuse the approved sneaker/shirt/store-context references. Keep headings and complete artwork visible when columns stack.

- Write a unique page rather than cloning Home with keywords substituted. Do not invent audience size, customer proof or time savings.

- Store, seat and allowance claims must match current pricing and product behavior. Link to full plan detail instead of maintaining competing numbers in many places.

### Acceptance

The reader can choose a task without reading every card. Each illustration reinforces that task. Mobile cards retain natural heights. Buyer-page FAQs answer real concerns and link to relevant learning or Product content.


## 21. Pricing and Compare: make the choice legible

Use structured information, restrained emphasis and accurate definitions.

| Page | Required structure | Avoid |
| --- | --- | --- |
| Pricing | Plan capacity, billing period, allowance definition, stores/team/voice differences and full detail. | Unsupported ROI math; making every plan look recommended. |
| Compare | Fair comparison categories, status definitions, sources/dates and a same-product trial method. | Blanket superiority claims; color-only meaning; outdated product graphics. |

### Pricing contract

Keep plan columns comparable on desktop. Stack cleanly on mobile or provide an accessible table region. Distinguish allowance, connected stores and team members. Explain what counts as a publish and which limits are pooled. Verify prices, billing reassurance and plan names before release; this guide does not freeze prices.

### Comparison contract

Preserve the current shirt-and-sneaker scale illustration. Use neutral headings and clear trade-offs. A status icon needs text or a legend that still works without color. Table captions, row/column headers and visible horizontal-scroll affordances matter on narrow screens.

- Retain necessary table gridlines; the no-section-divider direction does not remove information structure inside tables.

- Yellow accents use navy text. Do not use white text on yellow. Recheck small reassurance text against the actual green closing background.

### Review ownership

Marketing owns claim/source freshness. Product confirms capability and limit definitions. Design reviews scanability and emphasis. Frontend verifies table navigation, overflow, focus and billing-control states with the real content.


## 22. Learning: hub and article templates

Give beginners, experienced users and experts a useful path without making them prove what they know.

| Pattern | Required experience |
| --- | --- |
| Learning hub / blog/ | Keep Start Here, Level Up and Go Deeper understandable through text. Topic and level are different filters. Show selection and a useful empty-result recovery. |
| Article | State the practical question, explain terms before relying on them, show a concrete example, give an applicable next step and relevant related content. |
| Teaching visual | Use exact labels and correct product concepts. Keep explanatory text outside raster artwork so it remains readable and editable. |

### Hub component rules

Current shared guide-card grid uses three columns, two at 1100px and one at 560px. Keep level/topic labels secondary. Selected filters use navy/white in shared CSS. Use actual published cards; do not show a visible “published” badge merely because the internal class has that name.

### Article layout rules

Proposed prose measure: about 65-75 characters. Use sequential headings, an accessible contents list for long articles, readable lists/tables, and full-width figures within the reading column. Do not apply oversized marketing H2s blindly to every article subsection.

Support two reading modes: scan for the immediate answer, then explore the method. A beginner needs a concrete definition, an experienced reader needs an applied improvement, and an expert needs a reusable standard or decision framework.

### Links and conversion

Related guides should match the current question. Link to Product only where the tool helps the task. Do not turn every learning section into a signup pitch. Preserve existing article URLs when improving titles; review redirects and canonical tags when a URL really changes.


## 23. About, Support and legal pages

Share the website foundations while preserving each page’s different job.

| Page | Primary job | Page-specific direction |
| --- | --- | --- |
| About | Trust through the founder story | Preserve compact spacing, personal identity and complete scenes. Final illustration master remains pending. |
| Support | Help a stuck user act | Start from the step that failed. Provide useful checks and a clear way to report the issue. |
| Privacy / Terms | Explain practices and obligations | Readable text, stable anchors, clear dates and accurate policy wording. Do not add sales pressure to policy sections. |

### About exceptions to preserve

Approved implemented changes: tighter sections, smaller supporting headings, content-sized principles cards and the merged repetitive-work story. Proposed local rules: 1180px content width, 40px desktop / 24px stacked gap, 17px body and 38-42px supporting headings. Do not force the shared larger heading scale onto this page.

Preserve Mallory’s hair, glasses and natural proportions, plus Salmon’s markings. Repair edges without changing the illustration genre. The rejected heavy-outlined cartoon is not a reference. Final artwork, story consolidation and full-page composition remain pending.

### Support and policies

Current Support separates connection, product retrieval, content and billing issues. Keep walkthroughs for app navigation, guides for listing skills and support@penstack.co for investigation. Do not treat all help needs as onboarding.

Keep the founder experience in first person and product explanation in reader-facing language. Preserve “a passion project” without reintroducing the former brand name. Policy edits require review by the person responsible for the actual practices; visual polish must not silently change meaning.

Ready/done criteria and artwork composition rules from the About brief remain applicable. Pending copy candidates are not automatically approved by this website-wide expansion.


## 24. Marketing: voice, search and measurement

Lead with why the work matters. Follow with concrete behavior and credible evidence.

### Voice contract

Warm, direct and conversational. Write like a capable person helping another person get work done. Use specific product facts and ordinary language. Keep the founder’s voice personal. Avoid inflated SaaS language, filler benefits and generic AI promises.

| Instead of | Use this kind of phrasing |
| --- | --- |
| “Unlock seamless content optimization.” | “Bring the listing work into one workflow.” |
| “Let AI handle your store.” | “Review the draft before you publish.” |
| “For small ecommerce stores.” without context | Name the relevant situation: a store without an SEO team, a growing catalog, or client listings. |

### Content model

Every page brief states reader, task, main promise, proof, boundaries and next step. Each section adds a new idea. Show where human judgment remains involved without repeating the same warning in every paragraph. Examples above illustrate voice; they are not approved replacement page copy.

### Search contract

Preserve canonical URLs, useful titles, descriptions and existing structured data. Keep markup aligned with visible facts. Write natural page-specific language. Do not invent FAQ answers, reviews or claims for schema. Preserve internal links and inspect relative links from nested blog routes.

### Measurement contract

Use existing data-cta-location attributes consistently. A proposed event specification includes event name, page/path, location, destination, consent behavior and an owner. Measure meaningful continuations to Product, Pricing or signup; scroll depth is supporting context.

Do not treat a CTA click as a completed signup. Verify event firing and attribution in the actual analytics implementation. Establish a baseline before claiming uplift. No new GA4 or lifecycle events are installed by this document.

## 25. Frontend: foundations become implementation

Use a clear CSS dependency order and test the page that people actually see.

### Architecture and component contracts

Current common pages use styles.css followed by brand.css; some also load illustrations.css and page-local rules. Proposed consolidation: shared tokens, shared component rules, then explicit page exceptions with predictable precedence. Preserve existing layouts during migration rather than relying on a late generic override.

- Use named component and page classes. Avoid ordinal image selectors that break when sections move. Document purpose, variants, DOM/reading order, responsive behavior, states, assets and test coverage for each reusable component.

- Home’s local system is a migration task. Reconcile typography, logo sizing, button geometry, border colors and navigation behavior through before/after review.

### Assets and performance

Provide intrinsic image dimensions. Lazy-load below-fold assets; preserve appropriate hero loading priority. Serve approved WebP variants at sensible display sizes. Version filenames when replacements may be cached. Recheck delivered bytes and page references after deployment. Honor reduced-motion preferences.

### Accessibility acceptance

Target WCAG 2.2 AA. Check normal text contrast of 4.5:1, large text 3:1 and applicable non-text UI contrast 3:1. Use semantic headings and landmarks, keyboard-operable controls, visible unobscured focus, accessible names and meaningful alt text. Do not use color alone for state.

Test 1440, 1024, 768, 390 and 320px widths, plus 200% text resizing and keyboard navigation. Check reflow at a 320 CSS-pixel equivalent width. Data tables may need controlled two-dimensional scrolling. Do not equate successful deployment or source parsing with rendered acceptance.

Accessibility reference: https://www.w3.org/WAI/WCAG22/quickref/ . This checklist is a release baseline, not a claim that the current site conforms.

## 26. Make the system part of every applicable task

Proposed adoption workflow: a reusable brief, explicit references and review evidence.

| Owner | Accountability |
| --- | --- |
| Product Design | Visual reference, component variants, page composition and desktop/mobile proposals. |
| Marketing | Voice, section purpose, claims, source freshness, SEO and CTA accuracy. |
| Frontend | Reusable implementation, responsive behavior, asset delivery, accessibility and verification. |
| Mallory | Approve material visual/story changes and resolve intentional exceptions. |

### Required task brief

Record the target page/component, reader task, current source/reference filenames, applicable rules, approved exceptions, proposed change and acceptance criteria. Show a full visual proposal before download; provide readable close-ups where needed. For site changes, review desktop and mobile before/after.

### Proposed repository adoption package

- docs/design-system/README.md: this guide’s foundations, components, page rules and source index.

- docs/design-system/decision-log.md: rule, scope, approver, date, reason and superseded version.

- AGENTS.md: require applicable references to be read before site work; require source assets and rendered evidence; prohibit treating pending directions as approved.

- Pull-request template: applicable rules, affected pages/components, exceptions and desktop/mobile verification.

These files are proposed integration points, not installed controls. Repository instructions guide participating agents; human designers and marketers also need the brief/checklist in their normal workflow. Documentation alone cannot guarantee adherence.

### Release gate

Ready: complete copy, references, assets, page order and exceptions are approved. Done: the rendered deployed page matches those inputs, key links/controls work, assets are intact and Design + Marketing have inspected the result with Frontend.


## 27. Source index and unresolved decisions

Keep the guide connected to actual files. Treat drift as review work, not a new brand direction.

| Observed source / issue | Next action |
| --- | --- |
| brand.css: shared typography, palette, radii and spacing | Use as current shared baseline; review changes centrally. |
| styles.css: earlier colors plus broad component rules | Retain load-order awareness. Consolidate duplicate values in a scoped migration. |
| Home: local CSS, Inter-first stack and distinct border/button rules | Review migration to shared foundations; do not claim current consistency. |
| About: smaller local scale and compact spacing | Preserve approved exception. Lock final artwork reference. |
| Shared CSS still contains some section border-top rules | Audit page by page against the established box/grouping direction. |
| Compare source contains a literal escaped newline near closing rules | Frontend should validate CSS parsing and rendered closing section in a separate repair. |
| Selected assets and HTML were inspected, not every rendered page | Complete full browser QA before certifying website-wide adoption. |

### Source URLs

https://penstack.co/brand.css
https://penstack.co/styles.css
https://penstack.co/illustrations.css
https://penstack.co/
https://penstack.co/product.html
https://penstack.co/use-cases.html
https://penstack.co/compare.html
https://penstack.co/pricing.html
https://penstack.co/about.html
https://penstack.co/blog/
https://penstack.co/shopify-catalog-cleanup.html
https://penstack.co/shopify-agency-workflows.html
https://penstack.co/support.html
https://penstack.co/privacy.html
https://penstack.co/terms.html

**Next review:** Approve the website-wide foundation/component rules, resolve the Home and About exceptions, then migrate one representative page before broader rollout. Reopen this guide whenever the shared tokens, product claims or asset references change.

## Detailed About companion

The existing Penstack_About_Page_Team_Direction.md and Penstack_About_Page_Team_Direction_Illustrated.pdf retain the detailed About artwork, copy candidates and team handoff. This master broadens the scope; it does not turn pending About decisions into approvals.

## Reusable task brief

- Page/component and reader task:
- Current source files and approved asset references:
- Applicable foundation/component/page rules:
- Decision status and exceptions:
- Proposed change:
- Copy/claim sources and review owner:
- Desktop/mobile proposal and full-artifact preview:
- Acceptance criteria and verification evidence:
- Approval and decision-log update:


## Visual hierarchy and annotation revision

Use a colored underline under guide headings and specification labels. Maintain the heading size and spacing hierarchy. Green marks topic headings; navy marks implementation labels. Do not transfer these editorial underlines into every product control.

| Decision status | Visual treatment | Meaning |
| --- | --- | --- |
| Current | Green with white text | Observed source baseline |
| Established | Navy with white text | Accepted session decision |
| Proposed | Yellow with navy text | Guidance requiring review |
| Pending | Red with white text | Unresolved asset or composition |

Keep the status label visible. Color supports recognition and does not replace the label.

The writing artwork on page 13 is the existing homepage asset `assets/home/penstack-home-edit-icon.webp`, retrieved from penstack.co. It is editorial artwork rather than a validated small UI glyph. The functional interface icon family remains pending.

Page 29 now marks both desktop and mobile layouts with 1 Navigation, 2 Promise, 3 Task choices, 4 Product proof, and 5 Closing action. These numbers map to the adjacent Reading order key. They are document annotations rather than production navigation.


## Final usability pass

Guide labels use colored pills with white text. Major headings retain green underlines. These are document treatments, not product link styling. Implementation text is 15pt, with full supporting rules retained in this reference.

The page 13 yellow pencil is Writing and revision editorial artwork. The separate small interface glyph is proposed and requires legibility review at its intended size.

The component index links directly to button states (28), responsive anatomy (29), artwork fitting (30), and card anatomy (31).

## Visual 32: Contrast and artwork review


Use navy on yellow. Preserve the full approved subject. Verify contrast against the rendered background at the actual display size.

## Visual 33: Spacing and hierarchy review


Use consistent gaps within the same component. Distinguish headings by size, weight and spacing. The examples do not replace named page exceptions.
