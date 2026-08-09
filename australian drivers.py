#Ejercicio de la empresa de transporte
lista_names=[]
lista_km=[]
lista_days=["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
lista_total=[]
acumula = 0
name = "0"
while name != " ":
    name=input("Ingrese su nombre o ingrese un espacio para terminar")
    if name != " ":
        for i in lista_days:
            km= float(input(f"Ingrese los kilometros conducidos del dia {i}"))
            lista_km.append(km)
            acumula = acumula + km
        print("Cada kilometro del dia", lista_km)
        print("Kilometros recorridos", acumula)
        lista_names.append(name)
        lista_total.append(acumula)
print("Conductores registrados", lista_names)
print("Total de kilometros recorridos", lista_total) 
        
    
