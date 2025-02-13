import os
import random;

os.system("cls || clear");

nomes:str = [];
n:str;
nome_sorteado:str;

while len(nomes) < 10:
    n = str(input(f"Digite o {len(nomes)+1}° nome: "));
    nomes.append(n);
    
nome_sorteado = random.choice(nomes);

os.system("cls || clear");
print(f"O nome sorteado é: {nome_sorteado}")