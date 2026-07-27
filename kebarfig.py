# Inicializar los tres mejores tiempos (promedios)
primer_tiempo = 999
segundo_tiempo = 999
tercer_tiempo = 999

primer_nombre = ""
primer_pais = ""

segundo_nombre = ""
segundo_pais = ""

tercer_nombre = ""
tercer_pais = ""

# los 5 atletas
for atleta in range(1, 6):

    print(f"ATLETA {atleta}")

    nombre = input("Nombre del atleta: ")
    pais = input("País: ")

    suma = 0

    # las 5 pruebas
    for prueba in range(1, 6):

        tiempo = float(input(f"Tiempo de la prueba {prueba} (min): "))

        if tiempo <= 15:
            print("Resultado: APTO")
        else:
            print("Resultado: NO APTO")

        suma += tiempo

    promedio = suma / 5

    print(f"Promedio del atleta: {promedio:.2f} minutos")

    # Comparar el podio
    if promedio < primer_tiempo:

        tercer_tiempo = segundo_tiempo
        tercer_nombre = segundo_nombre
        tercer_pais = segundo_pais

        segundo_tiempo = primer_tiempo
        segundo_nombre = primer_nombre
        segundo_pais = primer_pais

        primer_tiempo = promedio
        primer_nombre = nombre
        primer_pais = pais

    elif promedio < segundo_tiempo:

        tercer_tiempo = segundo_tiempo
        tercer_nombre = segundo_nombre
        tercer_pais = segundo_pais

        segundo_tiempo = promedio
        segundo_nombre = nombre
        segundo_pais = pais

    elif promedio < tercer_tiempo:

        tercer_tiempo = promedio
        tercer_nombre = nombre
        tercer_pais = pais

# Mostrar resultados finales
print(" PODIO ")

print("Primer lugar")
print("Nombre:", primer_nombre)
print("País:", primer_pais)
print("Promedio:", round(primer_tiempo, 2), "min")

print("Segundo lugar")
print("Nombre:", segundo_nombre)
print("País:", segundo_pais)
print("Promedio:", round(segundo_tiempo, 2), "min")

print("Tercer lugar")
print("Nombre:", tercer_nombre)
print("País:", tercer_pais)
print("Promedio:", round(tercer_tiempo, 2), "min")    

    
    

