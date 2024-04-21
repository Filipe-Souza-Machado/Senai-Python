import os;

os.system("cls || clear");

numeros = [5];
maior:int;
menor:int;

for i in range(4):
    dados = float(input(f"Digite o {i + 1}º valor: "));
    numeros.append(dados);
