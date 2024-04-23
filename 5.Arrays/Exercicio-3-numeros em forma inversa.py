import os;

os.system("cls || clear");

numeros = [];
num:int;

for i in range(6):
    num = int(input(f"Digite o {i + 1}° valor: "));1

    if num < 0 and num %2 == 1:
        print("digite um valor positivo, inteiro, par");
    
    else:
        numeros.append(num);

numeros.reverse();

os.system("cls || clear");

for i in numeros:
    print(i);