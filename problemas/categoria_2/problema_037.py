"""
problema: #37 - Truncatable Primes
enlace: https://projecteuler.net/problem=37
categoría: 2
complejidad: O(nlogn)
"""

def solve():
    """
    encuentra los 11 primos truncables y calcula su suma
    
    """
    limite = 1_000_000  #considero que este límite es suficiente para encontrar los 11 primos
    
    #criba de Eratóstenes
    criba = [True] * limite
    criba[0] = criba[1] = False
    for i in range(2, int(limite**0.5) + 1):
        if criba[i]:
            for j in range(i*i, limite, i):
                criba[j] = False
    
    def es_primo_truncable(n):
        """verifica si un primo es truncable por izquierda y derecha"""
        if n < 10:  #los primos de un dígito no cuentan
            return False
        
        #verificamos truncamiento por la derecha
        primo_temporal = n
        while primo_temporal > 0:
            if not criba[primo_temporal]:
                return False
            primo_temporal //= 10
        
        #verifico truncamiento por izquierda
        primo_temporal = str(n)
        for i in range(1, len(primo_temporal)):
            if not criba[int(primo_temporal[i:])]:
                return False
        
        return True
    
    primos_truncables = []
    conteo = 0
    
    #busco primos truncables, empezando desde 11, recordemos que los de un dígito no cuentan
    for num in range(11, limite):
        if criba[num] and es_primo_truncable(num):
            primos_truncables.append(num)
            conteo += 1
            if conteo == 11:  #solo hay 11 primos truncables
                break
    
    suma_total = sum(primos_truncables)
    
    print(f"primos truncables encontrados: {primos_truncables}")
    print(f"cantidad: {len(primos_truncables)}")
    print(f"suma total: {suma_total}")
    return suma_total

if __name__ == "__main__":
    solve()