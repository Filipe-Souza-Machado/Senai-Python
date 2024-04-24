#. Fac¸a um programa que receba do usuario um vetor com 10 posic¸ ´ oes. Em seguida dever ˜ a´
#ser impresso o maior e o menor elemento do vetor

import os;

os.system("cls || clear");

numeros = [];
num:int;
maiorNum:int = 0;
menorNum:int = 9999;

for i in range(0 ,10):

    num = int(input(f"Digite o {i + 1}° valor: "));
    numeros.append(num);
    os.system("cls || clear");

for x in range(0 , 10):
    if numeros[x] > maiorNum:
        maiorNum = numeros[x];

    if numeros[x] < menorNum:
        menorNum = numeros[x];
        
print(f"Maior: {maiorNum}");
print(f"Menor: {menorNum}");