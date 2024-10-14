# crie um programa que tenha um tupla com varias palavras( não usar acento).
# depois disso mostre para cada palavra quais são suas vogais

x = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis','estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for c in x:
    print(f'\nNa palavra {c} temos: ', end='')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')


