#Python exercises
Not1= float(input("Ingrese la nota del parcial 1"))
Not2= float(input("Ingrese la nota del parcial 2"))


prom1 = Not1 * 0.30
prom2 = Not2 * 0.30


result= (prom1 + prom2) 

if result <2.0:
    print("El estudiante no puede presentar el examen y pierde la materia por bajo rendimiento")
    print("El promedio fue de:",result)
elif result >= 2.0:
    print("Presenta el examen final")
    Not3= float(input("Ingrese la nota del examen final"))
    if Not3 < 2.0:
        print("Se desconoce las notas parciales por lo su nota es con el examen final de:", Not3)
    elif Not3 >= 2.0 and Not3 <= 2.9:
        prom3 = Not3 * 0.40
        NoteDef = prom1+prom2+prom3
        print("Su nota definitiva es de ", NoteDef)
        if NoteDef >=3.0:
            print("Aprueba la asignatura")
        else:
            print("pierde la asignatura, pero la habilita")
            Habili= float(input("ingrese la nota de la habilitacion"))
            if Habili >= 2.0:
                print("Aprueba la habilitacion")
            else:
                print("Desaprobo la habilitacion")
    else:
        print("aprobo")
else:
    print("Promedio no valido")




