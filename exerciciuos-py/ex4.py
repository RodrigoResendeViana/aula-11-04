i = 1
quant = 0
while i <=10:
    num = int(input("Digite um numero:" ))
    i += 1
    if num >=100 and num<=200:
        quant += 1
print(f'Dentre os 10 números digitados, há {quant} entre 100 e 200')