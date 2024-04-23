import os

os.system("cls || clear");

# Ler um conjunto de numeros reais, armazenando-o em vetor e calcular o quadrado das ´
#componentes deste vetor, armazenando o resultado em outro vetor. Os conjuntos temˆ
#10 elementos cada. Imprimir todos os conjuntos.

num:float;
quadrado:float;
numeros = [];
numerosQuadrado = [];

for i in range(0 , 10):
    num = float(input(f"Digite o {i + 1}° valor: "));
    numeros.append(num);
    os.system("cls || clear");

for x in range(0 , 10):
    quadrado = numeros[x] * numeros[x];
    numerosQuadrado.append(quadrado);

for j in range(0 , 10):
    print(f"Quadrado de {numeros[j]}: {numerosQuadrado[j]}");