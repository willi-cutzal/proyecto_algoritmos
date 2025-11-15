"""
problema: #10 - Summation of Primes
enlace: https://projecteuler.net/problem=10
ctegoría: 1
"""

import math

def solve():
    """
    usa la Criba de Eratóstenes para sumar todos los números primos
    menores que 2,000,000 y lo suma
    
    """
    limite = 2000000
    
    #inicio la criba - asumimos que todos son primos inicialmente
    es_primo = [True] * (limite + 1)
    es_primo[0] = es_primo[1] = False
    
    #solo marcar múltiplos de primos hasta √limite
    for i in range(2, int(math.sqrt(limite)) + 1):
        if es_primo[i]:
            #empezamos desde i², los múltiplos menores ya fueron marcados
            for j in range(i * i, limite + 1, i):
                es_primo[j] = False
    

    suma_primos = sum(i for i, primo in enumerate(es_primo) if primo)
    
    print(f"suma de primos menores que {limite}: {suma_primos}")
    return suma_primos

if __name__ == "__main__":
    solve()
