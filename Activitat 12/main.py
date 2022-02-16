import functions as f
def main():
    size = f.tamaño()
    valors = []
    for x in range(size):
        valors.append(f.validate())
    valors.sort(reverse=bool(True))
    print(valors)
if __name__ == '__main__':
    main()