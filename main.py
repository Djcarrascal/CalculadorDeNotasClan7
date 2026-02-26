print("\nBienvenido a tu calculadora de promedios\n")


input ("Ingese su nombre: ")


maximo = 5.0

while True:
    # Definimos que solo se puedan ingresar numeros
    try:
        print("\nIngrese sus notas obtenidas (ejemplo: 4.5)\n")
        nota1 = float(input("Nota #1: "))
        if nota1 >= 5.1:
            print("La nota no puede ser mayor a 5.0")
            continue
        break
    except ValueError:
        print("\nSolo se pueden ingresar numeros\n")
        continue

while True:
    try: 
        nota2 = float(input("Nota #2: "))
        if nota2 >= 5.1:
            print("La nota no puede ser mayor a 5.0")
            continue
        break
    except ValueError:
        print("\nSolo se pueden ingresar numeros\n")
        continue
        
while True:
    try:
        nota3 = float(input("Nota #3: "))
        if nota3 >= 5.1:
            print("La nota no puede ser mayor a 5.0")
            continue           
        break
    except ValueError:
        print("\nSolo se pueden ingresar numeros\n")
        continue

    


# Ahora hacemos la calculadora de notas
promedio = (nota1 + nota2 + nota3) / (3)

print(f"\nSu promedio de notas fue: {promedio:.1f}\n")

# Mensaje segun el rango de la nota

if promedio < 3.0:
    print("Su promedio es bajo, debe hacer nivelatorio\n")

elif promedio >= 3.0 and promedio <= 4.0:
    print ("Su promedio es bueno, pero puede mejorar\n")

elif promedio >= 4.1:
    print ("Su promedio es sobresaliente. Muy bien!\n")
    







