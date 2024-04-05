import os

# limpa o terminal
os.system("cls || clear");

nota1: float;
nota2: float;
nota3: float;
nota4: float;
media: float;
soma: float;

nota1 = float(input("Digite sua nota: "));
nota2= float(input("Digite sua nota: "));
nota3= float(input("Digite sua nota: "));
nota4= float(input("Digite sua nota: "));

os.system("cls || clear");

soma = nota1 + nota2 + nota3 + nota4;
media = soma / 4;

print(f"Media: {media}");