#Faca um programa que preencha um vetor com 10 numeros reais, calcule e mostre a 
#quantidade de numeros negativos e a soma dos numeros positivos desse vetor;

import os;
os.system("cls || clear");

numeros = [];
num:float;
somaPosi:float = 0;
qtdNegativos:int = 0;

for i in range(0 , 10):

    num = float(input(f"Digite o {i + 1}º numero: "));
    numeros.append(numeros);

for x in range(0 , 10):

    if numeros[x] > 0:
        somaPosi = somaPosi + numeros[x];
    else:
        qtdNegativos += 1;
