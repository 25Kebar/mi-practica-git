#Ejercicio  de Python sobre la coca cola
#Valores de las bebidas
Coca_cola = 3450
Powerade = 2940.99
Monster = 3300.99
Agua_ciel = 1200
Jugo_Valle = 2500
Acumu1 = 0
Acumu2 = 0
Acumu3 = 0
Acumu4 = 0
Acumu5 = 0
Acudes1 = 0
Acudes2 = 0
Acudes3 = 0
Acudes4 = 0
Acudes5 = 0
canti = 1
The_shop = input("Ingrese el nombre de la tienda")
while canti != 0:
    print("Bienvenido a la tienda", The_shop)
    print("Ingrese 1 para cliente")
    print("Ingrese 2 para administrador")

    user_admin = input()
    if user_admin == "1":
        print("#####Bebidas disponibles#####")
        print("1. Coca-Cola 1.4L retornable  = $3450")
        print("2. Powerade = $ 2940.99")
        print("3. Monster= $3300.99")
        print("4. Agua Ciel 1L = $1200")
        print("5. Jugos del valle 1.4L = $2500")
        beverages = input()
        if beverages == "1":
                amount = int(input("Ingrese cuantas bebidas va a comprar"))
                if amount > 0:
                    Prices = Coca_cola * amount
                    Acumu1 = Acumu1 + Prices
                    print("El precio total de la Coca-Cola 1.4L retornable es de:", Prices)
                    if Prices > 260000:
                        Discount = Prices * 0.08
                        Desco = Prices-Discount
                        Acudes1 = Acudes1 + Desco
                        print("Su descuento con la bebida es con el 8%, seria:",Desco)
                else:
                    print("No se permiten cantidades negativas")
        elif beverages == "2":
            amount = int(input("Ingrese cuantas bebidas va a comprar"))
            if amount > 0:
                Prices = Powerade * amount
                Acumu2 = Acumu2 + Prices
                print("El precio total del powerade es de:", Prices)
                if Prices > 260000:
                    Discount = Prices * 0.08
                    Desco = Prices-Discount
                    Acudes2 = Acudes2 + Desco
                    print("Su descuento con la bebida es con el 8%, seria:",Desco)
            else:
                print("No se permiten cantidades negativas")
        elif beverages == "3":
            amount = int(input("Ingrese cuantas bebidas va a comprar"))
            if amount > 0:
                Prices = Monster * amount
                Acumu3 = Acumu3 + Prices
                print("El precio total del Monster es de:", Prices)
                if Prices > 260000:
                    Discount = Prices * 0.08
                    Desco = Prices-Discount
                    Acudes3 = Acudes3 + Desco
                    print("Su descuento con la bebida es con el 8%, seria:",Desco)
            else:
                print("No se permiten cantidades negativas")
        elif beverages == "4":
            amount = int(input("Ingrese cuantas bebidas va a comprar"))
            if amount > 0:
                Prices = Agua_ciel * amount
                Acumu4 = Acumu4 + Prices
                print("El precio total del agua cielo 1L es de:", Prices)
                if Prices > 260000:
                    Discount = Prices * 0.08
                    Desco = Prices-Discount
                    Acudes4 = Acudes4 + Desco
                    print("Su descuento con la bebida es con el 8%, seria:",Desco)
            else:
                print("No se permite cantidades negativas")
        elif beverages == "5":
            amount = int(input("Ingrese cuantas bebidas va a comprar"))
            if amount > 0:
                Prices = Jugo_Valle * amount
                Acumu5 = Acumu5 + Prices
                print("El precio total del Jugo del valle 1.4L retornable es de:", Prices)
                if Prices > 260000:
                    Discount = Prices * 0.08
                    Desco = Prices-Discount
                    Acudes5 = Acudes5 + Desco
                    print("Su descuento con la bebida es con el 8%, seria:",Desco)
            else:
                print("No se permiten cantidades negativas")
        else:
            print("Bebida no disponible")
            
    elif user_admin =="2":
        print("Ingrese un numero mayor a 0 si desea ver la cantidad total de las compras y sus descuentos")
        print("Ingrese un numero menor para continuar")
        print("Ingrese el numero 0 para terminar")
        canti = int(input())
        if canti > 0:
            absolute = Acumu1 + Acumu2 + Acumu3 + Acumu4 + Acumu5
            Descounty = Acudes1 + Acudes2 + Acudes3 + Acudes4 + Acudes5
            print("El valor absoluto de las compras de la tienda fue de", absolute)
            print("El valor de las compras con los descuentos fue de:",Descounty)
    else:
        print("Ingrese 1 o 2")
        
    
        
    
        
