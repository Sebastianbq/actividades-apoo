def main():
    import random
    fila=5
    colum=5
    matriz=[]
    for f in range(fila):
        matriz.append([0] * colum)
    for f in range(fila):
        for c in range(colum):
            dato= random.randint(1,100)
            matriz[f][c]= dato
    for f in range(fila):
        for c in range(colum):
            print(matriz[f][c],end="\t")
        print("\n")
main()
