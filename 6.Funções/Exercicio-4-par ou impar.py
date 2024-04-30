import os

os.system("clear");

def logoSenai():
    os.system("clear");
    print("==== SENAI ====");

def par_ou_Impar(n1):
    if n1 %2 ==0:
        logoSenai();
        print("é par");
    else:
        logoSenai();
        print("É impar");

numero = int(input("Digite um numero: "));
os.system("clear");

pi = par_ou_Impar(numero);