#Escreva um programa que leia 10 numeros inteiros e os armazene em um vetor. Imprima ´
#o vetor, o maior elemento e a posic¸ao que ele se encontra.
import os;

os.system("cls || clear");

numeros = [];
num:int;
maiorNum:int = 0;
menorNum:int = 9999;
posicaoMaior:int;
posicaoMenor:int;

for i in range(0 ,10):

    num = int(input(f"Digite o {i + 1}° valor: "));
    numeros.append(num);
    os.system("cls || clear");

for x in range(0 , 10):

    if numeros[x] > maiorNum:
        maiorNum = numeros[x];
        posicaoMaior = ;

    if numeros[x] < menorNum:
        menorNum = numeros[x];
        
print(f"Maior: {maiorNum}");
print(f"Menor: {menorNum}");
print(f"posicao maior: {posicaoMaior}")