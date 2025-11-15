"""
problema: #20 - Factorial Digit Sum
enlace: https://projecteuler.net/problem=20
categoría: 1
"""

def solve():
    
    n = 100
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    
    suma_digitos = sum(int(digito) for digito in str(factorial))
    
    print(f"{n}! tiene {len(str(factorial))} digitos")
    print(f"suma de digitos: {suma_digitos}")
    return suma_digitos


if __name__ == "__main__":
    solve()