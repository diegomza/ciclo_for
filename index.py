# Ejercicio N°1


print("A continuación ingrese 5 valores enteros por favor")
suma = 0

for i in range(5):
    val = int(input(f"Ingrese valor {i+1}: "))
    suma = suma + val
    
print("El resultado de la suma de los valores ingresados es", suma)

# Ejercicio N°2

suma = 0

print("Bienvenido al contador automático")


val_1 = int(input("Desde que numero quiere contar en pantalla?: "))
val_2 = int(input("Hasta que numero quiere contar en pantalla?: "))

for i in range(val_1, (val_2 +1), 1):
    print(i)


# Ejercicio N°3


print("Por favor, a continuación ingrese 10 valores enteros")


val = 0
cont = 0
cont2 = 0
for i in range(10):
    val = int(input(f"Ingrese valor {i+1}: "))
    if val % 2 == 0:
        cont = cont + 1
    else:
        cont2 = cont2 + 1
        
print(f'-Hay {cont} numeros pares')          
print(f'-Hay {cont2} números impares')    
