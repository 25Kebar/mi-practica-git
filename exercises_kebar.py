#Ejercicio de python 2
precio=float(input("ingrese el precio de la camisa"))
camisa=int(input("ingrese la cantidad de camisas"))

if camisa >=3:
    preci1=precio*camisa
    discount=preci1*0.20
    total=preci1-discount
    print("valor total", total)
else:
    preci2=precio*camisa
    discount2=preci2*0.10
    total2=preci2-discount2
    print("valor total", total2)
