"""
problema: #39 - Integer Right Triangles
enlace: https://projecteuler.net/problem=39
categoría: 3 (Solo transpilación)
"""

def solve():
    """
    encuentra el perímetro p ≤ 1000 que maximiza el número de triángulos rectángulos enteros
    
    """
    maximo_soluciones = 0
    mejor_p = 0
    
    for p in range(12, 1001):  # El perímetro mínimo para un triángulo rectángulo es 12
        soluciones = 0
        
        # a y b son los catetos, c es la hipotenusa
        # a + b + c = p, a² + b² = c², a ≤ b < c
        for a in range(1, p // 3):  # a no puede ser mayor que p/3
            #despejo b de las ecuaciones:
            # a + b + c = p  y  a² + b² = c²
            # c = p - a - b
            # a² + b² = (p - a - b)²
            #resolviendo: b = (p² - 2pa) / (2p - 2a)
            numerador = p * p - 2 * p * a
            denominador = 2 * (p - a)
            
            if numerador > 0 and denominador > 0 and numerador % denominador == 0:
                b = numerador // denominador
                c = p - a - b
                
                #verificamos condiciones del triángulo
                if a < b < c and a * a + b * b == c * c:
                    soluciones += 1
        
        if soluciones > maximo_soluciones:
            maximo_soluciones = soluciones
            mejor_p = p
    
    print(f"perimetro con maximo soluciones: p = {mejor_p}")
    print(f"numero de soluciones: {maximo_soluciones}")
    return mejor_p

if __name__ == "__main__":
    solve()
