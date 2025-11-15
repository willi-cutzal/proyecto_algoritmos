"""
problema: #5 - Smallest Multiple
enlace: https://projecteuler.net/problem=5
categoría: 1
"""

import math

def solve():
    """
    encuentra el mínimo número divisible por todos los números del 1 al 20
    uso el concepto del Mínimo Común Múltiplo (MCM)
    
    """
    def mcm(a, b):
        """Calcula el Mínimo Común Múltiplo usando MCD"""
        return a * b // math.gcd(a, b)
    
    #calculo el  MCM de todos los números del 1 al 20
    resultado = 1
    for i in range(1, 21):
        resultado = mcm(resultado, i)
    
    print(f"el numero mas pequenio divisible por todos los numeros del 1 al 20 es: {resultado}")

if __name__ == "__main__":
    solve()
