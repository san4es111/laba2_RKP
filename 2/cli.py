"""Настройка разбора параметров приложения mathtool."""

import argparse

from calc.integration import FUNCTIONS
from calc.series import FORMULAS


def build_parser():
    """Создаёт разборщик команд и их параметров."""
    parser = argparse.ArgumentParser(
        prog="mathtool",
        description="Решение уравнений и обработка числовых рядов.",
        allow_abbrev=False,
    )
    commands = parser.add_subparsers(dest="command")

    solve = commands.add_parser("solve", help="решить уравнение", allow_abbrev=False)
    solve.add_argument("-a", type=int, help="коэффициент A")
    solve.add_argument("-b", type=int, help="коэффициент B")
    solve.add_argument("-c", type=int, help="коэффициент C")

    stats = commands.add_parser("stats", help="показатели последовательности", allow_abbrev=False)
    stats.add_argument("--input", help="файл с числами; без параметра читается stdin")

    series = commands.add_parser("series", help="суммировать ряд", allow_abbrev=False)
    series.add_argument("--func", choices=sorted(FORMULAS), required=True)
    stop = series.add_mutually_exclusive_group(required=True)
    stop.add_argument("--terms", type=int, help="количество слагаемых")
    stop.add_argument("--eps", type=float, help="точность суммирования")

    integrate = commands.add_parser("integrate", help="вычислить интеграл", allow_abbrev=False)
    integrate.add_argument("--func", choices=sorted(FUNCTIONS), required=True)
    integrate.add_argument("--from", dest="start", type=float, required=True, help="нижний предел")
    integrate.add_argument("--to", type=float, required=True, help="верхний предел")
    integrate.add_argument("--steps", type=int, required=True, help="число прямоугольников")
    return parser
