#Edad con condiciones (COndiciones anidadas)
def resta(año1, año2):
    return año1 - año2

AñoActual = int(input("Ingrese el año actual: "))
AñoNacimiento = int(input("Ingrese el año de nacimiento: "))
Edad = resta(AñoActual, AñoNacimiento)
print("Su edad es: ", Edad, " años APROX")
if(Edad >= 18):
    print("Es mayor de edad")
    if(Edad >= 60):
        print("Es un adulto mayor")
else:
    print("Es menor de edad")
    if(Edad <= 4):
        print("Es un bebé")
    elif(Edad <= 12):
        print("Es un niño")
    else:
        print("Es un adolescente")


