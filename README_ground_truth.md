# Ground-truth gene lists
Freeze procedure (do before any ranking exists):
1. Save each list as a plain text file named `groundtruth_P1.txt`, `groundtruth_P2.txt`, `groundtruth_P3.txt`, `groundtruth_NC2.txt`, `groundtruth_NC3.txt` (one HGNC symbol per line).
2. Record source table, selection rule, direction convention and ortholog table version in `groundtruth_SOURCES.md`.
3. Run `python make_hashes.py "groundtruth_*.txt" HASHES.txt`, commit, and copy the hashes into the pre-registration.
4. Never edit a list after seeing performance.
