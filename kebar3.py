#Python exercises 3
secret = 10

print("intento numero 1")
number = int(input("Ingrese el numero"))
if number < secret:
    print("El numero es menor")#primer intento
    number2 = int(input("Ingrese el segundo numero"))#segundo intento
    if number2 < secret:
        print("El numero es menor")
        number2 = int(input("Ingrese el tercer numero"))#tercer intento
        if number2 < secret:
             print("El numero es menor")
        elif number2 > secret:
            print("El numero es mayor")
        else:
            print("Encontraste el numero secreto")
    elif number2 > secret:
        print("El numero es mayor al numero secreto")
        number6 = int(input("Ingrese el tercer numero")) 
        if number6 < secret:
             print("El numero es menor")
        elif number6 > secret:
            print("El numero es mayor")
        else:
            print("Encontraste el numero secreto")
    else:
        print("Encontraste el numero secreto")
elif number > secret:
    print("El numero es mayor")
    number3 = int(input("Ingrese el segundo numero"))
    if number3 < secret:
        print("El numero es menor")
        number4 = int(input("Ingrese el tercer numero"))
        if number4 < secret:
             print("El numero es menor")
        elif number4 > secret:
            print("El numero es mayor")
        else:
            print("Encontraste el numero secreto")
    elif number3 > secret:
        print("El numero es mayor al numero secreto")
        number5 = int(input("Ingrese el tercer numero"))
        if number5 < secret:
             print("El numero es menor")
        elif number5 > secret:
            print("El numero es mayor")
        else:
            print("Encontraste el numero secreto")
    else:
        print("Encontraste el numero secreto")
else:
    print("Encontraste el numero secreto")
    
        
