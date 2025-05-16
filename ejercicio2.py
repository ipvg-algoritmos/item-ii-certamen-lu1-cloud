# 📝 ejercicio2.py
# 🎓 Promedio de notas
# Puntaje: 12 puntos

# Instrucciones:
# 1. Solicita cuántas notas ingresará el usuario.
# 2. Usa un ciclo para pedir las notas una por una y guárdalas en una lista.
# 3. Calcula el promedio con dos decimales.
# 4. Muestra si el promedio es suficiente para aprobar (4.0 o más) o no.
# 5. Todas las notas deben estar entre 1.0 y 7.0.

# 👇 Aquí comienza tu código
# Paso 1: Solicitar cuántas notas ingresará el usuario
cantidad_notas = int(input("¿Cuántas notas vas a ingresar? "))

notas = []

for i in range(cantidad_notas):
    while True:
       
        nota = float(input(f"Ingrese la nota {i+1}: "))
        if 1.0 <= nota <= 7.0:
            notas.append(nota)
            break
        else:
            print("La nota debe estar entre 1.0 y 7.0. Intenta nuevamente.")

promedio = sum(notas) / len(notas)
promedio = round(promedio, 2)

if promedio >= 4.0:
    print(f"Tu promedio es {promedio}. ¡Aprobaste!")
else:
    print(f"Tu promedio es {promedio}. No aprobaste.")