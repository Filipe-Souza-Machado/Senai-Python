import os

# limpa o terminal
os.system("cls || clear");

idade: int;

idade = int(input("Digite sua idade: "));

if idade > 18 or idade >= 65:
    print(f"Não votar");
else:
    print(f"pode votar");

print(f"final");