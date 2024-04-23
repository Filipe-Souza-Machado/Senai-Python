import os;

os.system("clear");

#Crie um programa que le 6 valores inteiros e, em seguida, mostre na tela os valores lidos. 

num:int;
numeros = [];

for i in range(0 , 6):
    num = int(input(f"Digite o {i + 1}º valor: "));
    numeros.append(num);
    os.system("clear");

for x in range(0 , 6):
    print(f"{x + 1}º valor: {numeros[x]}");1
