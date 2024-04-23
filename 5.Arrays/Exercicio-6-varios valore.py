import os

os.system("cls || clear");

num:int = 1;
numeros = [];
qtdPares:int = 0;
qtdImpares:int = 0;
qtdPositivos:int = 0;
qtdNegativos:int = 0;
maiorNumero:int = 0;
menorNumero:int = 9999;
mediaPar:int;
mediaImpar:int;
somaPar:int =0;
somaImpar:int = 0;
somaGeral:int = 0;
contadorPar = 0;
contadorImpar = 0;
contadorGeral:int = 0;
mediaGeral:int;

for i in range(0 , 5):
    contadorGeral += 1;

    num = int(input(f"Digite o {i + 1}º valor: "));
    somaGeral += num;

    numeros.append(num);

    if num %2==0:
        qtdPares += 1;
        somaPar = somaPar + numeros[i];
        contadorPar += 1;
    
    else: 
        qtdImpares += 1;
        somaImpar = somaImpar + numeros[i];
        contadorImpar += 1;
    
    if num > 0:
        qtdPositivos += 1;
    else:
        qtdNegativos += 1;

    if numeros[i] > maiorNumero:
         maiorNumero = numeros[i];
    
    if numeros[i] < menorNumero:
         menorNumero = numeros[i];

mediaPar = somaPar / contadorPar;
mediaImpar = somaImpar / contadorImpar;
mediaGeral = somaGeral / contadorGeral;

os.system("cls || clear");

print(f"Quantidade de pares: {qtdPares}");
print(f"Quantidade de impares: {qtdImpares}");
print(f"Quantidade de positivos: {qtdPositivos}");
print(f"Quantidade de negativos: {qtdNegativos}");
print(f"Quantidade de inseridos: {contadorGeral}");
print(f"Maior numero: {maiorNumero}");
print(f"Menor numero: {menorNumero}");
print(f"Media par: {mediaPar}");
print(f"Media impar: {mediaImpar}");
print(f"Media geral: {mediaGeral}");

for x in range(8 , 0):
    print(f"{x}° valor: {numeros[x]}");

