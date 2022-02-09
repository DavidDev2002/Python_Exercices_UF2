def validate():
    num = int(input("Introduce un número natural: "))
    while num < 1:
        num = int(input("Introduce un número natural: "))
    return num

def binary(num):
    count = 1
    binario = 0
    while num != 0:
        rem = num % 2
        num = num // 2
        binario = binario + (rem * count)
        count = count * 10
    return binario
