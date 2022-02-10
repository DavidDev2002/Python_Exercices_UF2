import functions as f
# Requereix que l’usuari introdueixi un valor natural entre 10 i 5000 (inclosos)
# En cas que no ho faci, li torni a demanar que introdueixi el nombre (fins a un màxim de 3 cops).
# Implementa aquesta funció de validació.
def main():

    num1 = f.validar()
    print(num1)

if __name__ == '__main__':
    main()