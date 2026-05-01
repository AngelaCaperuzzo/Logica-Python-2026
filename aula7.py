try:
    numero_1 = int(input('Digite um número: '))
    numero_2 = int(input('Agora, digite outro número: '))

    if numero_1 > numero_2:
        print('O primeiro numero digitado é maior que o segundo número digitado.')
    elif numero_2 > numero_1:
        print('O segundo número digitado é maior que o primeiro número digitado.')
    else:
        print('Os números digitados são iguais...')

except ValueError:
    print('Opa, digite apenas números.')