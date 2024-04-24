# Leia um vetor de 10 posicoes. Contar e escrever quantos valores pares ele possui;

import os;

os.system("cls || clear");

A = [];
num:int;
Vpar:int = 0;

for i in range(0 , 10):
    num = int(input(f"Digite o {i + 1}° valor: "));
    
    if num %2==0:
        A.append(num);
    
    os.system("cls || clear");

print(f"Quantidade de pares: {len(A)}")
