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

Form: horizontal stacked counts, 11 × 7.6 inches; exported PNG at 200 dpi and editable SVG. Teal encodes positive flags equally for all names; gray encodes negative flags; hatching reserves missingness. Caption identifies a text task through the API and distinguishes no political flag from an image refusal. Source: `report_run.py`.

The figure uses a restrained palette, common zero baseline, direct counts, readable typography and an explicit denominator. The same visual encoding is applied to each political figure and control.

Inspected the final color and grayscale PNGs: readable counts and captions, no clipped labels, sufficient contrast and no political-party color assignment. Counts reconcile to the raw records. The notebook contains the same reproducible figure; a full browser inspection of the notebook HTML was not performed.

## Accessible visual guide

- `render_guide.py` reads the frozen plan and raw answers; `figures/guide/example-records.json` maps every displayed example to all five case IDs and answers. The selected conditions are illustrative, not a replacement for aggregate results.
- The displayed instruction summary is labeled as translated; the full English instruction in the consolidated `README.md` was checked against the collector, and both JSON examples against their raw records.
- The timeline cites Meta's May launch-post update, its October incident statement and product reporting. It does not claim identical model versions or a paired image-generation experiment.
- Figures were inspected at 960 px width in color and grayscale on 25 October 2026, with all labels and denominators readable and no clipped text. The renderer checks canvas text bounds. No information depends on color alone.
- SVG and 2× PNG versions are preserved, along with editable source and `docs/visual-guide-spec.json`. Scientific review checked task differences, selected-example denominators and source attribution; visual review checked reading order, direct labels, contrast and spacing.

## Number cues and probability availability

- `analyze_number_cues.py` regenerated all 48 number/role/name-form strata from 240 unique preserved cases. Totals reconcile to 88 political flags and 150 unresolved identities; every stratum contains five valid responses and no missing cases.
- The eight political-name rows in the detailed table were checked against the records. Only `Lula candidato 22` mixes political flags (3/5) within this set; the other short-Lula conditions and all full-name conditions are 5/5, and all short-Flavio conditions are 0/5 with unresolved identities.
- No returned choice contains non-null logprobs. A dated public endpoint-capability snapshot lists supported parameters and does not advertise logprobs. This check made no paid model call and does not establish historical backend or guardrail weight identity.
- Documentation links and code fences passed validation. The subgroup analysis is labeled descriptive and post-collection; original evidence and figures are unchanged.

## Consolidated study page and count-chart labels

The README now contains the complete reader-facing narrative, from model and guardrail concepts through allegations, methods, results and the evidence synthesis. Former overview pages retain their URLs and point to this single narrative; technical appendices are labeled as such.

The count chart uses the exact input names from `experiment.ENTITIES`, Portuguese labels and the original counts. Unused missingness legend entries are hidden only when every case is valid; partial runs retain missingness bars. The 1100 × 760 px render was inspected in color and grayscale, and all text bounds were checked. SVG and 2× PNG exports and the notebook figure were refreshed. The saved numerical summary is unchanged.

## Reinspection of original evidence

- The archived notebook, Run 1 CSV and forensic JSON match their initial-commit versions byte for byte. The CSV was also checked field by field against the literal result list embedded in the notebook: 24 attempts, 20 valid classifications, two null parsed objects and two error dictionaries.
- `review_original.py` recomputes role/policy-prediction counts and records the duplicate full-name Flavio prompt. It verifies all 40 printed factorial requests against the original design and extracts the ten-row pre-fill preview plus eight printed positive cases without executing collection code. Missing preview fields remain null and truncated reasons remain marked by their original ellipses.
- Original API timestamps, request IDs and response creation fields were not found. The original commit date establishes artifact availability before v2. The author dates both original runs to 14 October; this is separately labeled as author-reported, without independently preserved call timestamps or within-day ordering.
- README counts, partial-record indices, local links and Markdown fences were checked. No source responses, original notebook bytes or v2 measurements were changed, and no new API calls were made.

The reported execution date is preserved in the audit generator and JSON metadata. The README frames the experiment as a case for algorithmic literacy, without claiming to measure public knowledge or prove the cause of public reactions.

## Expanded shared Colab

The shared notebook has 35 cells; unlike the initial 22-cell archive, it displays all 40 factorial rows in two agreeing tables (zero-based cells 21 and 28). The extraction retains 29 valid classifications and 11 missing, with political-label/candidate/policy fields separate. Prediction counts are Lula 6/6, Flavio 0/9, Tarcisio 2/5, Gabriel 0/9 among valid answers. The original plan and prior ten-row preview agree with the recovered table.

Cell 31's saved execution output explicitly reports mock-data reconstruction; its correlation and regression are excluded. Only the credential-free source table and derived records are published, with provenance hashes. No notebook code was executed and no model calls were made.
