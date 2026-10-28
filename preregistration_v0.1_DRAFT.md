# Pre-registration (DRAFT v0.1 — NOT YET LOCKED)

**Working title:** Does purity-aware, cell-type-informed bulk-expression ranking recover CRISPR-validated tumor-intrinsic immune-evasion genes? A pre-registered, multi-cancer benchmark (PDAC primary; melanoma and colorectal secondary) with a STYK1 case study

**Author:** [FILL]  **Date drafted:** 2026-10-21  **Repo:** [FILL]  **OSF/commit hash at lock:** [FILL]

> **How to read the markers.** `[FILL]` = you must supply it. `[VERIFY]` = I could not confirm this from a source I checked; verify before locking. `[PENDING STEP n]` = to be completed in that step of our process *before* the lock. Nothing in this file is locked until the lock procedure in Section 12 is done.

---

## 0. Lock rules and data-access rule

1. **Lock = a git tag `prereg-v1.0` on a commit containing this file plus the frozen ground-truth files and the config, AND an OSF registration of the same files.** After lock, changes are made only as dated amendments (Section 11).
2. **Data-access rule.** Before lock, do not open, plot or summarize per-gene expression, survival, or purity data from any study cohort. Allowed before lock: ground-truth gene lists from published tables, cohort metadata, counts of samples and events (needed for power), and scRNA-seq cell-type annotation tables.
3. **Prior-exposure statement (honesty requirement).** The author previously analyzed TCGA-PAAD and TCGA-SKCM in the IEDP project and knows STYK1's IEDP rank. The benchmark hypotheses (H1–H3) were designed without reference to those results, but H4 (STYK1) and any SKCM result are **not blind**. This is stated in the manuscript.
4. **Further prior exposure (2026-10-28).** Before lock, the author read the supplement of a 2025 JCI Insight multi-cohort PDAC paper (DOI 10.1172/jci.insight.174264). It lists STYK1 as consistently upregulated in five PDAC expression datasets, high in tumor epithelium and low in stroma by laser-capture RNA-seq (compartment level, not single-cell), not specific to basal-like or classical subtype, and higher in KRAS-mutant tumors in TCGA. H5 therefore tests an expectation that is partly anticipated at compartment level; its added value is single-cell resolution including NK/T and myeloid cells. Any novelty claim for H5 is worded accordingly.

## 1. Rationale (one paragraph for the preprint)

Bulk-expression screens for "immune evasion" genes can be confounded because tumor purity and stromal/immune content drive both gene expression and immune-marker correlations. There is currently no pre-registered test of whether common bulk-ranking strategies, with and without purity and cell-type adjustment, recover genes independently shown by CRISPR screens to control tumor-cell resistance to T-cell killing. A well-designed null (adjustment does not help; bulk ranking does not recover ground truth) is an informative result.

## 2. Hypotheses, endpoints and falsification

**Primary hypotheses are tested in a fixed sequence (H3 → H1 → H2).** Each is tested at two-sided α = 0.05 *only if the previous one passed* (fixed-sequence gatekeeping, so no further multiplicity adjustment). If a gate fails, later hypotheses are reported as descriptive.

| ID | Hypothesis | Endpoint | Supported if | Falsified if | What a falsification means |
|---|---|---|---|---|---|
| **H3** (gatekeeper) | The purity-adjusted composite (M5) recovers ground-truth genes better than chance | Mean across the 3 cancers of AP-lift (Sec. 6) | One-sided permutation p < 0.05 vs. label-permutation null | p ≥ 0.05 | Bulk purity-adjusted ranking does not recover CRISPR-validated genes beyond chance in this design. Publishable null. |
| **H1** (primary) | Purity adjustment improves recovery | ΔAP-lift = M5 − M2b, averaged equally across cancers | 95% paired-bootstrap CI for the mean Δ excludes 0 (lower bound > 0) | CI includes 0 or lower bound ≤ 0 | Adjustment does not measurably help here (or this design cannot detect it; see power, Sec. 8) |
| **H2** (primary) | Malignant-cell information adds to purity adjustment | ΔAP-lift = M6 − M5, over cancers with usable scRNA-seq | Same CI rule | Same | Single-cell weighting adds nothing detectable |
| **H4** (case study, descriptive) | STYK1 survives adjustment in PDAC | STYK1 rank percentile in the PDAC universe under M2b, M5, M6 | "Survives" if top 5% under M5; "does not survive" if outside top 20%; otherwise "indeterminate" | n/a (descriptive; single gene, no p-value) | If it does not survive, the IEDP ranking of STYK1 is likely a purity/compartment artifact |
| **H5** (single-cell localization, PDAC) | STYK1 is expressed mainly in malignant epithelial cells | Patient-level pseudobulk mean log-normalized STYK1 per compartment (malignant epithelial, NK/T lymphoid, myeloid, fibroblast, endothelial) | Malignant > each other compartment, paired Wilcoxon, BH q < 0.05 across the compartment comparisons | Any compartment not lower at q < 0.05 | STYK1 is not predominantly tumor-cell expressed; reframes the immune association |

**Secondary endpoints (BH-adjusted at q < 0.05 within the family):** per-cancer AP-lift for every method; precision at top k = 100, 200, 500; ROC-AUC; enrichment of positives in the top 5% / 10% vs. permuted labels; bootstrap rank stability (Sec. 6); sensitivity to composite weights (random Dirichlet weights vs. equal weights); leave-one-pathway-module-out AP-lift; stricter ground truth (P3).

**Negative-control endpoints (reported always, interpreted before the main result):**
- **NC1** permuted gene labels (10,000 permutations).
- **NC2** *sign-flipped set*: genes whose loss makes tumor cells *more resistant* to T-cell killing (IFNγ-pathway-type genes). A valid evasion-ranking should **not** enrich these. If it does, the method is reading infiltration/IFN signaling, not evasion.
- **NC3** *decoy set*: DepMap common-essential genes [VERIFY release; list frozen at lock]. Enrichment here means the method is detecting generic tumor-high or proliferation genes.
- **NC4** *mismatched-cancer ground truth*: positives from a screen in a different cancer's model scored against this cancer's ranking.

**Exploratory (labeled as such in every output):** anything not listed above, including any new method, filter, threshold or cohort added after seeing results.

## 3. Design overview

- **Unit of analysis: the gene.** Patients/samples are used only to compute each gene's score.
- **Universe U (per cancer):** genes with a 1:1 human–mouse ortholog in a named, versioned table [FILL version] **and** expressed in the cohort (proposed rule: TPM ≥ 1 in ≥ 20% of the included tumor samples [VERIFY the unit provided by the data source]). *Rule is fixed here; any change = amendment.* Restricting to 1:1 orthologs means mapping cannot create differences between positives and negatives.
- **Labels:** positives = ground-truth genes in U; everything else in U is *unlabeled*, not confirmed negative. Unlabeled genes may include true evasion genes lacking screen evidence, so absolute AP is a lower bound. Comparisons between methods remain valid because all methods share the same universe and labels.
- **Cancers:** PDAC (primary), SKCM and COAD (secondary). Selection reason: availability of matched CRISPR ground truth (Sec. 4) and public single-cell data. Not selected on any result.
- **No fitted weights.** All methods are rule-based. This removes most train/test leakage; there is no model to tune on the data.

## 4. Ground truth [PENDING STEP 4 for final frozen lists]

- **P1 (primary positives):** the "core" genes from the pan-model T-cell-killing screens (Lawson et al., Nature 2020) whose loss **increases tumor-cell sensitivity** to T-cell killing (i.e., evasion-*promoting* genes), mapped to 1:1 human orthologs. `[VERIFY supplementary table and the direction convention in the paper]`
- **P2 (secondary):** core cancer-intrinsic evasion genes consistent across multiple models in the PNAS Mga paper (DOI 10.1073/pnas.2406325121). `[VERIFY gene list and criteria]`
- **P3 (stricter):** genes with evidence of the same direction in ≥ 2 independent screens (candidate sources: Lawson 2020, Dubrot 2022, Manguso 2017, the MC38/gp100 JITC 2021 screen, and the CTIS compendium). `[FILL final source list]`
- **Cancer-matched sets (secondary):** PDAC ← Dubrot 2022 pancreatic in vivo model `[VERIFY model name and that tables are public]`; SKCM ← B16-based screens; COAD ← MC38/CT26-based screens.
- **Freeze procedure:** save each list as a plain-text file, record the source table, the selection rule and the ortholog table version, commit it, and record a SHA-256 hash in this document **before** any ranking exists. The lists are never edited after seeing performance.
- **Module warning:** these gene sets are dominated by a few biological modules (IFNγ/TNF response, autophagy). Hence the leave-one-module-out sensitivity analysis.

## 5. Methods compared (all produce a score; higher = more evasion-promoting)

| ID | Method | Definition |
|---|---|---|
| M0 | Random | Permuted ranking (null) |
| M1a–d | Single-component baselines | (a) tumor-vs-normal differential expression (DES) only; (b) mean expression; (c) IEC_raw: inverse Spearman correlation with the frozen immune-marker set; (d) SH_raw: univariate Cox hazard ratio |
| M2 | IEDP composite as published | z(DES) + z(IEC_raw) + z(SH_raw), equal weights |
| **M2b** | **Unadjusted two-component composite (primary comparator)** | z(IEC_raw) + z(SH_raw), equal weights |
| M3 | Purity-adjusted correlation (TIMER-style) | IEC_pa: partial Spearman correlation controlling for purity (CPE) |
| M4 | Purity + stroma adjusted | Partial correlation controlling for CPE and a stromal score `[VERIFY estimator]` |
| **M5** | **Adjusted two-component composite (primary method)** | z(IEC_pa) + z(SH_adj), equal weights; SH_adj = Cox log-HR adjusted for purity, age, stage (≤ 5 covariates) |
| M6 | Single-cell-informed | M5 with genes weighted/filtered by the fraction of malignant cells expressing them in a PDAC/SKCM/COAD scRNA-seq reference `[PENDING STEP 5 for exact rule]` |
| M7 (optional) | External tool | Gene-level TIDE output if obtainable and reproducible `[VERIFY]`; raw outputs saved |

- **Why M2b vs. M2:** M5 drops DES because tumor-vs-normal contrast has no meaningful purity adjustment. M2b lets H1 isolate the effect of *adjustment* from the effect of *dropping DES*. M5 vs. M2 is reported as a secondary comparison.
- **Frozen immune-marker set for IEC:** `[FILL the exact gene list used in IEDP; freeze with hash]`.
- **Same-samples rule:** every method uses the identical sample set (samples with purity available, one sample per patient) so methods differ only in method, not data.

## 6. Metrics and statistics

- **AP (average precision)** is the primary metric, computed with a pinned library version. **AP-lift = AP ÷ prevalence of positives**, which makes cancers with different universes comparable.
- **Primary inference:** paired, stratified bootstrap (10,000 resamples; positives and unlabeled genes resampled separately within each cancer; both methods evaluated on the same resample). Per-cancer Δlift is averaged with **equal weight across cancers**. 95% percentile CI.
- **Gene-dependence caveat and sensitivity:** genes are not independent (pathway modules). Sensitivity analysis: cluster bootstrap by pathway module `[PENDING STEP 5: define modules and database version before lock]`. If conclusions differ, report both and state that the cluster version is the more conservative.
- **Permutation null:** 10,000 label permutations, preserving the number of positives, run independently within each cancer; the null for H3 is the distribution of the cross-cancer mean lift.
- **Rank stability:** 1,000 sample-level bootstrap resamples; report top-k overlap and Spearman correlation of ranks to the full-data ranking.
- **Ties:** average rank. **Seeds:** global seed `20261021` (set in config; every random step derives from it).
- **Multiplicity:** primary = fixed sequence; secondary and per-cancer = Benjamini–Hochberg within family.

## 7. Confounder handling [PENDING STEP 5 for full detail]

- **Purity:** TCGA consensus purity estimate (CPE; Aran et al., Nat Commun 2015). CPE partly derives from expression-based estimators, so circularity is possible; sensitivity analyses repeat M3/M5 with each constituent estimator separately `[VERIFY availability]`. For non-TCGA replicate cohorts, an expression-based estimator is used and stated.
- **Subtype:** PDAC basal-like vs. classical; **KRAS, TP53, SMAD4 and CDKN2A** status as covariates in sensitivity analyses (a published supplement reports STYK1 higher in KRAS-, SMAD4- and CDKN2A-mutant TCGA tumors) `[VERIFY availability per cohort]`. COAD: MSI status as a stratifier. Batch/platform: each cohort analyzed separately; cohorts combined only at the level of metrics, never by pooling expression matrices.

## 8. Sample-size / power consideration

- **The statistical unit is the gene, so power depends on K = the number of positives in the universe, not on the number of patients.** K is unknown until the ground-truth lists are frozen and mapped (Step 4).
- **Pre-lock requirement:** run a simulation using the real K and universe size. Negatives ~ N(0,1); positives ~ N(d,1); vary d and the correlation between two methods' scores; estimate the power of the H1 bootstrap test. Report the **minimum detectable ΔAP-lift** for each cancer and state it in the paper instead of claiming "adequate power."
- **Placeholder rule (to be calibrated by that simulation, not accepted as is):** if K < 30 in a cancer, that cancer's per-cancer results are labeled descriptive. `[VERIFY by simulation before lock]`
- **Patient-level counts** (Cox component): record n and number of death events per cohort before lock; keep ≤ 5 covariates in SH_adj. A common heuristic of ≥ 10 events per covariate is a rough guide only.

## 9. Exclusion rules (decided on metadata/QC only, never on performance)

- **Samples:** primary solid tumor for PDAC and COAD; **SKCM metastatic samples only** (avoids mixing primary and metastatic biology) `[VERIFY counts]`; one sample per patient (choose by a fixed, documented barcode rule); PDAC restricted to ductal adenocarcinoma per the cohort's curated histology annotation `[VERIFY]`; samples missing purity or required clinical covariates are excluded **for all methods**.
- **Genes:** outside U (Sec. 3) excluded.
- **No outlier removal** based on results. QC-based removal only, with criteria stated before lock `[FILL QC criteria]`.
- Every exclusion is logged with a count and reason (flow diagram in the paper).

## 10. Single-cell arm (H2, H5) [PENDING STEP 5]

- Public PDAC single-cell/single-nucleus datasets under consideration: Peng et al., Cell Research 2019; Hwang et al., Nature Genetics 2022 `[VERIFY access route and license for each]`. Use the authors' published cell-type annotations; malignant vs. non-malignant epithelial labels taken from the authors' annotation or a pre-specified copy-number method `[FILL]`.
- Analysis at **patient level (pseudobulk)**, not cell level, to avoid pseudoreplication.

## 11. Deviations, amendments and exploratory labeling

- Any change after lock is a **dated amendment** in `AMENDMENTS.md` stating what changed, why, and whether any results had been seen.
- Any analysis not listed above is **exploratory**, labeled in the figure/table title, and its p-values are not interpreted as confirmatory.
- Failed or abandoned analyses are kept in a log, not deleted.

## 12. Pre-lock checklist (all must be ticked before the timestamp)

- [ ] Literature-screen logs complete: STYK1 string (298 hits triaged), benchmark string (all 48 scored; relaxed variant screened), MIDAS and iMLGAM full-text checks done; no paper meets 3-of-4 elements, or amendments made.
- [ ] Ground-truth lists P1–P3, NC2, NC3 frozen with SHA-256 hashes.
- [ ] Immune-marker set frozen.
- [ ] Appendix A cohort table filled (access type, n, events, date checked).
- [ ] Power simulation run; minimum detectable effect recorded.
- [ ] Sections marked [PENDING STEP n] completed.
- [ ] Code skeleton and `environment.yml` committed (no results).
- [ ] Confirmed: no per-gene expression/survival/purity data opened.

---

## Appendix A — Data inventory (fill; do not guess)

| Cancer | Cohort | Source/accession | Platform | n samples | n events | Access (open/controlled) | Date verified |
|---|---|---|---|---|---|---|---|
| PDAC | TCGA-PAAD | [FILL] | | | | | |
| PDAC | external 1–5 | [FILL] | | | | | |
| SKCM | TCGA-SKCM | [FILL] | | | | | |
| SKCM | external ≥ 1 | [FILL] | | | | | |
| COAD | TCGA-COAD | [FILL] | | | | | |
| COAD | external ≥ 1 | [FILL] | | | | | |
| PDAC scRNA/snRNA | [FILL] | | | | | | |

## Appendix B — References to verify (confirm each DOI resolves before citing)

- Aran D, Sirota M, Butte AJ. Systematic pan-cancer analysis of tumour purity. Nat Commun 2015. DOI 10.1038/ncomms9971
- Lawson KA et al. Functional genomic landscape of cancer-intrinsic evasion of killing by T cells. Nature 2020;586:120–126 `[VERIFY DOI]`
- Dubrot J et al. In vivo CRISPR screens reveal the landscape of immune evasion pathways across cancer. Nat Immunol 2022 `[VERIFY DOI]`
- Manguso RT et al. In vivo CRISPR screening identifies Ptpn2 as a cancer immunotherapy target. Nature 2017. DOI 10.1038/nature23270
- Mga in vivo CRISPR screens, PNAS. DOI 10.1073/pnas.2406325121
- Integrative analysis of CRISPR screening data (CTIS). Mol Cancer 2021. DOI 10.1186/s12943-021-01462-z
- Genome Medicine 2022 (aggregated CRISPR datasets). DOI 10.1186/s13073-022-01050-w
- ICB-Portal benchmark. Cancers 2023. DOI 10.3390/cancers15164094
- iMLGAM (ICB-response score; pooled CRISPR screens used to nominate CEP55). iMeta 2025. DOI 10.1002/imt2.70011 (related work; full text read)
- MIDAS (graph neural network for immuno-oncology target discovery). Nat Mach Intell 2026. DOI 10.1038/s42256-026-01201-3 (related work; full text read)
- Peng J et al. Single-cell RNA-seq highlights intra-tumoral heterogeneity and malignant progression in pancreatic ductal adenocarcinoma. Cell Res 2019 `[VERIFY]`
- Hwang WL et al. Single-nucleus and spatial transcriptome profiling of pancreatic cancer. Nat Genet 2022. DOI 10.1038/s41588-022-01134-8
- Reporting: TRIPOD and REMARK checklists (for the survival components) `[VERIFY current versions]`
