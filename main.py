import functions as f
#Introduce un numero natural por teclado y recibiras su numero en binario.
def main():
    num = f.validate()
    bin = f.binary(num)
    print(bin)

if __name__ == '__main__':
    main()