#Fazer um programa para ler 5 valores e, em seguida, mostrar a posic¸ao onde se encon- ˜
#tram o maior e o menor valor.
import os;
os.system("cls || clear");

numeros:int = [];
num:int;
maior_Num_Posi:int = 0;
menor_Num_Posi:int = 9999;
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