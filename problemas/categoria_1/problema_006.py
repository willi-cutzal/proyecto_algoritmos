"""
problema: #6 - Sum Square Difference
enlace: https://projecteuler.net/problem=6
categoría: 1
"""

def solve():
    """
    encuentra la diferencia entre el cuadrado de la suma y la suma de cuadrados
    de los primeros 100 números naturales
    
    """
    limite = 100
    
    #fórmula para la suma de los primeros n números: n(n+1)/2
    suma = limite * (limite + 1) // 2
    cuadrado_de_la_suma = suma ** 2
    
    #fórmula para la suma de cuadrados: n(n+1)(2n+1)/6
    suma_de_cuadrados = limite * (limite + 1) * (2 * limite + 1) // 6
    
    diferencia = cuadrado_de_la_suma - suma_de_cuadrados
    
    print(f"para los primeros {limite} numeros naturales:")
    print(f"suma de cuadrados: {suma_de_cuadrados}")
    print(f"cuadrado de la suma: {cuadrado_de_la_suma}")
    print(f"diferencia: {diferencia}")

if __name__ == "__main__":
    solve()