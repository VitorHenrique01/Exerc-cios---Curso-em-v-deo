# Crie um progrma que leia uma frase qualquer e diga se ela
# é um palindromo, desconsiderando os espaços ( se a frase se le de tras pra frente)

frase = str(input('Digite uma frase')) .strip() .upper()   # tirei os espaços # coloquei tudo em amiusculo
palavras = frase.split()    # SEPARA A FRASE EM PALATRAS
junto = ''.join(palavras)   # JUNTA AS PALAVRAS # (TROCAR OS (ESPAÇOS) )
inverso = ''
for letra in range(len(junto) -1, -1, -1):   # len para pegar ultima letra
# COMEÇO PELA ULTIMA LETRA: ( LEN(JUNTO) -1)
# VOU ATE A ULTIMA: ( -1 )
# DE TRAS PRA FRENTE ( -1 )
    inverso += junto[letra]
if inverso == junto:
    print( 'Temos um palindromo')
else:
    print('A frase não é um palindromo')



