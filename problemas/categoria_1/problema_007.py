"""
problema: #7 - 10001st Prime
enlace: https://projecteuler.net/problem=7
categoría: 1
"""

import math

def solve():
    """
    encuentra el 10_001vo. número primo usando la Criba de Eratóstenes

    """
    primo_avo = 10001
    
    #estimo un límite superior usando el teorema del número primo
    #para el n-ésimo primo p_n: p_n ≈ n * ln(n) + n * ln(ln(n))
    if primo_avo <= 6:
        limite = 15
    else:
        # Estimación conservadora para n=10001
        limite = int(primo_avo * (math.log(primo_avo) + math.log(math.log(primo_avo)))) + 1000
    
    #la criiba de eratóstenes
    es_primo = [True] * (limite + 1)
    es_primo[0] = es_primo[1] = False
    
    for i in range(2, int(math.sqrt(limite)) + 1):
        if es_primo[i]:
            for j in range(i * i, limite + 1, i):
                es_primo[j] = False
    
    #juntamos todos los primos
    primos = [i for i, primo in enumerate(es_primo) if primo]
    
    if len(primos) >= primo_avo:
        resultado = primos[primo_avo - 1]
        print(f"el numero {primo_avo}_ primo es: {resultado}")
        return resultado
    else:
        print(f"no se encontraron suficientes primos. Solo se encontraron {len(primos)}")
        return None

if __name__ == "__main__":
    solve()
