import os

os.system("clear");

def logoSenai():
    os.system("clear");
    print("==== SENAI ====");

def conversor_inflacionario(i):

    inflacão = 0;

    if i <= 99:
        inflacão = 10;
    else:
        inflacão = 20;

    porcentagem_Inflacionaria = (inflacão / 100) * i;
    total_A_Pagar = i + porcentagem_Inflacionaria;

    return total_A_Pagar;

preco = float(input("Digite o valor do produto: "));

total = conversor_inflacionario(preco);
os.system("clear");
logoSenai();
print(f"total = {total}")