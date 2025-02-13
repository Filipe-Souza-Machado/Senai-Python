import os
os.system("cls || clear");

num: int = 0;
numeros: int = [];
mediaAritimetica:int;
soma:int = 0;

while len(numeros) < 10:
    num = int(input(f"Digite o {len(numeros)+1}° numero: "));
    numeros.append(num);
    
for i in numeros:
    soma += i;
    
mediaAritimetica = soma / len(numeros);

os.system("cls || clear");
print(f"Media aritimetica: {mediaAritimetica}");