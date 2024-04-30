import os
os.system("clear");

# Função sem retorno
def logoSenai():
    os.system("clear");
    print("==== SENAI ====");

def tabuada(n1):

    for i in range(0,11):
        resultado = n1 * i;
        print(f"{n1} x {i} = {resultado}");

logoSenai();
primeiro_Numero = int(input("Digite o primeiro numero: "));

os.system("clear");
logoSenai();
tabuada(primeiro_Numero);