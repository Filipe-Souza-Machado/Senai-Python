import os

os.system("cls || clear");

nota: float;
soma: float = 0;
contador: int = 0;
escolha: bool = True;
quantidadeDeNotas: int = 0;

while escolha == True:

    nota = float(input("Digite suas notas: "));
    quantidadeDeNotas += 1;
#---------------------------------------------------------------------------------------------------
    contador += 1;
    soma += nota;
#---------------------------------------------------------------------------------------------------   
    escolha2 = str(input("Você quer mais notas: "));

    os.system("cls || clear");

    if escolha2 == "n":
        escolha = False;
    
    elif escolha2 == "s":
        escolha = True;
    
    elif escolha2 == "p":
        print(f"Quantidade de notas: {quantidadeDeNotas}");
#---------------------------------------------------------------------------------------------------
media = soma / contador;

print(f"Media: {media}");