import os

os.system("cls || clear");

maiorNum:int = -999;
num:int;

for i in range(0,3):
    num = int(input("Digite um numero: "));
    
    if num > maiorNum:
        maiorNum = num;
    
os.system("cls || clear");        
print(f"Maior numero: {maiorNum}")