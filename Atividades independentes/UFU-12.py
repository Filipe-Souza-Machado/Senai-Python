#Fazer um programa para ler 5 valores e, em seguida, mostrar todos os valores lidos
#juntamente com o maior, o menor e a media dos valores

import os;
os.system("cls || clear");

numeros:int = [];
num:int;
maiorNum:int = 0;
menorNum:int = 9999;
soma:int = 0;

for i in range(0 , 5):
    num = int(input(f"Digite o {i + 1}º valor: "));
    numeros.append(num);
    os.system("cls || clear");

for x in range(0 , 5):

    soma = soma + numeros[x];

    if numeros[x] > maiorNum:
        maiorNum = numeros[x];

    if numeros[x] < menorNum:
        menorNum = numeros[x];

media:int = soma / x;

print(f"Maior numero: {maiorNum}");
print(f"Menor numero: {menorNum}");
print(f"Media geral: {media}");