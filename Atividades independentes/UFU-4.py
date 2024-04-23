#Fac¸a um programa que leia um vetor de 8 posic¸oes e, em seguida, leia tamb ˜ em dois va- ´
#lores X e Y quaisquer correspondentes a duas posic¸oes no vetor. Ao final seu programa ˜
#devera escrever a soma dos valores encontrados nas respectivas posic¸ ´ oes ˜ X e Y .

import os

os.system("cls || clear");

num:int = 1;
x:int;
y:int;

numeros = [];

for i in range(0 ,8):
    num = int(input(f"Digite o {i + 1}° valor: "));
    numeros.append(num);
    os.system("cls || clear");

x = int(input("Digite o valor de X: "));
y = int(input("Digite o valor de Y: "));

for j in range(0 , 8):

    if numeros[j] == x:
        print(f"{numeros[j]} + {x} = {numeros + x}");