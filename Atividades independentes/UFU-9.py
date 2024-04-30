#Crie um programa que le 6 valores inteiros pares e, em seguida, mostre na tela os valores lidos na ordem inversa.

import os;

os.system("cls || clear");

num:int;
numeros = [];
pares:int = 0;

for i in range(0 , 6):
    num = int(input(f"Digite o {i + 1}° valor: "));
    numeros.append(num);
    os.system("cls || clear");

numeros.reverse();

for x in numeros:
    print(x);

