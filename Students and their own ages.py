#Ejercicio
lista_name =[]
lista_name2 = []
lista_age =[]
lista_majors =[]

name = "Tame impala"

while name != "0":
    name = input("Ingrese un nombre o cero para terminar")
    if name != "0":
        age =int(input("Ingrese su edad"))
        if age >=0:
            lista_name.append(name)
            lista_age.append(age)
        if age >= 18:
            lista_majors.append(age)
            lista_name2.append(name)
print("Nombres agregados", lista_name)
print("Edades agregadas", lista_age)
print("Nombres agregados de los estudiantes mayores", lista_name2)
print("Edades mayores", sorted(lista_majors, reverse=True))



    
    
