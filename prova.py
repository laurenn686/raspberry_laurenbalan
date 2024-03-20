N = int(input("Numero [1-20]: "))

if (N<1 or N>20):
    print(f"ERROR, Numero incorrecte")
else:
    for fila in range(1,N+1):
        for colum in range(1,N-fila+2):
            if (colum == N-fila+1):print(f"* ",end="")
            else: print("   ",end="")
        print()
