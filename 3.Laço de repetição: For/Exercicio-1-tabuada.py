import os

n1: int;

n1 = int(input("Digite um numero: "));

os.system("cls || clear");

for i in range(1,11):
    
    print(f" {n1} x {i} = {n1 * i}");
