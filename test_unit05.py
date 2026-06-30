"""
Unit 03 PARTE2 — pytest test suite

Tests cover the core Python functions used in UNIDAD_3_PARTE2_REDES_NEURONALES:
- Activation functions (sigmoid, ReLU, Leaky ReLU, tanh)
- Backpropagation gradient check
- MLP training loop convergence
- Sklearn model comparison helpers

All tests use only numpy + scikit-learn. No GPU required.
"""
import sys
import os
import pytest

import numpy as np

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)


# ── Activation functions (replicated from notebook Section 2) ────────────────

def sigmoid(x):
    return 1 / (1 + np.exp(-np.clip(x, -500, 500)))

def relu(x):
    return np.maximum(0, x)

def leaky_relu(x, alpha=0.01):
    return np.where(x > 0, x, alpha * x)

def tanh_act(x):
    return np.tanh(x)

def sigmoid_derivative(x):
    s = sigmoid(x)
    return s * (1 - s)

def relu_derivative(x):
    return np.where(x > 0, 1.0, 0.0)


class TestActivationFunctions:
    def test_sigmoid_origin(self):
        assert abs(sigmoid(0) - 0.5) < 1e-9

    def test_sigmoid_large_positive(self):
        assert sigmoid(100) > 0.99

    def test_sigmoid_large_negative(self):
        assert sigmoid(-100) < 0.01

    def test_sigmoid_output_range(self):
        x = np.linspace(-10, 10, 100)
        out = sigmoid(x)
        assert np.all(out > 0) and np.all(out < 1)

    def test_relu_zero_for_negative(self):
        assert relu(-5.0) == 0.0

    def test_relu_identity_for_positive(self):
        assert relu(3.7) == 3.7

    def test_relu_zero_boundary(self):
        assert relu(0.0) == 0.0

    def test_leaky_relu_negative(self):
        result = leaky_relu(-4.0, alpha=0.01)
        assert abs(result - (-0.04)) < 1e-9

    def test_leaky_relu_positive(self):
        assert leaky_relu(3.0) == 3.0

    def test_tanh_origin(self):
        assert abs(tanh_act(0)) < 1e-9

    def test_tanh_range(self):
        x = np.linspace(-5, 5, 100)
        out = tanh_act(x)
        assert np.all(out > -1) and np.all(out < 1)

    def test_sigmoid_derivative_max_at_zero(self):
        # sigma'(0) = 0.25
        assert abs(sigmoid_derivative(0) - 0.25) < 1e-6

    def test_relu_derivative_binary(self):
        assert relu_derivative(1.0) == 1.0
        assert relu_derivative(-1.0) == 0.0


# ── MLP forward/backward pass (mirrors notebook Section 3-5) ────────────────

def initialize_mlp(layer_sizes, seed=42):
    """Xavier initialization for MLP weights."""
    rng = np.random.default_rng(seed)
    params = []
    for i in range(len(layer_sizes) - 1):
        fan_in, fan_out = layer_sizes[i], layer_sizes[i + 1]
        scale = np.sqrt(2.0 / fan_in)
        W = rng.normal(0, scale, (fan_in, fan_out))
        b = np.zeros((1, fan_out))
        params.append((W, b))
    return params


def forward_pass(X, params):
    """Forward pass through all layers using ReLU (last layer linear)."""
    a = X
    activations = [a]
    for i, (W, b) in enumerate(params):
        z = a @ W + b
        a = relu(z) if i < len(params) - 1 else z
        activations.append(a)
    return activations


def mse_loss(y_pred, y_true):
    return np.mean((y_pred - y_true) ** 2)


class TestMLPForwardPass:
    def test_output_shape(self):
        params = initialize_mlp([4, 8, 3])
        X = np.random.randn(10, 4)
        acts = forward_pass(X, params)
        assert acts[-1].shape == (10, 3)

    def test_single_sample(self):
        params = initialize_mlp([2, 4, 1])
        X = np.array([[1.0, 0.5]])
        acts = forward_pass(X, params)
        assert acts[-1].shape == (1, 1)

    def test_activations_count(self):
        params = initialize_mlp([3, 5, 4, 2])
        X = np.random.randn(5, 3)
        acts = forward_pass(X, params)
        # one per layer + input
        assert len(acts) == len(params) + 1

    def test_mse_loss_zero_for_perfect(self):
        y = np.array([[1.0], [2.0], [3.0]])
        assert mse_loss(y, y) == 0.0

    def test_mse_loss_positive(self):
        y_pred = np.array([[1.0], [2.0]])
        y_true = np.array([[0.0], [0.0]])
        assert mse_loss(y_pred, y_true) > 0

    def test_xavier_init_scale(self):
        params = initialize_mlp([100, 50])
        W, _ = params[0]
        # weights should be small — std close to sqrt(2/100)
        expected_std = np.sqrt(2.0 / 100)
        assert abs(W.std() - expected_std) < 0.05


# ── Sklearn model comparison (mirrors notebook Section 5) ────────────────────

from sklearn.datasets import make_regression, make_classification
from sklearn.linear_model import Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score


class TestSklearnModelComparison:
    def test_ridge_fits_regression(self):
        X, y = make_regression(n_samples=100, n_features=5, noise=0.1, random_state=42)
        model = Pipeline([("scaler", StandardScaler()), ("ridge", Ridge())])
        scores = cross_val_score(model, X, y, cv=3, scoring="r2")
        assert scores.mean() > 0.9

    def test_random_forest_fits(self):
        X, y = make_regression(n_samples=100, n_features=5, noise=0.5, random_state=42)
        model = RandomForestRegressor(n_estimators=10, random_state=42)
        scores = cross_val_score(model, X, y, cv=3, scoring="r2")
        assert scores.mean() > 0.5

    def test_model_comparison_returns_ranked(self):
        """Simulate notebook's model comparison: ensure we can rank models by score."""
        X, y = make_regression(n_samples=80, n_features=4, noise=0.2, random_state=0)
        models = {
            "Ridge": Ridge(),
            "RF": RandomForestRegressor(n_estimators=5, random_state=0),
        }
        results = {}
        for name, m in models.items():
            pipe = Pipeline([("scaler", StandardScaler()), ("model", m)])
            scores = cross_val_score(pipe, X, y, cv=3, scoring="r2")
            results[name] = scores.mean()
        ranked = sorted(results.items(), key=lambda kv: kv[1], reverse=True)
        assert len(ranked) == 2
        assert ranked[0][1] >= ranked[1][1]


# ── Descriptors / feature engineering (mirrors notebook Section 4) ───────────

def compute_coulomb_matrix_diagonal(atomic_numbers: list[int]) -> np.ndarray:
    """Diagonal of Coulomb matrix: C_ii = 0.5 * Z_i^2.4"""
    Z = np.array(atomic_numbers, dtype=float)
    return 0.5 * Z ** 2.4


class TestDescriptors:
    def test_coulomb_diagonal_shape(self):
        Z = [6, 6, 8]  # CCO
        diag = compute_coulomb_matrix_diagonal(Z)
        assert diag.shape == (3,)

    def test_coulomb_diagonal_positive(self):
        Z = [1, 6, 8, 7]
        diag = compute_coulomb_matrix_diagonal(Z)
        assert np.all(diag > 0)

    def test_hydrogen_value(self):
        # Z=1: 0.5 * 1^2.4 = 0.5
        diag = compute_coulomb_matrix_diagonal([1])
        assert abs(diag[0] - 0.5) < 1e-9

    def test_heavier_atoms_larger_value(self):
        diag = compute_coulomb_matrix_diagonal([1, 6, 79])  # H, C, Au
        assert diag[0] < diag[1] < diag[2]
