"""
problema: #9 - Special Pythagorean Triplet
enlace: https://projecteuler.net/problem=9
categoría: 1
"""

import math


def solve():
    """
    calcula b a través de la variable a
    ssustituyo a+b+c=1000 en a²+b²=c²
    para encontrar la tripleta pitagórica especial cuya suma es 1000
    
    """
    suma_objetivo = 1000
    
    for a in range(1, suma_objetivo // 3):
        numerador = 500000 - 1000 * a
        denominador = 1000 - a
        
        if denominador > 0 and numerador % denominador == 0:
            b = numerador // denominador
            c = suma_objetivo - a - b
            
            if a < b < c and a**2 + b**2 == c**2:
                producto = a * b * c
                print(f"valores de la tripleta: a={a}, b={b}, c={c}")
                print(f"producto abc: {producto}")
                return producto
    
    return None

if __name__ == "__main__":
    solve()