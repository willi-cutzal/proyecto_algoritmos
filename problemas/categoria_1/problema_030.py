"""
problema: #30 - Digit Fifth Powers
enlace: https://projecteuler.net/problem=30
categoría: 1
"""

def solve():
    """
    encuentra todos los números iguales a la suma de sus dígitos elevados a la 5ta potencia
    
    """
    exponente = 5
    
    #calcular límite superior: el máximo número donde la suma de dígitos^5 podría igualar el número
    #para n dígitos, el máximo es n × 9^5
    #resolvemos: 10^(n-1) <= n × 9^5
    #para n=6: 100000 <= 6 × 59049 = 354294 (sí)
    #para n=7: 1000000 <= 7 × 59049 = 413343 (no)
    limite_superior = 6 * (9 ** exponente)  # 354294
    
    #precalculamos las quintas potencias de los dígitos 0-9
    potencias_digitos = [i ** exponente for i in range(10)]
    
    suma_total = 0
    numeros_encontrados = []
    
    #verificamos todos los números desde 2 hasta el límite superior
    for numero in range(2, limite_superior + 1):
        suma_numero = sum(potencias_digitos[int(d)] for d in str(numero))
        if suma_numero == numero:
            numeros_encontrados.append(numero)
            suma_total += numero
    
    print(f"numeros encontrados: {numeros_encontrados}")
    print(f"suma total: {suma_total}")
    return suma_total

if __name__ == "__main__":
    solve()