def generator_kodow_pocztowych(start: str, end: str):
    lista_kodow = []
    start_numer = int(start.replace("-", ""))
    end_numer = int(end.replace("-", ""))

    for kod in range(start_numer, end_numer + 1):
        kod_string = f"{kod:05d}"  # Formatowanie z zerami wiodącymi
        lista_kodow.append(f"{kod_string[:2]}-{kod_string[2:]}")

    return lista_kodow


kody = generator_kodow_pocztowych("79-900", "80-155")
print(kody)
