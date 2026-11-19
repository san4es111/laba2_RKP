"""Подынтегральные функции и метод левых прямоугольников."""

import math

MAX_STEPS = 100_000


def ratio(x):
    """Возвращает x / (x + 1)."""
    return x / (x + 1)


def root(x):
    """Возвращает квадратный корень из x² + 1."""
    return math.sqrt(x * x + 1)


FUNCTIONS = {
    "ratio": (ratio, "F(x) = x / (x + 1)", 0.0, 20.0, True),
    "root": (root, "F(x) = sqrt(x^2 + 1)", -5.0, 5.0, False),
}


def integrate(function, start, end, steps):
    """Вычисляет интеграл методом левых прямоугольников."""
    dx = (end - start) / steps
    result = 0.0
    for i in range(steps):
        x = start + i * dx
        result += function(x) * dx
    return result
