# CRie um programa que leia o nome e duas notas de varios alunos e guarde tudo em uma lista
# No final mostre um boletim contendo a média de cada um
# e permita que o usuário possa mostrar as notas de cada aluno individualmente


ficha = list()
while True:
    nome = str(input('nome:'))
    nota1 = float(input('nota 1: '))
    nota2 = float(input('nota 2: '))
    media = (nota1 + nota2) /2
    ficha.append([nome,[nota1, nota2], media])
    resp = str(input('Quer  continuar? [S/N]'))
    if resp in 'Nn':
        break

print('-='*30)
print(f'{'No.':<4}  {'NOME:':<10}  {'MÉDIA:':>8}')  # MOSTRAR TEXTO APENAS SEM INF.
print('-'*30)
for i, a in enumerate(ficha):      # ENUMERAR UMA LISTA, CONFORME OS DADOS VÃO ENTRANDO
    print(f'{i:<4}  {a[0]:<10}  {a[2]:>8.1f}')      # A CADA LAÇO (i)+=1, # (a) = LAÇO E TODAS INFORMAÇÕES (a)[0] É = NOME
while True:
    print('-'*30)
    opc = int(input('Mostrar nota de qual aluno ? (999 interrompe): '))
    if opc == 999:
        print('Finalizando...')
        break
    if opc <=len(ficha) -1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')