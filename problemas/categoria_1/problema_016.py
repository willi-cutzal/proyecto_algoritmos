"""
problema: #16 - Power Digit Sum
enlace: https://projecteuler.net/problem=16
categoría: 1
"""

def solve():
    """
    Solución directa usando la capacidad de Python para enteros grandes.
    Calcula 2^1000 y suma sus dígitos.
    """
    exponente = 1000
    numero = 2 ** exponente
    suma_digitos = sum(int(digit) for digit in str(numero))
    
    print(f"suma de digitos: {suma_digitos}")
    return suma_digitos

if __name__ == "__main__":
    solve()
