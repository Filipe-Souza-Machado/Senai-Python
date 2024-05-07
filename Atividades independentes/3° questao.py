import os;
import time;

os.system("cls || clear");

nome = str(input("Digite seu nome: "));
idade = int(input("Digite sua idade: "));
email = str(input("Digite seu email: "));
telefone = int(input("Digite seu telefone: "));

os.system("cls || clear");

while True:
    print("==== MENU ====");
    print("1 - Mostrar nome e idade;");
    print("2 - Mostrar nome e e-mail;");
    print("3 - Mostrar nome e telefone;");
    print("4 - Mostrar todas as informações;");
    print("0 - Sair do programa.");

    escolha = int(input("Escolha um opção: "));

    match escolha:
        case 1:
            print(f"nome: {nome}")
            print(f"idade: {idade}")

        case 2:
            print(f"nome: {nome}")
            print(f"email: {email}")

        case 3:
            print(f"nome: {nome}")
            print(f"telefone: {telefone}")

        case 4:
            print(f"nome: {nome}")
            print(f"idade: {idade}")
            print(f"email: {email}")
            print(f"telefone: {telefone}")

        case 0:
            break
            
        case _: 
            print("Opção  incorreta, tente novamente.");
            time.sleep(3)
            os.system("cls || clear");


