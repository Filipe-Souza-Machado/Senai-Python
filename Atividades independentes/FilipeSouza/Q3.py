import os
os.system("cls || clear");

num: int = 0;
numeros: int = [];
maiorNum:int = -99999;

for i in range(0,10):
    
    num = int(input(f"Digite o {i+1}° numero: "));
    numeros.append(num);

for x in range(len(numeros)):
    if numeros[x] > maiorNum:
        maiorNum = numeros[x];
        
os.system("cls || clear");
print(numeros);
print(f"Maior numero: {maiorNum}");