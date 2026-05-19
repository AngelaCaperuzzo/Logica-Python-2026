entrada = input('Que horas são? ')
entrada_int = int(entrada)

if 0 <= entrada_int <= 11:
    print('Bom dia.')

elif 12 <= entrada_int <= 17:
    print('Boa tarde.')

elif 18 <= entrada_int <= 23:
    print('Boa noite.')

else:
    print('Hora inválida.')