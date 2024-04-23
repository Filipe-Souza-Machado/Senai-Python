import os

os.system("cls || clear");

num:int = 1;
numeros = []
qtdPares:int = 0;
qtdImpares:int = 0;
qtdPositivos:int = 0;
qtdNegativos:int = 0;
qtdInserida:int = 0;
contador:int  = 0;

while num != 0:
    
    contador += 1;
    num = int(input(f"Digite o {contador}° valor: "));
    qtdInserida += 1;
    numeros.append(num);
    os.system("cls || clear");
 
    if num %2==0:
        qtdPares += 1;
    else: 
        qtdImpares += 1;
   
    if num > 0:
        qtdPositivos += 1;
    else:
        qtdNegativos += 1;

print(f"Quantidade inserida: {qtdInserida}");
print(f"Quantidade de pares: {qtdPares}");
print(f"Quantidade de impares: {qtdImpares}");
print(f"Quantidade de positivos: {qtdPositivos}");
print(f"Quantidade de negativos: {qtdNegativos}");
