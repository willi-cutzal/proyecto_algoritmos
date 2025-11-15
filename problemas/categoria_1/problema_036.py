"""
problema: #36 - Double-base Palindromes
enlace: https://projecteuler.net/problem=36
categoría: 1
"""

def solve():
    """
    encuentra todos los números < 1,000,000 que son palíndromos en base 10 y base 2
    
    """
    def solve(s):
        """verificamos si un string es palíndromo"""
        return s == s[::-1]
    
    limite = 1000000
    suma_total = 0
    numeros_encontrados = []
    
    #notemos que verificamos solo números impares, ya que los pares en binario terminan en 0, no pueden ser palíndromos
    
    for numero in range(1, limite, 2):  #solo impares
        cadena_decimal = str(numero)
        cadena_binaria = bin(numero)[2:]  #quito el prefjio '0b'
        
        if solve(cadena_decimal) and solve(cadena_binaria):
            numeros_encontrados.append(numero)
            suma_total += numero
    
    print(f"numeros encontrados: {numeros_encontrados}")
    print(f"suma total: {suma_total}")
    return suma_total


if __name__ == "__main__":
    solve()
