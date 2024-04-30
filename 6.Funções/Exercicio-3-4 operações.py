import os
os.system("clear");

# Função sem retorno
def logoSenai():
    os.system("clear");
    print("==== SENAI ====");

def somar(n1, n2):
    resutadoS = n1 + n2;
    return resutadoS;

def subtrair(n1, n2):
    resutadoSb = n1 - n2;
    return resutadoSb;

def multplicar(n1, n2):
    resutadoM = n1 * n2;
    return resutadoM;

def dividir(n1, n2):
    resutadoD = n1 / n2;
    return resutadoD

logoSenai();
primeiro_Numero = int(input("Digite o primeiro numero: "));

logoSenai();
segundo_Numero = int(input("Digite o segundo numero: "));

som = somar(primeiro_Numero, segundo_Numero);
subtr = subtrair(primeiro_Numero, segundo_Numero);
mult = multplicar(primeiro_Numero, segundo_Numero);
div = dividir(primeiro_Numero, segundo_Numero);

print(f"soma: {som}");
print(f"subtração: ");
print(f"Divisão: ");
print(f"Divisão: ");