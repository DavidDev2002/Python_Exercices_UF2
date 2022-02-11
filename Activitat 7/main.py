import functions as f
#
def main():

    total = 0
    notes = []
    size = f.tamaño()
    for i in range(size):
        num1 = f.valor10()
        total += num1
        notes.append(num1)

    max_value = max(notes)
    min_value = min(notes)
    notes.sort()
    mitjana = f.mitjana(total, size)
    print("\nLista ordenada: ", notes)
    print("Mitjana dels valors introduits: ", mitjana)
    print("Valor més gran: ", max_value)
    print("Valor més petit: ", min_value)

if __name__ == '__main__':
    main()