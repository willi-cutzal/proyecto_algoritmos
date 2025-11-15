"""
problema: #28 - Number Spiral Diagonals
enlace: https://projecteuler.net/problem=28
categoría: 1
"""

def solve():
    """
    calcula la suma de las diagonales en una espiral numérica nxn.
    
    """
    tamanio_espiral = 1001  # Tamaño de la espiral (debe ser impar)
    
    total = 1  # Empezar con el centro (1)
    
    #para cada 'capa' de la espiral (desde la capa 1 hasta (n-1)/2)
    for capa in range(1, (tamanio_espiral // 2) + 1):
        tamanio_del_lado = 2 * capa + 1  #tamaño del lado de esta capa
        
        #veamos que los 4 números en las esquinas de esta capa siguen un patrón:
        #esquina superior derecha: (2k+1)²
        #esquina superior izquierda: (2k+1)² - 2k
        #esquina inferior izquierda: (2k+1)² - 4k  
        #esquina inferior derecha: (2k+1)² - 6k
        
        esquina_superior_derecha = (2 * capa + 1) ** 2
        esquina_superior_izquierda = esquina_superior_derecha - 2 * capa
        esquina_inferior_izquierda = esquina_superior_derecha - 4 * capa
        esquina_inferior_derecha = esquina_superior_derecha - 6 * capa
        
        total += esquina_superior_derecha + esquina_superior_izquierda + esquina_inferior_izquierda + esquina_inferior_derecha
    
    print(f"suma de diagonales en espiral {tamanio_espiral} x {tamanio_espiral}: {total}")
    return total

if __name__ == "__main__":
    solve()