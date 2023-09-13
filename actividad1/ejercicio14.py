def mediartimetica(L):
    suma= 0
    con= 0
    for i in range(len(L)):
        con=con + 1
        suma= suma + L[i]
    ma= suma / con
    return ma

