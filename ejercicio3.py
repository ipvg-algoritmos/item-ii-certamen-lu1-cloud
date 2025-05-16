# 📝 ejercicio3.py
# 🔁 Verificador de palíndromos
# Puntaje: 15 puntos

# Instrucciones:
# 1. Solicita al usuario una palabra o frase.
# 2. Crea una función llamada es_palindromo(texto) que:
#    - Convierta el texto a minúsculas
#    - Elimine los espacios
#    - Compare el texto con su reverso
# 3. Muestra si es o no un palíndromo con un mensaje claro.

# 👇 Aquí comienza tu código
def es_palindromo(texto):
    
    texto = texto.replace(" ", "").lower()
    
    if texto == texto[::-1]:
        return True
    else:
        return False

entrada = input("Introduce una palabra o frase para verificar si es un palíndromo: ")

if es_palindromo(entrada):
    print(f"Sí, '{entrada}' es un palíndromo.")
else:
    print(f"No, '{entrada}' no es un palíndromo.")