import os

os.system("clear");

def logoSenai():
    os.system("clear");
    print("==== SENAI ====");

def conversor(m):
    cm = m * 100;
    return cm;

metros = float(input("Digite a quantidade de metros: "));

logoSenai();
tam = conversor(metros);

print(f"{tam} cm");