dniA = input("Ingrese el primer DNI: ")
while not dniA.isdigit() or len(dniA) > 8:
    print("El DNI debe ser un número de hasta 8 digitos.")
    dniA = input("Ingresá nuevamente el primer DNI: ")

dniB = input("Ingrese el segundo DNI: ")
while not dniB.isdigit() or len(dniB) > 8:
    print("El DNI debe ser un numero de hasta 8 digitos.")
    dniB = input("Ingrese nuevamente el segundo DNI: ")

conjuntoA = set(dniA)
conjuntoB = set(dniB)

print("Conjunto A:", sorted(conjuntoA))
print("Conjunto B:", sorted(conjuntoB))

print("Union:", sorted(conjuntoA | conjuntoB))
print("Interseccion:", sorted(conjuntoA & conjuntoB))
print("Diferencia (1 - 2):", sorted(conjuntoA - conjuntoB))
print("Diferencia simetrica:", sorted(conjuntoA ^ conjuntoB))

suma1 = sum(int(d) for d in dniA)
suma2 = sum(int(d) for d in dniB)
print("Suma de los digitos del primer DNI:", suma1)
print("Suma de los digitos del segundo DNI:", suma2)

digitos_comunes = conjuntoA & conjuntoB
if digitos_comunes:
    print("Digito compartido:", sorted(digitos_comunes))

if len(conjuntoA) > 6:
    print("Conjunto A: Diversidad numerica alta")
if len(conjuntoB) > 6:
    print("Conjunto B: Diversidad numerica alta")