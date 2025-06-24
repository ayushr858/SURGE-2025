"""
High-Order Compact FDM solver for TFBSE.
"""

import numpy as np

def solve(alpha: float, S_max: float, N: int, T: float, M: int):
    """
    4th-order accurate in space, (2−α)-order in time HOC scheme.
    """
    # Stub: build tridiagonal systems, implement fractional time derivative...
    return np.zeros((N+1, M+1))
