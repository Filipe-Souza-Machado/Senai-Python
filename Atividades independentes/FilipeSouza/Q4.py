import os
os.system("cls || clear");

nomes:str = [];
n:str;

while len(nomes) < 5:
    n = str(input(f"Digite o {len(nomes)+1}° nome: "));
    nomes.append(n);
    
os.system("cls || clear");
nomes.sort()
print(nomes);