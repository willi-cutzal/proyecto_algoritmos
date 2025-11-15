"""
problema: #41 - Pandigital Prime
enlace: https://projecteuler.net/problem=41
categoría: 2
complejidad: O(n)
"""

import math
from itertools import permutations

def solve():
    """
    encuentra el primo pandigital más grande.
    
    """
    def es_primo(n):
        """verifica si un número es primo"""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True
    
    #notemos que los números pandigitales de 8 y 9 dígitos 
    #son divisibles por 3 (suma de dígitos me daría = 36 y 45, ambos divisibles por 3)
    #por lo que, no pueden ser primos. Así que empezamos desde 7 dígitos
    
    primo_pandigital_mas_grande = 0
    
    #probamos desde pandigitales de 7 dígitos hacia abajo
    for n in range(7, 0, -1):
        digitos = ''.join(str(i) for i in range(1, n + 1))
        
        #generamos permutaciones en orden descendente
        permutaciones = permutations(digitos)
        pandigital = sorted([int(''.join(p)) for p in permutaciones], reverse=True)
        
        for numero in pandigital:
            if es_primo(numero):
    
                primo_pandigital_mas_grande = numero
                break
        
        if primo_pandigital_mas_grande > 0:
            break
    
    print(f"el primo pandigital mas grande es: {primo_pandigital_mas_grande}")
    print(f"tiene {len(str(primo_pandigital_mas_grande))} digitos")
    return primo_pandigital_mas_grande

if __name__ == "__main__":
    solve()