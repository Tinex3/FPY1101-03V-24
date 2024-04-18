User = ["Pedro","Angel"]
password = ["1234","a4s1"]


def login():
    user = input("Introduce tu usuario: ")
    passw = input("Introduce tu contraseña: ")
    if user in User and passw in password:
        print("Bienvenido")
    else:
        print("Usuario o contraseña incorrectos")
        
a = login()