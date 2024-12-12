import random as r, string as s

elements = s.ascii_letters + s.ascii_lowercase + s.ascii_uppercase + s.punctuation + s.punctuation + s.digits
longitud = int(input("Que tan larga sera la contraseña?"))
#|---------------------------Codigo-----------------------------|
contrasenas = ""
for i in range(longitud):
    contrasenas += r.choice(elements)
print(contrasenas)