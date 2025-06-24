# SURGE-2025

## Time-Fractional Black–Scholes Solvers

This repository implements and compares various numerical and machine-learning-based solvers for the Time-Fractional Black–Scholes Equation (TFBSE).

## 📂 Repository Structure

```plaintext
tfbs-solvers/
├── README.md
├── LICENSE
├── environment.yml       ← Conda/Pip dependencies
├── src/                  ← Python packages for each solver
│   ├── fdm/
│   ├── hoc_fdm/
│   ├── pinn/
│   └── nn/
├── notebooks/            ← Executable Jupyter notebooks
│   ├── 01-FDM.ipynb
│   ├── 02-HOC-FDM.ipynb
│   ├── 03-PINN.ipynb
│   └── 04-NN-surrogate.ipynb
├── results/              ← Tables, plots, CSVs
│   ├── convergence.csv
│   └── error_vs_alpha.png
├── tests/                ← Automated unit/integration tests
│   └── test_solvers.py
├── docs/                 ← Built documentation site (Sphinx or MkDocs)
└── slides/               ← Final presentation (PDF or HTML)

