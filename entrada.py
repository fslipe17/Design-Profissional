"""Funcoes auxiliares para ler e validar dados digitados pelo usuario."""


def ler_texto(mensagem):
    while True:
        valor = input(mensagem).strip()
        if valor:
            return valor
        print("Valor invalido: o campo nao pode ficar vazio.")


def ler_inteiro(mensagem, minimo=None, maximo=None):
    while True:
        try:
            valor = int(input(mensagem).strip())
        except ValueError:
            print("Valor invalido: digite um numero inteiro.")
            continue
        if minimo is not None and valor < minimo:
            print(f"Valor invalido: o minimo permitido e {minimo}.")
        elif maximo is not None and valor > maximo:
            print(f"Valor invalido: o maximo permitido e {maximo}.")
        else:
            return valor


def ler_decimal(mensagem, minimo=0.01):
    while True:
        try:
            valor = float(input(mensagem).strip().replace(",", "."))
        except ValueError:
            print("Valor invalido: digite um numero (ex.: 19,90).")
            continue
        if valor < minimo:
            print(f"Valor invalido: o minimo permitido e {minimo}.")
        else:
            return valor


def formatar_preco(valor):
    return f"R$ {valor:.2f}".replace(".", ",")
