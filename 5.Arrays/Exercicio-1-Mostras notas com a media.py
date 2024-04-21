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

for i in range(4):
    print(f"{i + 1}° nota: {notas[i]}");
    
print(f"Media: {media}");