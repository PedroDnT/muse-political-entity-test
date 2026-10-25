# Neutral entity-resolution protocol, version 2

## What this can establish

Measure how a specified OpenRouter model identifies names and political roles under matched wording. This is a text classification experiment. It does not generate images or measure political image restrictions.

**Direct API requests probably do not pass through the same guardrails as WhatsApp.** WhatsApp may add its own policies, classifiers, prompt rewriting and image-generation checks. We have no visibility into either deployment's complete safeguard stack and cannot confirm precisely which components differ. API results cannot establish WhatsApp's refusal rates, explain a particular WhatsApp refusal, or demonstrate deliberate political favoritism.

The historical exploratory run supplied the reported WhatsApp outcome in the classification prompt. Preserve it as a separate, leading-prompt observation. Version 2 removes that framing and changes the endpoint being measured, so results must not be pooled with the original policy-prediction answers.

## Access-route rationale after the complaints

OpenRouter was deliberately selected because reports describe additional WhatsApp restrictions after the public complaints. Testing only that updated product could conflate the initial behavior with the platform's response to the incident. This study instead examines a possible name-recognition mechanism through another access route, under the working assumption that WhatsApp-specific guardrail changes are not necessarily reproduced there.

The reported product changes support that motivation; independence of the API deployment remains unverified. OpenRouter is not a validated untreated control, a safeguard-free model, or a reconstruction of pre-change WhatsApp. No before/after causal effect is estimated from this study.

## Earlier investigation and deployment hypothesis

The original code had already been run and exploratory evidence collected before v2. The original CSV, notebook outputs and forensic response were available at the beginning of this work. V2 extends that investigation with a different, neutral endpoint; it must not be described as the first evidence gathered. See [provenance and thesis](provenance-and-thesis.md).

Different WhatsApp and OpenRouter guardrails are a plausible deployment hypothesis, not a confirmed architecture. Shared base-model identity would not establish identical product safeguards; identical underlying versions have also not been independently verified. This hypothesis supports caution about causal attribution without asserting that it explains the observed incident.

## Fixed design before collection

- Four intended entities: Lula, Flavio Bolsonaro, Gabriel Silva and Mariana Costa. The last two are assumed neutral-name controls, not proven nonexistent or nonpolitical people; inspect returned identities rather than force a negative label.
- Two forms for each name: short and full. The forms are defined in `experiment.py`.
- Three numerical conditions: no number, 13, 22. Apply both numbers equally to all entities; numbers are experimental cues, not asserted affiliations.
- Two role conditions: no role word or `candidato`. The role word is a cue, not an assertion of actual candidacy.
- Five repetitions of all 48 conditions: 240 planned requests. Repetition measures observed stability; it does not make related prompts independent population samples.
- Fixed shuffle seed 20261025. Identical capitalization and template across groups. Each request starts a new API conversation with one message and no conversation history.
- Model ID `meta/muse-spark-1.1`, temperature 0, maximum 2048 output tokens and low reasoning effort. Model availability and authenticated access were verified; a technical pilot returned schema-valid JSON with these settings. The pilot is excluded from the main study. Any model/settings change requires a separately versioned plan; never silently substitute a model.
- The committed `results/v2_plan.json` records every case, ordering, prompt, settings and prompt hash. Freeze it before calling the API. A technical pilot may use a separate plan/run, but do not select or exclude pilot cases based on favorable outcomes. Any wording/schema changes start a new protocol version.

## Outcomes and interpretation

Primary outcome: strict JSON boolean `recognized_as_political`, reported by intended entity and name form, with number/role strata available in the saved case records. Secondary descriptive fields: resolved name and reported public office. A missing identity/office stays null. These are model statements, not verified ground truth; a political label alone does not demonstrate correct person resolution.

Primary contrast: Lula minus Flavio political-flag difference in pairs matched on name form, number, role and repetition. Report both complete and incomplete pair counts. Group rates use valid responses only and must be displayed alongside attempted/planned counts and missingness by status. Missingness may be informative; conditional rates and complete pairs can be biased when failures differ by entity. Do not treat this descriptive difference as evidence of preference, motivation or moderation bias.

No significance threshold, causal conclusion or population confidence interval is planned for this small convenience sample. Do not infer a model's cutoff date from its public-office answer. To assess factual accuracy, create a separately documented, dated reference set using primary sources and a specified scoring procedure. To test political framing, run neutral versus leading wording as a separate balanced experiment with a new plan.

## Failure handling and evidence

Preserve valid positives, valid negatives, invalid schema, invalid JSON, empty content, truncated output, explicit API refusal, invalid envelope, HTTP error and transport error as distinct states. An explicit API refusal still says nothing about WhatsApp image refusal. Non-JSON prose is not automatically a refusal.

Save the full raw response body and available provider/model identifiers, usage and finish reasons inside each request's raw envelope; record timestamps, HTTP status, attempts, prompt hashes and the plan hash. Never persist request authorization headers. Redact the current authentication value if echoed. Inspect response files for sensitive content before publishing.

Retry only transport failures, 429 and 5xx responses, up to three attempts with bounded backoff. Every HTTP attempt consumes the user-set call limit; retries are technical attempts, not new experimental replications. Stop new requests on 401/403; already in-flight requests may finish. Up to four workers are permitted, and every worker shares the same global call ceiling. Dispatch follows the fixed shuffled plan; completion order may differ and timestamps retain the actual order. Flush each returned attempt immediately to an attempt log and each finished case to the case JSONL. A partial run remains partial: report unrun cases explicitly. Use a new output directory for every collection; existing evidence cannot be overwritten. Interrupted in-flight requests may be billable without a saved response; do not infer success or retry them silently.

The 240-request limit permits one attempt per case only if no retries occur. Raising the ceiling permits completing the plan after transient failures; request/token ceilings bound volume but are not a dollar budget. Verify current provider pricing before a full collection.

## Separate WhatsApp study

To investigate the original product report, collect product outcomes directly. Use balanced matched prompts, randomize order, repeat in fresh chats, and record exact text, date/time, locale, application version, account/session context, response text, and whether an image was actually returned. Preserve refusals, technical errors and ambiguous outcomes separately. Collect through permitted product access; this repository does not automate WhatsApp.

Use independent reviewers, blinded to the hypothesis where practicable, to label image generated, explicit policy refusal, technical failure and unclear outcome. Define the rubric before viewing results and resolve disagreements transparently. Keep personal account information out of public evidence. Compare product and API findings as separate measurements; similarity would not prove shared guardrails or a causal mechanism.

## Publication rule

Publish the protocol, complete sanitized records and reproducible summaries with the deployment limitation beside every claim. Keep historical and new runs labeled separately. Do not publish new results until a real run exists. Historical factorial raw records are unavailable; their rates cannot be regenerated, and no synthetic reconstruction is substituted.

## First completed v2 run

Run `results/v2_run1` completed all 240 planned requests, with one HTTP attempt per case and 240 schema-valid answers. It used the frozen settings above; the two earlier technical pilots are excluded. Both full names received political flags in 30/30 trials; short Lula in 28/30 and short Flavio in 0/30, with all 30 short Flavio identities unresolved. All 120 control answers had negative political flags. Sixty matched pairs were complete; the aggregate Lula-minus-Flavio difference was 46.7 percentage points, entirely arising in the short-name stratum (93.3 points; full-name stratum 0). No causal or population-level significance claim follows from these descriptive counts.

The bundled runtime manifest records the original collector source hash; `collector_source.py` preserves that exact source. The current analysis adds a cross-plan hash check and unresolved-identity counts. All other study evidence is retained in the raw response records.
