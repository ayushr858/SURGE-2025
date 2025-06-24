# Time-Fractional Black–Scholes Solvers

---

## Motivation
- Standard BS fails for markets with memory
- Fractional derivative accounts for anomalous diffusion

---

## Methods
1. Finite-Difference (FDM)
2. High-Order Compact (HOC-FDM)
3. Physics-Informed NN (PINN)
4. Data-Driven Surrogate NN

---

## Key Results
| Method       | Error |
|--------------|-------|
| FDM          | 2.3e-3|
| HOC-FDM      | 4.1e-5|
| PINN         | 7.8e-4|
| Surrogate NN | 1.2e-3|

*(Convert with Pandoc to PDF or use reveal.js.)*
