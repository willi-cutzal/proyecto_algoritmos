"""
problema: #34 - Digit Factorials
enlace: https://projecteuler.net/problem=34
categoría: 1
"""

import math

def solve():
    """
    encuentra todos los números iguales a la suma del factorial de sus dígitos
    
    """
    #calculo facotirales de los digitos 0 a 9
    factoriales = [math.factorial(i) for i in range(10)]
    
    #calcular límite superior
    #para n dígitos, el máximo es n × 9! = n × 362880
    #7 × 362880 = 2540160 < 10000000 (7 dígitos)
    #8 × 362880 = 2903040 > 10000000 (8 dígitos) - imposible
    limite_superior = 7 * factoriales[9]  # 2540160
    
    suma_total = 0
    numeros_encontrados = []
    
    #verificar números desde 10 hasta el límite superior
    for numero in range(10, limite_superior + 1):
        suma_factorial_de_digitos = sum(factoriales[int(d)] for d in str(numero))
        if suma_factorial_de_digitos == numero:
            numeros_encontrados.append(numero)
            suma_total += numero
    
    print(f"numeros encontrados: {numeros_encontrados}")
    print(f"suma total: {suma_total}")
    return suma_total

if __name__ == "__main__":
    solve()