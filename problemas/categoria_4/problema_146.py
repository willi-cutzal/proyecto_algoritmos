"""
problema: #146 - Investigating a Prime Pattern
enlace: https://projecteuler.net/problem=146
categoría: 4
dificultad: x = 50
"""

import math

def solve():
    """
    encuentra la suma de todos los n < 150,000,000 tales que:
    n²+1, n²+3, n²+7, n²+9, n²+13, n²+27 son primos consecutivos

    """
    limite = 150_000_000
    
    def es_primo(n):
        """verifica primalidad"""
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
    
    def vericador_patron(n):
        """verifica el patron de primos para n"""
        n2 = n * n
        primos_por_revisar = [n2 + 1, n2 + 3, n2 + 7, n2 + 9, n2 + 13, n2 + 27]
        
        #verificamos que todos los números requeridos sean primos
        for numero in primos_por_revisar:
            if not es_primo(numero):
                return False
        
        #verificamos que son primos consecutivos, es decir que no hay otros primos entre ellos
        #los números entre n²+1 y n²+27 que NO deben ser primos:
        no_primos = [n2 + 5, n2 + 11, n2 + 15, n2 + 17, n2 + 19, n2 + 21, n2 + 23, n2 + 25]
        
        for numero in no_primos:
            if es_primo(numero):
                return False
        
        return True
    
    suma_total = 0
    contador = 0
    
    #notemos que n debe ser múltiplo de 10, esto es por lo visto en el ejemplo n=10
    for n in range(10, limite, 10):
        if vericador_patron(n):
            suma_total += n
            contador += 1
            print(f"encontrado n = {n} (total encontrados: {contador})")
            
            
    
    print(f"suma total de n válidos: {suma_total}")
    print(f"cantidad de n encontrados: {contador}")
    return suma_total

if __name__ == "__main__":
    solve()