import os

# limpa o terminal
os.system("cls || clear");

nomeDoUsuario: str;
idadeDoUsuario: int;
pesoDoUsuario: float;

nomeDoUsuario = input("Digite seu nome: ");
idadeDoUsuario = int(input("Digite seu nome: "));
pesoDoUsuario = float(input("Digite seu nome: "));
print(f"\n=== Resultados ===");

print(f"nome: {nomeDoUsuario}");
print(f"Idade: {idadeDoUsuario}");
print(f"Peso: {pesoDoUsuario}");
