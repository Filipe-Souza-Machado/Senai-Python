import os

num: int = -1;
soma: int = 0;

while num != 0:
    
    num = int(input("Digite um numero: "));
    soma = soma + num;
    
os.system("cls || clear");
print(f"total: {soma}");