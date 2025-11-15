"""
problema: #35 - Circular Primes
enlace: https://projecteuler.net/problem=35
categoría: 1
"""

def solve():
    """
    encuentra todos los primos circulares menores que 1,000,000
    
    """
    limite = 1_000_000
    
    #usamos la criba de Eratóstenes para encontrar todos los primos
    criba = [True] * limite
    criba[0] = criba[1] = False
    for i in range(2, int(limite**0.5) + 1):
        if criba[i]:
            for j in range(i*i, limite, i):
                criba[j] = False
    
    def es_primo_circular(n):
        """verifica si un número primo es circular"""
        numero_cadena = str(n)
        #generamos todas las rotaciones
        for i in range(len(numero_cadena)):
            rotacion = int(numero_cadena[i:] + numero_cadena[:i])
            if not criba[rotacion]:
                return False
        return True
    
    primos_circulares = []
    
    #verificamos cada número primo
    for numero in range(2, limite):
        if criba[numero] and es_primo_circular(numero):
            primos_circulares.append(numero)
    
    print(f"primos circulares encontrados: {len(primos_circulares)}")
    print(f"ejemplos: {primos_circulares[:20]}...")
    return len(primos_circulares)

if __name__ == "__main__":
    solve()