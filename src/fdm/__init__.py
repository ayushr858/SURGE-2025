"""
Finite-Difference Method solver for Time-Fractional Black–Scholes Equation.
"""

import numpy as np
from scipy.special import gamma

def solve(alpha: float, S_max: float, N: int, T: float, M: int):
    """
    Solve the TFBSE using a 2nd-order spatial, 1st-order temporal FDM.
    
    Parameters
    ----------
    alpha : float
        Fractional order in time (0 < alpha ≤ 1).
    S_max : float
        Maximum asset price.
    N : int
        Number of spatial grid points.
    T : float
        Final time.
    M : int
        Number of time steps.
    
    Returns
    -------
    grid : np.ndarray
        Solution grid of shape (N+1, M+1).
    """
    # --- Grid setup ---
    dx = S_max / N
    dt = T / M
    grid = np.zeros((N+1, M+1))
    # ... implement boundary, initial conditions, L1‐scheme in time ...
    return grid
