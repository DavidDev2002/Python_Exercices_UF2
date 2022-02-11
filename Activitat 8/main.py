import functions as f
# Dissenya una funció que, donats dos nombres naturals (x,y) retorni xy.
def main():
    num1 = f.validate_base()
    num2 = f.validate_expo()
    print(f.potencia(num1,num2))

if __name__ == '__main__':
    main()