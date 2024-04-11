import os

os.system("cls || clear");

n1: int;
n2: int;
escolha: str;

n1 = int(input("Digite um valor: "));
n2 = int(input("Digite outro valor: "));
escolha = str(input("Digite um operador: "));

soma = n1 + n2;
subtr = n1 - n2;
mult = n1 * n2;
divi = n1 / n2;

os.system("cls || clear");

if escolha == "+":
    print(f"{n1} + {n2} = {soma}");
elif escolha == "-":
    print(f"{n1} - {n2} = {subtr}");
elif escolha == "*":
    print(f"{n1} x {n2} = {mult}");
elif escolha == "/":
    print(f"{n1} : {n2} = {divi}");