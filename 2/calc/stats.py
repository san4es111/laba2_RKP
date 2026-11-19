"""Отдельные функции для показателей последовательности чисел."""

import math


def total(values):
    """Возвращает сумму чисел."""
    result = 0.0
    for value in values:
        result += value
    return result


def mean(values):
    """Возвращает среднее арифметическое."""
    return total(values) / len(values)


def sum_squares(values):
    """Возвращает сумму квадратов чисел."""
    result = 0.0
    for value in values:
        result += value * value
    return result


def root_mean_square(values):
    """Возвращает среднее квадратическое."""
    return math.sqrt(sum_squares(values) / len(values))


def squared_deviations(values):
    """Возвращает сумму квадратов отклонений от среднего."""
    average = mean(values)
    result = 0.0
    for value in values:
        result += (value - average) ** 2
    return result


def variance(values):
    """Возвращает дисперсию с делителем N."""
    return squared_deviations(values) / len(values)


def standard_error(values):
    """Возвращает СКО с делителем N."""
    return math.sqrt(variance(values))


def sample_standard_deviation(values):
    """Возвращает стандартное отклонение с делителем N − 1 или None."""
    if len(values) < 2:
        return None
    return math.sqrt(squared_deviations(values) / (len(values) - 1))


def minimum(values):
    """Возвращает наименьшее значение."""
    result = values[0]
    for value in values:
        if value < result:
            result = value
    return result


def maximum(values):
    """Возвращает наибольшее значение."""
    result = values[0]
    for value in values:
        if value > result:
            result = value
    return result


def positive_count(values):
    """Возвращает количество положительных чисел."""
    result = 0
    for value in values:
        if value > 0:
            result += 1
    return result


def negative_count(values):
    """Возвращает количество отрицательных чисел."""
    result = 0
    for value in values:
        if value < 0:
            result += 1
    return result


REPORT = [
    ("Сумма", total, ".3f"),
    ("Ср. арифм.", mean, ".3f"),
    ("Сумма кв.", sum_squares, ".3f"),
    ("Ср. кв.", root_mean_square, ".3f"),
    ("Дисперсия", variance, ".3f"),
    ("СКО", standard_error, ".3f"),
    ("Станд. откл.", sample_standard_deviation, ".3f"),
    ("Наименьшее", minimum, ".3f"),
    ("Наибольшее", maximum, ".3f"),
    ("Положительных", positive_count, "d"),
    ("Отрицательных", negative_count, "d"),
]
