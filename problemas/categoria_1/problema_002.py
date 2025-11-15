"""
problema: #2 - Even Fibonacci Numbers
enlace: https://projecteuler.net/problem=2
categoría: 1
complejidad: O(n) donde n es el número de términos hasta 4,000,000
"""

def solve():
    """
    encuentra la suma de los terminos pares de Fibonacci menores que 4,000,000.
    
    """
    limite = 4_000_000
    total = 0
    
    #inicio los primeros dos términos de Fibonacci
    a, b = 1, 2
    
    #genero la secuencia sin pasar el límite
    while a <= limite:
        #si el término actual es par, lo sumo a total
        if a % 2 == 0:
            total += a
        
        #calculo el siguiente término de Fibonacci
        a, b = b, a + b
    
    print(f"La suma de los terminos pares de Fibonacci menores que {limite} es: {total}")



if __name__ == "__main__":
    solve()