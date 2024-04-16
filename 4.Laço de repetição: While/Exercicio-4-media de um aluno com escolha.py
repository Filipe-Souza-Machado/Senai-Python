import os

os.system("cls || clear");

nota: float;
soma: float = 0;
contador: int = 0;
escolha: bool = True;

while escolha == True:

    nota = float(input("Digite suas notas: "));

    contador += 1;
    soma += nota;

    escolha2 = str(input("Você quer mais notas: "));

    os.system("cls || clear");

    if escolha2 == "n":
        escolha = False;
    
    elif escolha2 == "s":
        escolha = True;

media = soma / contador;

print(f"Media: {media}");