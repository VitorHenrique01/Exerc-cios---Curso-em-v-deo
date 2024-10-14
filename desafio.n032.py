from datetime import date

ano = int(input('Que ano quer analizar ? Coloque 0 para anaisar o ano atual '))
if ano %4 == 0 and ano % 100 != 0 or ano % 400 == 0:
# colocando mais CONDIÇÕES nas CONDIÇÕES

    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO É BISSEXTO'.format(ano))

#screva um programa que leia um ano qualquer e mostre se ele é bissexto