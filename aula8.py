nome = input('Digite aqui o seu nome: ')
idade = input('Agora, digite aqui a sua idade: ')

if nome and idade:
    print(f'Seu nome é: {nome}')
    print(f'A sua idade é: {idade} anos')
    print(f'Seu nome invertido é: {(nome[::-1])}')
    
    if " " in nome:
        print(f'Os espaços em seu nome são: {nome.count(" ")}')
    else:
        print('Não há espaços.')

    print(f'Seu nome possui: {len(nome)} letras')
    print(f'A primeira letra do seu nome é: {(nome[0])}')
    print(f'A última letra do seu nome é: {(nome[-1])}')
else:
    print('Desculpe, mas há campos vazios...')