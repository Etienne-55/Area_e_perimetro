import math 

print("Calcular a distância entre os pontos A e B: ")

xb = int(input("Informe o valor de xb: "))

xa = int(input("Informe o valor de xa: "))

yb = int(input("Informe o valor de yb: "))

ya = int(input("Informe o valor de ya: "))


print("O valor da distância é de: ", math.sqrt((xb - xa) **2 + (yb - ya) **2))