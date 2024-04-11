import os

n1: int;
soma: int = 0;

os.system("cls || clear");

for i in range(1,6):
    
    n1 = int(input("Digite um numero: "));
    soma = soma + n1;

os.system("cls || clear");
print(f"total: {soma}");