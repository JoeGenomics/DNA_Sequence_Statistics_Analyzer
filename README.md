![Python](https://img.shields.io/badge/Python-3.x-blue)
![Biopython](https://img.shields.io/badge/Biopython-enabled-brightgreen)
![Status](https://img.shields.io/badge/Project-active-success)

# 🧬 DNA Sequence Statistics Analyzer

# DNA_Sequence_Statistics_Analyzer
A Python-based tool for calculating length, base composition, GC and AT content from FASTA sequences

OVERVIEW
> This project is a Python-based bioinformatics tool designed to calculate detailed nucleotide statistics from DNA sequences stored in FASTA format.
The current version analyzes the hemagglutinin (HA) gene of Influenza A (H1N1) and computes:
- Total sequence length
- Counts of each nucleotide (A, T, G, C)
- GC content (%)
- AT content (%)
These metrics are essential in genome characterization, viral evolution studies, and comparative genomics.

## PURPOSE
The goal of this project is to compute nucleotide composition and GC/AT content of the Influenza A (H1N1) HA gene.
These metrics provide insight into viral sequence characteristics and can be used to study genome stability and variation across strains.

## Dataset Information
| Attribute | Details |
|----------|---------|
| Organism | Influenza A virus |
| Strain | A/California/07/2009 (H1N1) |
| Gene | Hemagglutinin (HA), segment 4 |
| GenBank Accession | CY121680.1 |
| Source | NCBI Influenza Virus Resource |
| FASTA file | `example.fasta` |

---

## Dependencies
| Software | Version |
|----------|---------|
| Python | 3.x |
| Biopython | latest |


## How to Run
Run the script from the terminal:

```bash
python dna_stats.py example.fasta
```


### Example Output
```
Sequence ID: CY121680.1
Length: 1320
A: 270
T: 371
G: 458
C: 221
GC Content: 51.44 %
AT Content: 48.56 %
```


## Interpretation
- The HA gene of this strain contains 1320 nucleotides
- GC content (51.44%) is slightly higher than AT content (48.56%)
- Moderate GC enrichment implies good structural stability of the HA segment

## Such statistics may assist in:
- Viral strain comparison, Protein expression efficiency prediction
- Primer design for PCR
- Vaccine development studies

## Contributions
Contributions and feature suggestions are welcome.
Fork this repository and submit a pull request anytime.

📄 License
This project is open-source and free to use for research and education.
