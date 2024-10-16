 # crie um programa que leia nome, sexo e idade de varias pessoas, guardando os dados de cada pessoa em um  dicionario
 # e todos os dicionarios em uma lista. no final mostre:
 # Quantas pessoas cadastradas
 # a média de idade
 # uma lista com mulheres
 # uma lista com idade acima da medias


dici = dict()
lista = list()
mulheres = list()
acima = list()
tot = media = 0


while True:
    dici.clear()
    dici['nome'] = str(input('Qual seu nome ? '))
    dici['idade'] = int(input('Qual sua idade ? '))
    while True:
        dici['sexo'] = str(input(f'Qual seu sexo (M/F)? ')).upper()
        if dici['sexo'] in 'MF':
            break
    tot += dici['idade']
    lista.append(dici.copy())
    if dici['sexo'] == 'F':
        mulheres.append(dici.copy())

    while True:
        x = str(input('Quer gravar outro? (S/N): ')).upper()
        if x in 'SN':
            break
        print('Erro! Escreva apenas S ou N.')
    if x == 'N':
        break
media = tot / len(lista)
for c in lista:
    if c['idade'] >= media:
        print('     ')
        for k, v in c.items():
            print(f'{k} = {v}', end='')

print(f'Essas são todas pessoas cadastradas: {lista}')
print(f'Esse é o total de pessoas cadastradas: {len(lista)}')
print(f'Essa é a média: {media:5.2f}')
print(f'Essas são todas as mulheres: {mulheres}')
print(f'As pessoas com idade acima da é:')
for c in lista:
    if c['idade'] >= media:
        print('     ')
        for k, v in c.items():
            print(f'{k} = {v}', end=' ')








