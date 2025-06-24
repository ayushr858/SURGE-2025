"""
Neural-network surrogate model for parking synthetic TFBS data.
"""

import torch
import torch.nn as nn

class SurrogateNN(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, output_dim)
        )

    def forward(self, x):
        return self.model(x)

def train_surrogate(model, data_loader, epochs, optimizer, loss_fn):
    """
    Train NN on (α, grid_params) → solution snapshots.
    """
    pass
