año1 = int(input("Ingrese el año de nacimiento de la primera persona: "))
año2 = int(input("Ingrese el año de nacimiento de la segunda persona: "))

años = [año1, año2]

pares = 0
impares = 0
for año in años:
    if año % 2 == 0:
        pares += 1
    else:
        impares += 1

if año1 > 2000 and año2 > 2000:
    print("Grupo Z")

for año in años:
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        print("Tenemos un año especial")

año_actual = 2025
edades = [año_actual - año for año in años]
producto_cartesiano = [(a, e) for a in años for e in edades]

print(f"Años pares: {pares}, Años impares: {impares}")
print("Calculo del producto cartesiano (Año x Edad):", producto_cartesiano)