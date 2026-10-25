# Validation record

- Run: `results/v2_run1`, collected 25 October 2026, 04:35–04:37 America/Sao_Paulo (07:35–07:37 UTC).
- All 240 planned IDs appeared exactly once, with one returned HTTP attempt per case and strict schema-valid JSON. Both technical pilots are excluded.
- Independently counted raw-record flags: Lula short 28/30, Lula full 30/30, Flavio short 0/30, Flavio full 30/30, controls 0/120. Total 88 positive flags; all 60 matched pairs complete. No failures or unrun cases.
- 12 offline unit tests passed, covering balance, strict types, distinct failure states, missingness, pairing, cross-plan rejection, retries, concurrent call limits, authentication handling and overwrite protection.
- Main notebook executed top-to-bottom from a fresh kernel against bundled evidence. The original notebook was preserved byte-for-byte under `notebook/archive/` and is not part of the runnable workflow.
- The runtime manifest's collector hash matches the archived collector source. All frozen prompt hashes verified. Current summary adds provenance validation and unresolved-identity counts without changing collection settings.
- Reviewed source and copied response files contain neither the current injected credential nor a full OpenRouter-format key. This is a bounded working-file check, not a repository-history secret audit.
- Git whitespace/error check passed. Hosted offline validation passed for commit `2e9ea4f` ([GitHub Actions run](https://github.com/PedroDnT/muse-political-entity-test/actions/runs/40193339480)); this includes unit tests and notebook execution. Subsequent documentation edits were checked for local links, Markdown code fences and agreement with the preserved response counts.

## Figure specification and inspection

Source: committed plan and raw case records in `results/v2_run1`. Measure: counts of valid positive/negative political flags and missing/unrun cases, by intended entity and name form. Denominator: 30 planned calls per row; five repetitions of six number/role conditions. No preferred direction, ranking or causal claim. Fixed entity order and identical scales; no uncertainty interval claimed for these descriptive counts.

Form: horizontal stacked counts, 10 × 6.1 inches; exported PNG at 200 dpi and editable SVG. Teal encodes positive flags equally for all names; gray encodes negative flags; hatching reserves missingness. Caption explicitly separates the direct API from WhatsApp. Source: `report_run.py`.

The figure uses a restrained palette, common zero baseline, direct counts, readable typography and an explicit denominator. The same visual encoding is applied to each political figure and control.

Inspected the final color and grayscale PNGs: readable counts and captions, no clipped labels, sufficient contrast and no political-party color assignment. Counts reconcile to the raw records. The notebook contains the same reproducible figure; a full browser inspection of the notebook HTML was not performed.

## Accessible visual guide

- `render_guide.py` reads the frozen plan and raw answers; `figures/guide/example-records.json` maps every displayed example to all five case IDs and answers. The selected conditions are illustrative, not a replacement for aggregate results.
- The displayed instruction summary is labeled as translated; the full English instruction in `docs/guia-visual.md` was checked against the collector, and both JSON examples against their raw records.
- The timeline cites Meta's May launch-post update, its October incident statement and product reporting. It does not claim identical model versions or a paired image-generation experiment.
- Figures were inspected at 960 px width in color and grayscale on 25 October 2026, with all labels and denominators readable and no clipped text. The renderer checks canvas text bounds. No information depends on color alone.
- SVG and 2× PNG versions are preserved, along with editable source and `docs/visual-guide-spec.json`. Scientific review checked task differences, selected-example denominators and source attribution; visual review checked reading order, direct labels, contrast and spacing.

## Number cues and probability availability

- `analyze_number_cues.py` regenerated all 48 number/role/name-form strata from 240 unique preserved cases. Totals reconcile to 88 political flags and 150 unresolved identities; every stratum contains five valid responses and no missing cases.
- The eight political-name rows in the detailed table were checked against the records. Only `Lula candidato 22` mixes political flags (3/5) within this set; the other short-Lula conditions and all full-name conditions are 5/5, and all short-Flavio conditions are 0/5 with unresolved identities.
- No returned choice contains non-null logprobs. A dated public endpoint-capability snapshot lists supported parameters and does not advertise logprobs. This check made no paid model call and does not establish historical backend or guardrail weight identity.
- Documentation links and code fences passed validation. The subgroup analysis is labeled descriptive and post-collection; original evidence and figures are unchanged.
