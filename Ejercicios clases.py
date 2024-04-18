Nota1 = float(input("Ingrese Nota 1: "))
Nota2 = float(input("Ingrese Nota 2: "))
Nota3 = float(input("Ingrese Nota 3: "))

prom = ((Nota1*0.3) + (Nota2*0.3) + (Nota3*0.4))*0.6
print("Su promedio actual es ", prom)
Examen = float(input("Ingrese su nota del examen: "))
final = prom + (Examen * 0.4)
print("Su promedio final es ", final)

if(final >= 4.0):
    print("Aprobado")
else:
    print("Reprobado")