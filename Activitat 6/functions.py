TEXTO = "Introduce un número: "
def suma():
    num = int(input(TEXTO))
    resultado, suma = 0, 0
    while num < 0:
        num = int(input(TEXTO))
    while num >= resultado + suma:
        resultado = suma + resultado
        print(suma, "<---->", resultado)
        suma += 1
