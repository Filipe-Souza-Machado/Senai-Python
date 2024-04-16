import os

os.system("cls || clear");

nota: float = -1;
soma: float = 0;

for i in range(1,4):
    while True:
        nota = float(input("Digite sua nota: "));
        if nota < 0 or nota > 10:
            print("Nota invalida....\n");
        else:
            soma += nota;
            break;

os.system("cls || clear");

media = soma / 3;

if media >= 7:
    print("Aprovado!!!");

elif media <= 6.9 or media >= 5:
    print("Recuperação!!!");

else:
    print("Reprovado!!!");