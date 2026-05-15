try:

    numero = input('Digite um número: ')
    numero = int(numero)

    if numero %2 == 0:
        print('Esse número é um número par.')

    else:
        print('Esse número é um número ímpar.')

except ValueError:
    print('Esse número não é um número inteiro.')