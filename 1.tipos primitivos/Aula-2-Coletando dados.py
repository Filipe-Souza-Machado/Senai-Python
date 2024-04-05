import os

# limpa o terminal
os.system("cls || clear");

# solicitando dados do usuario
nome = input("Digite seu nome: ");
idade = int(input("Digite sua idade: "));
peso = float(input("Digite seu peso: "));

#Exibindo dados inderidos pelo usuario
print("\n === Exibindo resultados ===");
print(f"Nome: {nome}");
print(f"Idade: {idade}");
print(f"Idade: {peso}");