import os

os.system("cls || clear");

nota1: float = -1;
nota2: float = -1;

while nota1 < 0 or nota1 > 10:
    nota1 = float(input("Digite sua nota: "));
    os.system("cls || clear");

while nota2 < 0 or nota2 > 10:
    nota2 = float(input("Digite sua nota: "));
    os.system("cls || clear");

mediaAritimetica = (nota1 + nota2) / 2;

print(f"Media: {mediaAritimetica}");