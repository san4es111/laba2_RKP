"""Проверка коэффициентов и решение линейных и квадратных уравнений."""

import math

MAX_VALUE = 10_000


def validate_coefficients(coefficients):
    """Проверяет диапазон коэффициентов и наличие неизвестной."""
    for name, value in coefficients.items():
        if abs(value) > MAX_VALUE:
            raise ValueError(f"коэффициент {name} вне допустимого диапазона")
    if coefficients["A"] == 0 and coefficients["B"] == 0:
        raise ValueError("это не уравнение, неизвестное отсутствует")


def solve(a, b, c):
    """Возвращает вид уравнения, дискриминант и список действительных корней."""
    if a == 0:
        return "линейное", None, [-c / b]
    discriminant = b * b - 4 * a * c
    if discriminant > 0:
        root = math.sqrt(discriminant)
        return "квадратное", discriminant, [(-b + root) / (2 * a), (-b - root) / (2 * a)]
    if discriminant == 0:
        return "квадратное", discriminant, [-b / (2 * a)]
    return "квадратное", discriminant, []
