import os

# limpa o terminal
os.system("cls || clear");

nota: float;

nota = float(input("Digite sua nota: "));

if nota >= 7:
    print("Aprovado");

elif nota >= 5:
    print("Reculperação");

elif nota >= 4:
    print("conselho de classe");

else:
    print("Reprovado");

