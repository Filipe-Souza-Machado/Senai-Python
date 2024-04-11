import os

os.system("cls || clear ");

quantidadeAdquirida: int;
precoUnitario: float;
total: float;
totalPagar: float;
desconto: float;
desconto = 0;

print("====tabela de preços====");
print("pao: 5.00");
print("queijo:3.00");
print("ovo:10..");

quantidadeAdquirida = int(input(f"Quantidade desejada: "));

if quantidadeAdquirida <= 5:
    desconto = 2;

elif quantidadeAdquirida > 5 and quantidadeAdquirida <= 10:
    desconto = 3;

elif quantidadeAdquirida > 10:
    desconto = 5;

