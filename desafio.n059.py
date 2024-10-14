# CRIE UM PROGRAMA QUE LEIA DOIS VALORES E MOSTRE UM MENU NA TELA:
# 1 - SOMAR
# 2 - MULTIPLICAR
# 3 - SABER QUAL MAIOR VALOR
# 4 - GERAR NOVOS NUMEROS
# 5 - SAIR DO PROGRAMA
# o PROGRAMA DEVE REALIZAR A OPERAÇÃO SOLICITADA
c = 1
while c == 1:
    n1 = int(input('Digite um valor: '))
    n2 = int(input('Digite outro valor: '))
    op = int(input('''--- APERTE PARA: ---
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] SABER O MAIOR
    [ 4 ] GERAR NOVOS NUMEROS
    [ 5 ] SAIR DO PROGRAMA 
    RESPOSTA: '''))
    if op == 1:
        print(' A soma de {} com {} é {}' .format(n1, n2, n1+n2))
        c += 1
    elif op == 2:
        print('A multiplicação de {} com {} é {}' .format(n1, n2, n2*n1))
        c += 1

    elif op == 3:
        if n1 < n2:
            print('O maior entre eles é {}' .format(n2))
        else:
            print('O maior entre eles é {}' .format(n1))
        c += 1

    elif op == 4:
        c = 1
    elif op == 5:
        c += 1
print('Fim')

