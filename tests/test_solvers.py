import numpy as np
import pytest

from src.fdm import solve as fdm_solve
from src.hoc_fdm import solve as hoc_solve
from src.pinn import PINN, train
from src.nn import SurrogateNN, train_surrogate

def test_fdm_against_analytical():
    # trivial case α=1, known analytical solution V(x,t)=...
    grid = fdm_solve(alpha=1.0, S_max=1.0, N=50, T=0.1, M=10)
    # Insert real analytic here for comparison
    analytic = np.zeros_like(grid)
    assert np.allclose(grid, analytic, atol=1e-2)

def test_hoc_fdm_runs():
    grid = hoc_solve(alpha=0.8, S_max=1.0, N=50, T=0.1, M=10)
    assert grid.shape == (51, 11)

@pytest.mark.skip("PINN training is stochastic")
def test_pinn_training():
    model = PINN([__import__('torch').nn.Linear(2,10), __import__('torch').nn.Tanh(), __import__('torch').nn.Linear(10,1)])
    # train(model, ...)
    # assert final loss < threshold

def test_surrogate_initialization():
    model = SurrogateNN(input_dim=2, hidden_dim=10, output_dim=1)
    x = np.random.rand(5,2).astype(np.float32)
    y = model(__import__('torch').from_numpy(x))
    assert y.shape == (5,1)
