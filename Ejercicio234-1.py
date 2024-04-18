
Animales = ["Perro","Cocodrilo","Conejo","TIburon"]
def lista():
    for i in range(len(Animales)):
        print(i,"",Animales[i])
def Buscador(Animal_ELecto):
    puntos = 0.0
    if(Animales[Animal_ELecto] == Animales[3]):
        puntos += 1.0
        return puntos
    elif(Animales[Animal_ELecto] == Animales[1]):
        print ("aqui")
        puntos += 0.5
        return puntos
    else:
        puntos += 0.0
    


print("CUal de los siguientes animales Viven en el agua")
imprimir = lista()


a = int(input("Ingrese el numero del animal: "))
print (a)
print(Animales[a])
b = float(Buscador(a))
print (b)

match b:
    case 1:
        print("Correcto")
    case 0:
        print("Incorrecto")
    case 0.5:
        print("Casi")
    case _:
        print("Error")