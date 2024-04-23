import os;

os.system("clear");

A = [1, 0, 5, -2, -5, 7];
soma:int = 0;

soma = A[0] + A[1] + A[5];
A[4]= 100;

print(f"soma: {soma}");
print(f"posição 4: {A[4]}");

for i in range(6):
    print(f"posição {i}: {A[i]} ");