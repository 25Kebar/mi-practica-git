#Ejercicio de cantida de cupos ofrecidos
lista_names1=[]
lista_names2=[]
lista_names3=[]
lista_age1=[]
lista_age2=[]
lista_age3=[]
lista_lastname1=[]
lista_lastname2=[]
lista_lastname3=[]
lista_codig1=[]
lista_codig2=[]
lista_codig3=[]
lista_program1=[]
lista_program2=[]
lista_program3=[]


for i in range (1,3):
    name=input("Ingrese su nombre")
    last_name=input("Ingrese su apellido")
    age=int(input("Ingrese su edad"))
    codig=int(input("Ingrese el codigo"))
    print("Digite 1 si es Análisis y Desarrollo de Sistemas de Información")
    print("Digite 2 si es Técnico en programación")
    print("Digite 3 si es Multimedia")
    program = int(input())
    if program == 1:
        lista_names1.append(name)
        lista_lastname1.append(last_name)
        lista_age1.append(age)
        lista_codig1.append(codig)
        lista_program1.append(program)
    elif program == 2:
        lista_names2.append(name)
        lista_lastname2.append(last_name)
        lista_age2.append(age)
        lista_codig2.append(codig)
        lista_program2.append(program)
    elif program == 3:
        lista_names3.append(name)
        lista_lastname3.append(last_name)
        lista_age3.append(age)
        lista_codig3.append(codig)
        lista_program3.append(program)
    else:
        print("Numero invalido")
program = 12
while program >= 1 or program <= 3:
    print("Digite 1 para Análisis y Desarrollo de Sistemas de Información")
    print("Digite 2 para Técnico en programación")
    print("Digite 3 para Multimedia")
    program2 = int(input())
    if program2 == 1:
        print("Codigos registrados", lista_codig1)
        print("Nombres registrados", lista_names1)
        print("Apellidos registrados", lista_lastname1)
        print("Edades registradas", lista_age1)
        print("Cuantos se registraron", len(lista_program1))
    elif program2 == 2:
        print("Codigos registrados", lista_codig2)
        print("Nombres registrados", lista_names2)
        print("Apellidos registrados", lista_lastname2)
        print("Edades registradas", lista_age2)
        print("Cuantos se registraron", len(lista_program2))
    elif program2 == 3:
        print("Codigos registrados", lista_codig3)
        print("Nombres registrados", lista_names3)
        print("Apellidos registrados", lista_lastname3)
        print("Edades registradas", lista_age3)
        print("Cuantos se registraron", len(lista_program3))
    else:
        print("Numero invalido")

