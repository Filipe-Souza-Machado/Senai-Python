import os
os.system("cls || clear");

num: int = 0;
numeros: int = [];
qtdPositivos = 0;
qtdNegativos = 0;
somaPositivos = 0;
Negativos = [];

while len(numeros) < 10:
    
    num = int(input(f"Digite o {len(numeros)+1}° numero: "));
    numeros.append(num);
    
for i in numeros:
    
    if i > 0:
        qtdPositivos += 1;
        somaPositivos += i;
    else:    
        qtdNegativos += 1;
        Negativos.append(i);
 
os.system("cls || clear");   
print(f"Quantidade dos poistivos: {qtdPositivos}");
print(f"Quantidade dos negativos: {qtdNegativos}");
print(f"Negativos: {Negativos}");
print(f"Soma positivos: {somaPositivos}");