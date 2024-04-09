import os

# limpa o terminal
os.system("cls || clear");

idade: int;

idade = int(input("Digite sua idade: "));

if idade > 18 or idade >= 65:
    print(f"É obrigado a votar");
    
else:
    print(f"Não é obrigado a votar");

print(f"final");