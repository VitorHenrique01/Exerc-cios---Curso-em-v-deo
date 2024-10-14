#Crie um programa que simule o funcionamento de um caixa eletronico.
# no inicio pergunte ao usuario qual o valor a ser sacado (numero inteiro)
# e o programa vai informar quantas cedulas de cada valor serão entregues
# OBS: Considere que o caixa possui cedulas de $50, $20, $10 e $1
print('=' * 30)
print('{:^30}'.format('BANCO VITOR'))
print('=' * 30)
valor = int(input('Que valor você quer sacar? '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced: # FAZ A CONTA SE TIVER VALOR ACIMA DE 1
        total -= ced # SUBTRAI O VALOR PELO DINHEIRO
        totced +=1 # SE SUBTRAIR USA (1 CEDULA)
    else:
        if totced > 0: # O PROGRAMA SO ESCREVE SE TIVER CEDULA A USAR !
            print(f'Total de {totced} cedulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break

