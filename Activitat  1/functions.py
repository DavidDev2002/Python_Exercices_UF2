def validar():
    error = "Has introdicido 3 veces valores erroneos"
    num = int(input("Introduce un numero entre 10 y 5000: "))
    i = 0
    while num < 10 or num > 5000:
        num = int(input("Introduce un numero entre 10 y 5000: "))

    return num
