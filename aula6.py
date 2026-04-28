nome = input('Qual o seu nome? ')
salario = input('Quanto você quer ganhar como Dev? ')
meses = input('Quanto tempo falta para ir até o Japão? ')

float_salario = float(salario)

print(f'Seu nome é: {nome}')
print(f'Você recebe: {float_salario:.3f}')
print(f'Então faltam {meses} para chegar até o Japão.')