import os;

os.system("cls || clear");

notas = [];
media: float;
contador: int;
soma: float = 0;

for i in range(4):
    nota = float(input(f"Digite sua {i + 1}º nota: "));
    notas.append(nota);
    soma = soma + nota;

contador = len(notas);

media = soma / contador;

print(f"Media: {media}");