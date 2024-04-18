import os

os.system("cls || clear");

numero: int = 0;
contador: int =0;
media: int;
soma: int = 0;

while numero >= 0:
    
    numero = float(input("Digite suas notas: "));

    if numero > 0:
        soma = soma + numero;
        contador += 1;

media = soma / contador;

os.system("cls || clear");

print(f"Media: {media}");
