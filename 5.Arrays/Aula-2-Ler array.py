import os

os.system("clear");

notas = [];# criar variavel

for i in range(3):
    nota = float(input(f"Digite a {i + 1}º nota: ")); # pega o valor
    notas.append(nota); # Guarda o valor no vetor

os.system("clear");

print(f"Tamanho do vetor: {len(notas)}");#tamanho do vetor

for i in range(len(notas)):
    print(f"{i + 1}ª Nota: {notas[i]}");