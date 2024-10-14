# faça um programa que lia nome e peso de varias pessoas. Guarde tudo em uma lista e no final:
# 1 - Quantas pessoas foram  cadastradas
# 2 - Uma listagem com as pessoas mais pesadas
# 3 - Uma listagem com as pessoas mais leves

temp = []
princ = []
mai = men = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        maio = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        elif temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()

    resp = str(input('Quer continuar [Ss/Nn]'))
    if resp in 'Nn':
        break

print(f'Os dados foram {princ}')
print(f'Ao todo você cadastrou {len(princ)} pessoas')
print(f'O maior peso foide {mai}Kg')
print(f'O menor peso foi de {men}Kg')
