"""Суммирование знакочередующихся числовых рядов."""

import math

MAX_TERMS = 10_000
MAX_EPS = 0.0001
MAX_ITERATIONS = 100_000
DIGITS = math.ceil(-math.log10(MAX_EPS))


def sign(n):
    """Возвращает знак n-го слагаемого знакочередующегося ряда."""
    return 1 if n % 2 else -1


def term_sqplus(n):
    """Возвращает n-е слагаемое ряда sqplus."""
    return sign(n) / (n * n + 1)


def term_third(n):
    """Возвращает n-е слагаемое ряда third."""
    return sign(n) / (3 * n)


FORMULAS = {
    "sqplus": (term_sqplus, "S = 1/(1^2+1) - 1/(2^2+1) + 1/(3^2+1) - ..."),
    "third": (term_third, "S = 1/3 - 1/6 + 1/9 - 1/12 + ..."),
}


def sum_by_terms(term, count):
    """Возвращает сумму первых count слагаемых."""
    result = 0.0
    for n in range(1, count + 1):
        result += term(n)
    return result, count


def sum_by_eps(term, eps):
    """Возвращает сумму до первого слагаемого меньше eps и его номер."""
    result = 0.0
    for n in range(1, MAX_ITERATIONS + 1):
        value = term(n)
        result += value
        if abs(value) < eps:
            return result, n
    raise ValueError("точность не достигнута")
