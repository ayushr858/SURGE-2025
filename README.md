# SURGE-2025

## Time-Fractional Black–Scholes Merton Equation

This project implements and compares various numerical and machine-learning-based solvers for the Time-Fractional Black–Scholes Equation (TFBSE).

## 📂 Repository Structure

tfbs-solvers/
├── README.md
├── LICENSE
├── environment.yml
├── src/
│ ├── fdm/
│ ├── hoc_fdm/
│ ├── pinn/
│ └── nn/
├── notebooks/
│ ├── 01-FDM.ipynb
│ ├── 02-HOC-FDM.ipynb
│ ├── 03-PINN.ipynb
│ └── 04-NN-surrogate.ipynb
├── results/
│ ├── convergence.csv
│ └── error_vs_alpha.png
├── tests/
│ └── test_solvers.py
├── docs/
└── slides/
