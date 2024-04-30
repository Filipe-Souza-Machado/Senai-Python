#Fac¸a um programa para ler a nota da prova de 15 alunos e armazene num vetor, calcule
#e imprima a media geral.
import os;
os.system("cls || clear");

notas = [];
num:float;
soma:float = 0;

for i in range(0 , 15):
    num = float(input(f"Digite a nota do {i + 1}º aluno: "));
    notas.append(num);
    soma = soma + num;
    os.system("cls || clear");

media = soma / i;

print(f"Media geral: {media}");