"""
problema: #14 - Longest Collatz Sequence
enlace: https://projecteuler.net/problem=14
categoría: 1
"""

def solve():
    
    limite = 1_000_000
    
    def longitud_sucesion_collatz(n):
        
        largo = 1
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
            largo += 1
        return largo
    
    longitud_maxima = 0
    numero_inicio = 0
    
    for i in range(1, limite):
        largo = longitud_sucesion_collatz(i)
        if largo > longitud_maxima:
            longitud_maxima = largo
            numero_inicio = i
    
    print(f"calculo (hasta {limite}): {numero_inicio}, longitud: {longitud_maxima}")
    return numero_inicio

if __name__ == "__main__":
    solve()
