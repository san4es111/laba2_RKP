"""Точка входа: ввод и вывод для команд приложения mathtool."""

import math
import sys

from calc import equation, integration, series, stats
from cli import build_parser

MAX_ABS = 10_000
MAX_COUNT = 20


def read_values(path):
    """Читает числа из файла либо из стандартного ввода и проверяет их."""
    values = []
    if path:
        try:
            with open(path, encoding="utf-8-sig") as handle:
                for line in handle:
                    for word in line.split():
                        try:
                            value = float(word)
                        except ValueError:
                            raise ValueError(f"{word} не является числом") from None
                        values.append(value)
        except OSError:
            raise ValueError("файл не открывается") from None
    else:
        for line in sys.stdin:
            for word in line.split():
                try:
                    value = float(word)
                except ValueError:
                    raise ValueError(f"{word} не является числом") from None
                values.append(value)

    if not values:
        raise ValueError("последовательность пуста")
    if len(values) > MAX_COUNT:
        raise ValueError("чисел больше 20")
    for value in values:
        if not math.isfinite(value):
            raise ValueError("число должно быть конечным")
        if abs(value) > MAX_ABS:
            raise ValueError("число вне допустимого диапазона")
    return values


def handle_solve(args):
    """Проверяет входные коэффициенты, решает уравнение и печатает ответ."""
    supplied = (args.a is not None, args.b is not None, args.c is not None)
    if any(supplied) and not all(supplied):
        raise ValueError("укажите все три коэффициента либо ни одного")
    if not any(supplied):
        try:
            a = int(input("Введите A: "))
            b = int(input("Введите B: "))
            c = int(input("Введите C: "))
        except EOFError:
            raise ValueError("ввод завершён до получения всех коэффициентов") from None
        except ValueError:
            raise ValueError("коэффициент не является целым числом") from None
    else:
        a, b, c = args.a, args.b, args.c

    coefficients = {"A": a, "B": b, "C": c}
    equation.validate_coefficients(coefficients)
    kind, discriminant, roots = equation.solve(a, b, c)
    if kind == "линейное":
        print("Уравнение линейное")
        print(f"x = {roots[0]:.3f}")
        return 0
    print("Уравнение квадратное")
    print(f"D = {discriminant}")
    if len(roots) == 2:
        print(f"x1 = {roots[0]:.3f}")
        print(f"x2 = {roots[1]:.3f}")
    elif len(roots) == 1:
        print(f"x = {roots[0]:.3f}")
    else:
        print("Действительных корней нет")
    return 0


def handle_stats(args):
    """Читает последовательность и печатает показатели из таблицы."""
    values = read_values(args.input)
    print(f"Количество: {len(values)}")
    for label, function, form in stats.REPORT:
        value = function(values)
        if value is None:
            print(f"{label}: НЕ СУЩЕСТВУЕТ")
        else:
            print(f"{label}: {value:{form}}")
    return 0


def handle_series(args):
    """Проверяет параметры, суммирует выбранный ряд и печатает ответ."""
    if args.terms is not None:
        if not 1 <= args.terms <= series.MAX_TERMS:
            raise ValueError("количество слагаемых вне диапазона")
    else:
        if not math.isfinite(args.eps) or not 0 < args.eps <= series.MAX_EPS:
            raise ValueError("точность вне диапазона")

    term, formula = series.FORMULAS[args.func]
    if args.terms is not None:
        result, count = series.sum_by_terms(term, args.terms)
    else:
        result, count = series.sum_by_eps(term, args.eps)
    print(formula)
    print(f"Слагаемых: {count}")
    print(f"Сумма ряда: {result:.{series.DIGITS}f}")
    return 0


def handle_integrate(args):
    """Проверяет пределы, вычисляет и печатает численный интеграл."""
    if not math.isfinite(args.start) or not math.isfinite(args.to):
        raise ValueError("предел должен быть конечным числом")
    if args.start >= args.to:
        raise ValueError("начальный предел не меньше конечного")
    if not 1 <= args.steps <= integration.MAX_STEPS:
        raise ValueError("количество шагов вне диапазона")

    function, formula, low, high, closed = integration.FUNCTIONS[args.func]
    if closed:
        outside = args.start < low or args.start > high or args.to < low or args.to > high
    else:
        outside = args.start <= low or args.start >= high or args.to <= low or args.to >= high
    if outside:
        raise ValueError("предел вне промежутка")

    result = integration.integrate(function, args.start, args.to, args.steps)
    print(formula)
    print(f"Значение интеграла: {result:.4f}")
    return 0


HANDLERS = {
    "solve": handle_solve,
    "stats": handle_stats,
    "series": handle_series,
    "integrate": handle_integrate,
}


def main(argv=None):
    """Разбирает аргументы, вызывает команду и возвращает код завершения."""
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command is None:
        parser.print_help()
        return 0
    try:
        return HANDLERS[args.command](args)
    except (OSError, ValueError) as error:
        print(f"ОШИБКА: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
