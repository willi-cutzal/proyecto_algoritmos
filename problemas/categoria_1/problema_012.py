"""
problema: #12 - Highly Divisible Triangular Number
enlace: https://projecteuler.net/problem=12
categoría: 1
"""

import math

def solve():
    objetivo = 500
    n = 1
    triangular = 1
    
    while True:
        #contamos los divisores
        conteo = 0
        raiz_triangular = int(math.sqrt(triangular))
        
        for i in range(1, raiz_triangular + 1):
            if triangular % i == 0:
                conteo += 2  #i  y triangular/i
        
        #ajustamos si es cuadrado perfecto
        if raiz_triangular * raiz_triangular == triangular:
            conteo -= 1
        
        if conteo > objetivo:
            print(f"triangular - T({n}) = {triangular} tiene {conteo} divisores")
            return triangular
        
        n += 1
        triangular += n

if __name__ == "__main__":
    solve()
