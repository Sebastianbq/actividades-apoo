def main():
    lis=[1,2,45,6,7,8,9,43,34]
    menor= 100000
    mayor= 0
    for i in range(len(lis)):
        if list[i] > mayor:
            mayor= lis[i]
        if lis[i] < menor:
            menor= lis[i]
    print(f"el mayor es: {mayor} y el menor es: {menor}")
main()
