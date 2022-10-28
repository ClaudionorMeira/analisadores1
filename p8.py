print('¨' * 20)
print('{:^20}'.format('VALIDAÇÃO DE DADOS'))
print('¨' * 20)
for s in range(1, 6):
    nome = str(input('Nome: ')).strip().upper()
    sexo = str(input('Digite o sexo: ')).strip().upper()[0]
    while sexo not in 'M/F':
        nome = str(input('Nome: ')).strip().upper()
        sexo = str(input('DADOS INVÁLIDOS. Por favor, informe seu sexo: ')).strip().upper()[0]
    print(f'Nome: {nome}')
    print(f'Sexo {sexo}')
print('¨' * 35)
print('DADOS VALIDADOS COM SUCESSO')
print('FIM DO PROGRAMA')