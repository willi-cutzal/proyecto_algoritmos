"""
problema: #3 - Largest Prime Factor
enlace: https://projecteuler.net/problem=3
categoría: 1
"""

def solve():
    """
    encuentra el mayor factor primo del número 600851475143

    """
    primo = 600851475143
    mayor_factor_primo = 1
    
    #divido por 2 mientras sea posible
    while primo % 2 == 0:
        mayor_factor_primo = 2
        primo //= 2
    
    #la variable primo debe ser impar ahora, pruebo divisores impares
    factor = 3
    while factor * factor <= primo:
        while primo % factor == 0:
            mayor_factor_primo = factor
            primo //= factor
        factor += 2
    
    # Si n es mayor que 2, entonces n es primo
    if primo > 2:
        mayor_factor_primo = primo
    
    print(f"el mayor factor primo de 6000851475143 es: {mayor_factor_primo}")

if __name__ == "__main__":
    solve()
