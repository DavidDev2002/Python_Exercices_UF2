TEXTO_1 = "Introduce un número natural: "
TEXTO_2 = "Introduce un valor entre 1-50: "
def tamaño():
    size = int(input(TEXTO_2))
    while size < 1 or size > 50:
        size = int(input(TEXTO_2))
    return size

def validate():
    num = int(input(TEXTO_1))
    while num < 1:
        num = int(input(TEXTO_1))
    return num