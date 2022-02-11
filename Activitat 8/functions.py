BASE = "Introduce la base de la potencia: "
EXPO = "Introduce el exponente de la potencia: "
def validate_base():
    num = int(input(BASE))
    while num < 1:
        num = int(input(BASE))
    return num

def validate_expo():
    num = int(input(EXPO))
    while num < 1:
        num = int(input(EXPO))
    return num

def potencia(x,y):
    t = x
    for i in range(y-1):
        t *= x
    return t