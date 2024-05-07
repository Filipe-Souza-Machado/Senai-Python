import os;

os.system("cls || clear");

num:int;
maiorNumero:int = 0;
menorNumero:int = 9999;

for i in range(0 , 5):

    num = int(input(f"Digite o {i + 1}° numero: "))

    if num > maiorNumero:
        maiorNumero = num;
    
    if num < menorNumero:
        menorNumero = num;

print(f"Maior numero: {maiorNumero}");
print(f"Menor numero: {menorNumero}");

