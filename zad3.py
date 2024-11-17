from decimal import Decimal


def generuj_liste_decimal(start: float, end: float, step: float):
    start_decimal = Decimal(str(start))
    end_decimal = Decimal(str(end))
    step_decimal = Decimal(str(step))

    liczby = []
    while start_decimal <= end_decimal:
        liczby.append(start_decimal)
        start_decimal += step_decimal

    return liczby


lista = generuj_liste_decimal(2, 5.5, 0.5)
print(lista)
