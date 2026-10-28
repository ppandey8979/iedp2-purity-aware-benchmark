# IEDP follow-up: purity-aware benchmark of bulk immune-evasion gene ranking

**Status: pre-registration phase. No study data has been opened or analyzed.**

## Question
In PDAC (primary) and melanoma and colorectal cancer (secondary), do purity-adjusted and single-cell-informed bulk-expression rankings recover CRISPR-validated tumor-intrinsic immune-evasion genes better than unadjusted IEDP-style scores and simple baselines? STYK1 is a pre-specified case study.

## Rules of this repository
1. The analysis plan is `preregistration_v0.1_DRAFT.md`. It is locked by git tag `prereg-v1.0` plus an OSF registration. Changes after the tag go in `AMENDMENTS.md`.
2. No per-gene expression, survival or purity data from the study cohorts is opened before the lock.
3. Raw data is never committed. `manifest.csv` records source, access type, checksum and date instead.
4. Every figure and table is produced by code from saved raw outputs. No reconstructed figures.
5. Anything not in the pre-registration is labeled EXPLORATORY.

## Files (flat layout for now)
| File | What it is |
|---|---|
| `preregistration_v0.1_DRAFT.md` | analysis plan (draft until locked) |
| `01_benchmark_string_v3.csv`, `02_relaxed_string.csv`, `03_STYK1_tierA.csv`, `04_STYK1_tierB.csv` | logged literature searches with scoring (see `README_literature_screen.md`) |
| `analysis_log.md` | dated log of what was run and decided |
| `AMENDMENTS.md` | changes after the lock |
| `config.yaml` | seeds and fixed parameters (must match the pre-registration) |
| `environment.yml` | software environment (versions pinned at lock) |
| `manifest.csv` | data manifest (see `README_data.md`) |
| `HASHES.txt`, `make_hashes.py` | frozen ground-truth hashes and the script that makes them (see `README_ground_truth.md`) |

Planned naming for later files: `groundtruth_*.txt` (frozen gene lists), `src_*.py` (code), `results_*.csv` (raw outputs), `nb_*.ipynb` (Colab notebooks). The repository can be reorganized into folders at release.

## Citation and license
Zenodo DOI: TBD at release. License: TBD.
