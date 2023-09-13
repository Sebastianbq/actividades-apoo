def palindromo(pal):
    pal= pal.replace("","").lower()
    if len(pal) <= 1:
        return True
    elif pal [0] == pal [-1]:
        return palindromo(pal[1:-1])
    else:
        return False

def main():
    palabra= str(input("Ingrese palabara: "))
    if palindromo(palabra):
        print("es un palindromo")
    else:
        print("no es un palindromo")
main()