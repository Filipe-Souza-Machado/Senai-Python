# xburger11.50, xsalada12.50, xbacon13.00, xegg13.50,xfrango 13.50, xtudo14.50, xtudodefrngo14.50;

import os;

os.system("cls || clear");

qtdPratos:int = 0;
preco:float = 0;
escolha:bool = True;
prato:int;
desconto:float = 0;
descontoTotal:float = 0;
taxa:float = 0;
taxaTotal:float = 0;
precoTotal:float;
pratos_Escolhidos = [];
pagamentoEscolhido:int;

while escolha == True:
    
    print("===== Cardapio =====");
    print("1- X-burger: R$ 11.50");
    print("2- X-salada: R$12.50");
    print("3- X-bacon: 13.00");
    print("4- X-egg: 13.50");
    print("5- X-frango: 13.50");
    print("6- X-tudo: 14.50");
    print("7- X-tudo: 14.50");
    print("\n");

    qtdPratos +=1;
    
    prato = int(input("Escolha uma opção do cardapio: "));

    if prato == 1:
        preco +=  11.50;
        pratos_Escolhidos.append("X-burger");
        
    elif prato == 2:
        preco +=  12.50;
        pratos_Escolhidos.append("X-salada")

    elif prato == 3:
        preco +=  13.00;
        pratos_Escolhidos.append("X-bacon")

    elif prato == 4:
        preco +=  13.50;
        pratos_Escolhidos.append("X-egg")
        
    elif prato == 5:
        preco +=  13.50;
        pratos_Escolhidos.append("X-frango")
        
    elif prato == 6:
        preco +=  14.50;
        pratos_Escolhidos.append("X-tudo")
        
    elif prato == 7:
        preco +=  14.50;
        pratos_Escolhidos.append("X-tudo de frango")
        
    Escolha_Do_Usuario = str(input("Quer mais um prato (s/n): "));
    
    if Escolha_Do_Usuario == "s":
        escolha = True;
    else:
        escolha = False;
    
    os.system("cls || clear");

print("=====Forma de pagamento=====");
print("1 - A vista");
print("2 - Cartão de credito");
    
forma_De_Pagamento = int(input("escolha uma forma De Pagamento: "));
    
if forma_De_Pagamento == 1:
    desconto += 10;
    descontoTotal = (desconto / 100) * preco;
    precoTotal = preco - descontoTotal;
    pagamentoEscolhido = "Vista";

elif forma_De_Pagamento == 2:
    taxa += 10;
    taxaTotal = (taxa / 100) * preco;
    precoTotal = preco + taxaTotal;
    pagamentoEscolhido = "Cartão";
        
os.system("cls || clear");

print("===Pratos escolhidos===");
for i in pratos_Escolhidos:
    print(i);

print("\n");
print(f"Forma de pagamento escolhida: {pagamentoEscolhido}");
print(f"Valor de desconto: R${descontoTotal}");
print(f"Valor de acressimo: R${taxaTotal}");
print(f"sub total: R${preco}");
print(f"Total a pagar: R${precoTotal}");
