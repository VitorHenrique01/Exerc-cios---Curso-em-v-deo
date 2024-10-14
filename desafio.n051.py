# desenvola um programa que leia o preimeiro termo e a razao de uma PA
# No final, mostre os 10 primeiros termos dessa progressão

print('OS 10 PRIMEIROS TERMOS DE UMA PROGRESSÃO')
p = int(input('Numero inicial: '))
r = int(input('razão: '))
c = 1
x = p
total = 0
m = 10
while m != 0:
    total = total + m
    while c <= total:
        print('{}' .format(x) , end=' > ')
        x += r
        c += 1
    print('Pausa')
    m = int(input('Quantos você quer mostrar a mais ?: '))
print('Fim')

#for c in range(primeiro, decimo, razão):
#   print('{}'. format(c), end=' > ')
#print('ACABOU')


