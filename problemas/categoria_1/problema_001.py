"""
problema: #1 - Multiples of 3 or 5
enlace: https://projecteuler.net/problem=1
categoría: 1
complejidad: O(n)
"""


def solve():
    """
    encuentra la suma de todos los múltiplos de 3 o 5 menores que 1000.
    
    """
    limite = 1000
    total = 0 #inicia la suma en cero
    
    #iteramos por todos los números menores que 1000
    for i in range(1, limite):
        #verificamos si es múltiplo de 3 o de 5
        if i % 3 == 0 or i % 5 == 0:
            total += i
            
    
    print(f"la suma de todos los multiplos de 3 o 5 menores que {limite} es: {total}")





if __name__ == "__main__":
    solve()
    