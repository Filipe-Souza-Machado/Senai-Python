import os

os.system("cls || clear");

num:int;
numeros = []
qtdPares:int = 0;
qtdImpares:int = 0;
qtdPositivos:int = 0;
qtdNegativos:int = 0;
qtdInserida:int = 0;

for i in range(5):
    num = int(input(f"Digite o {i + 1}° valor: "));
    qtdInserida += 1;
    numeros.append(num);
    os.system("cls || clear");


for x in range(5):
    
    if numeros[x] %2==0:
        qtdPares += 1;
    else: 
        qtdImpares += 1;
   
    if numeros[x] > 0:
        qtdPositivos += 1;
    else:
        qtdNegativos += 1;

print(f"Quantidade inserida: {qtdInserida}");
print(f"Quantidade de pares: {qtdPares}");
print(f"Quantidade de impares: {qtdImpares}");
print(f"Quantidade de positivos: {qtdPositivos}");
print(f"Quantidade de negativos: {qtdNegativos}");
