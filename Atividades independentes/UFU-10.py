
import os

os.system("clear")

QTDNUMEROS = 5
contador = 0
mediageral = 0 
somageral = 0
mediapares = 0 
somapares = 0
mediaimpares = 0
somaimpares = 0
qtdpares = 0
qtdimpares = 0
qtdpositivo = 0
qtdnegativo = 0
maiornumero = 0
menornumero =9999



for i in range (QTDNUMEROS):
    
    numeros = int(input("Digite um numero:"))
    contador +=1
    somageral += 1
    mediageral = somageral + contador

    if numeros > 0 :
        qtdpositivo += 1
    else:
        qtdnegativo +=1

    if numeros %2 == 0 :
        qtdpares += 1
        somapares += numeros

    if nume:
        qtdimpares += 1
        somaimpares += numeros

    if(numeros >maiornumero):
        maiornumero = numeros

    if(numeros > menornumero):
        menornumero = numeros

    mediapares = somapares / qtdpares;
    mediaimpares = somaimpares / qtdimpares;
    
print(f"A quantidade de valores apresentados e : {QTDNUMEROS}")
print(f"A quantidade de valores positivos e : {qtdpositivo}")
print(f"A quantidade de valores negativos e : {qtdnegativo}")
print(f"A quantidade de valores pares e : {qtdpares}")
print(f"A quantidade de valores impares e : {qtdimpares}")
print(f"A media de valores pares e : {mediapares}")
print(f"A media de valores impares e : {mediapares}")
print(f"A media geral e : {mediageral}")
print(f"O maior numero e : {maiornumero}")
print(f"O menor numero e : {menornumero}")