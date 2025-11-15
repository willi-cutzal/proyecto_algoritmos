"""
problema: #31 - Coin Sums
enlace: https://projecteuler.net/problem=31
categoría: 3 (solo transpilación)
complejidad: O(n x m) donde n es el objetivo y m el número de monedas
"""

def solve():
    """
    calcula el número de formas de formar 200 peniques usando las monedas dadas
    
    """
    objetivo = 200
    monedas = [1, 2, 5, 10, 20, 50, 100, 200]
    
    #inicializo dp[i] = número de formas de formar i peniques
    dp = [0] * (objetivo + 1)
    dp[0] = 1  #una forma de formar 0 peniques: no usar monedas
    
    #para cada moneda, actualizar las formas posibles
    for moneda in monedas:
        for monto in range(moneda, objetivo + 1):
            dp[monto] += dp[monto - moneda]
    
    print(f"formas de formar {objetivo} peniques: {dp[objetivo]}")
    return dp[objetivo]

if __name__ == "__main__":
    solve()
