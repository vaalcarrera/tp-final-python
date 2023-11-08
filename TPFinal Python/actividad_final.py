#Importamos el csv
import csv

# 1. Calcular y mostrar la cantidad de votos totales por partido. 

#Diccionario para almacenar el recuento de votos
conteo_votos = {}

print("Cantidad de votos totales por partido.\n")

#Abrimos el archivo csv para la lectura de datos, 'r' = read
with open('votos.csv', 'r') as f:
    reader = csv.DictReader(f)
    #Recorremos cada fila en el csv
    for file in reader:
        partido = file['Voto']
        #Actualizamos el recuento de votos para cada partido en el diccionario
        if partido in conteo_votos:
            conteo_votos[partido] += 1
        else:
            conteo_votos[partido] = 1
#Mostramos la cantidad de votos totales para cada partido.
for partido, votos in conteo_votos.items():
    print(f"{partido} tiene: {votos} votos.")





# 2. Mostrar las personas con DNI mayor a 40,000,000 y con nombre "Juan".

print("")
print("Personas llamadas Juan con DNI superior a 40 millones:")
#Lista para almacenar las personas que cumplen las condiciones
personas = []

#Abrimos el archivo csv para la lectura de datos
with open('votos.csv', 'r') as f:
    reader = csv.DictReader(f)
    #Recorremos cada fila del csv.
    for file in reader:
        dni = int(file['DNI'])
        nombre = file['Nombre'].lower()
        #Verificamos si cumple ambas condiciones
        if dni > 40000000 and nombre == "juan":
            #agregamos la fila entera a la lista.
            personas.append(file)

#Mostramos a las personas que cumplen los criterios; sino, mostramos un mensaje .
if personas:
    for persona in personas:
        print(persona)
else:
    print("No se encontraron personas con DNI mayor a 40 millones y con nombre Juan.")






# 3. Guardar en un archivo de texto las personas que se apellidan "Gonzalez". 

print("")
print("Peronas guardadas en archivo txt.")

#Abrimos el archivo csv para leer los datos
with open('votos.csv', 'r') as f:
    reader = csv.DictReader(f)
    #Abrimos un archivo de texto para escritura, 'w' = write
    with open('gonzalez.txt', 'w') as output_file:
        #Creamos la primera línea del archivo de texto
        output_file.write("Apellido, Nombre, DNI, Voto:\n")
        #Recorremos cada fila en el csv
        for file in reader:
            apellido = file['Apellido']
            #Verificamos si en la fila actual el apellido es Gonzalez y tomamos el resto de los datos
            if apellido == "Gonzalez":
                nombre = file['Nombre']
                apellido = file['Apellido']
                dni = file['DNI']
                voto = file['Voto']
                #Creamos una línea de texto con la información
                linea = f"{apellido}, {nombre}, {dni}, {voto}\n"
                #Escribimos la información en el archivo de texto
                output_file.write(linea)
                #Mostramos en la consola las filas que guardamos en el archivo de texto
                print(file)