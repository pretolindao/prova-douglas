print('INFORME UM NUMERO')
num = input()
print('1-SOMA\2-SUBTRACAO\3-MULIPLICACAO\4-DIVISAO\')
operacao = int(input())
print('INFORME O SEGUNDO NUMERO')
num2 = input()

if operacao == 1:
    print(f'OPERACAO:{num} + {num2} = {float(num)+float(num2)}')
elif operacao==2:
    print(f'OPERACAO:{num} - {num2} = {float(num) - float(num2)}')
elif operacao==3:
    print(f'OPERACAO:{num} * {num2} = {float(num) * float(num2)}')
elif operacao==4:
    print(f'OPERACAO:{num} / {num2} = {float(num) / float(num2)}')
elif operacao==5:
    print(f'OPERACAO:{num} % {num2} = {float(num) % float(num2)}')
