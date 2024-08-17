from .operacoesAvancadas import potencia


def soma(valor1 : float = 0, valor2: float = 0) -> float:
    return valor1 + valor2

def subtracao(valor1 : float = 0, valor2: float = 0) -> float:
    return valor1 - valor2

def multiplicacao(valor1 : float = 0, valor2: float = 0) -> float:
    return valor1 * valor2

def divisao(valor1 : float = 0, valor2: float = 0) -> float:
    return valor1 / valor2


# teste de importação
print(potencia(3, 3))