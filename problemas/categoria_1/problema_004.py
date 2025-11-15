"""
problema: #4 - Largest Palindrome Product
enlace: https://projecteuler.net/problem=4
categoría: 1
"""

def solve():
    """
    prueba todos los productos posibles.
    
    """
    maximo_palindromo = 0
    factores = (0, 0)
    
    for i in range(999, 99, -1):
        for j in range(i, 99, -1):  # j desde i para evitar duplicados
            producto = i * j
            if producto <= maximo_palindromo:
                break  #no puede encontrar uno mayor en esta fila
            
            #verificamos que si es palíndromo
            producto_str = str(producto)
            if producto_str == producto_str[::-1]:
                if producto > maximo_palindromo:
                    maximo_palindromo = producto
                    factores = (i, j)
    
    print(f"{maximo_palindromo} = {factores[0]} x {factores[1]}")
    return maximo_palindromo

if __name__ == "__main__":
    solve()
