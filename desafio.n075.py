# desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma pupla. no final mostre:
# quantas vezes apareceu o numero 9
# Em que posição foi digitado a primeira vez o valor3
# Quais foram os numeros pares?

num = ( int(input('Digite um numero: ')),
        int(input('Digite um numero: ')),
        int(input('Digite um numero: ')),
        int(input('Digite um numero: ')))
print(f'Você digitou os valores {num}')
print(f'O valor apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O numero 3 apareceu em {num.index(3)}° posição')
else:
    print('O valor (3) não foi digitado nenhuma vez')
print(f'Os numeros pares sorteados foram ')
for n in num:
    if n%2 == 0:
        print(n, end=' ')

