"""
problema: #25 - 1000-digit Fibonacci Number
enlace: https://projecteuler.net/problem=25
categoría: 1
"""

def solve():
    """
    encuentra el primer número de Fibonacci con 1000 dígitos.
    
    """
    objetivo = 1000
    
    #casos base
    a, b = 1, 1
    indice = 2
    
    #itero  hasta encontrar el número con 1000 dígitos
    while len(str(b)) < objetivo:
        a, b = b, a + b
        indice += 1
    
    print(f"el primer numero de fibonacci con {objetivo} digitos es F({indice})")
    print(f"F({indice}) tiene {len(str(b))} ddgitos")
    return indice

if __name__ == "__main__":
    solve()