#Ejercicio de la temperatura

lista_Temperature =[]
lista_hot = []
lista_cold = []
lista_templade = []
day = int(input("Ingrese cuantos dias va a anotar la temperatura"))
for i in range (1, day+1):
    print(f"dia{i}")
    degres2= float(input("Ingrese la temperatura maxima"))
    degres1=float(input("Ingrese la temperatura minima"))
    if degres2 > degres1 and degres1 < degres2:
        result = (degres2 + degres1)/2
        lista_Temperature.append(result)
        if result >=0 and result <= 15:
            lista_cold.append(result)
        elif result >= 16 and result <= 26:
            lista_templade.append(result)
        elif result >=27:
            lista_hot.append(result)
    else:
        print("Temperaturas invalidas")
    
print("Temperatura registradas",lista_Temperature) 
print("Temperaturas frias", lista_cold)
print("Temperaturas templadas",lista_templade)
print("Temperaturas calientes",lista_hot)
