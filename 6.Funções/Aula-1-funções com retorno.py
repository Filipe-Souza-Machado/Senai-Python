import os

os.system("clear");

# Função sem retorno
def logoSenai():
    os.system("clear");
    print("==== SENAI ====");

# Função com retorno
def somar(n1, n2):
    resultado = n1 + n2;
    return resultado;



logoSenai();
primeiro_Numero = int(input("Digite o primeiro numero: "));

logoSenai();
segundo_Numero = int(input("Digite o segundo numero: "));

soma = somar(primeiro_Numero , segundo_Numero);

print(soma);