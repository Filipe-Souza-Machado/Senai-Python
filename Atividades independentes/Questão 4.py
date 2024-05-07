import os;

os.system("cls || clear");

nome:str;
n:float;
notas = [];
soma:int = 0;
aprovacao:str;
contador = 0;

nome = str(input("Digite seu nome :"));

for i in range(0 , 4):

    contador += 1;
    n = float(input(f"Digite sua {i + 1}° nota: "));
    notas.append(n);
    os.system("cls || clear");

for x in range(0 , 4):
    soma = soma + notas[x];

media_Aritimetica = soma / contador;

if media_Aritimetica >= 7:
    aprovacao = "Aprovado!!!";

elif media_Aritimetica <= 6.9 and media_Aritimetica >= 5:
    aprovacao = "Recuperação!!!";

else:
    aprovacao = "Reprovado";
    
print("==== DADOS ====");
print(f"nome: {nome}")
for i in range(0,4):
    print(f"{i + 1}° nota: {notas[i]}");
    
print(f"media_Aritimetica: {media_Aritimetica}");
print(f"Resultado: {aprovacao}");

