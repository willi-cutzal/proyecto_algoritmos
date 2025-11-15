"""
problema: #17 - Number Letter Counts
enlace: https://projecteuler.net/problem=17
categoría: 1
"""

def solve():
    #palabras para números básicos
    primeros_veinte = [
        "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
        "seventeen", "eighteen", "nineteen"
    ]
    
    decenas = [
        "", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", 
        "eighty", "ninety"
    ]
    
    def numero_palabras(n):
        
        """
        convierte un número a su representación en palabras sin espacios ni guiones
        
        """
        if n == 0:
            return "zero"
        if n < 20:
            return primeros_veinte[n]
        elif n < 100:
            decena = decenas[n // 10]
            unidades = primeros_veinte[n % 10]
            return decena + unidades if unidades == "" else decena + unidades
        elif n < 1000:
            centena = primeros_veinte[n // 100] + "hundred"
            residuo = n % 100
            if residuo == 0:
                return centena
            else:
                return centena + "and" + numero_palabras(residuo)
        elif n == 1000:
            return "onethousand"
        else:
            return ""
    
    total_letras = 0
    for i in range(1, 1001):
        palabras = numero_palabras(i)
        total_letras += len(palabras)
    
    print(f"total de letras para numeros del 1 al 1000: {total_letras}")
    return total_letras

if __name__ == "__main__":
    solve()