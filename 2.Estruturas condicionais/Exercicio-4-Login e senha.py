import os

# limpa o terminal
os.system("cls || clear");

login: str; 
loginCadastrado:str = "paula";
senha: str;
senhaCadastrada:str = "1234";

login = str(input(f"Login: "));
senha = str(input(f"Senha: "));

if login == loginCadastrado and senha == senhaCadastrada:
    print("Bem vindo");
else: 
    print("Login e senha invalidos");