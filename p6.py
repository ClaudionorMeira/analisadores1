from time import sleep
qtd_brancos = 0 #quantitativo += 1
qtd_pardos = 0 #quantitativo += 1
qtd_negros = 0 #quantitativo += 1
homens_maior = 0 #quantitativo += 1
mulher_negra = 0 #quantitativo += 1
for p in range(1, 8):
    print(f'------{p}º Registro------')
    nome = str(input('NOME: ')).strip().upper()
    idade = int(input('IDADE: '))
    cor = str(input('COR: ')).strip().upper()
    sexo = str(input('SEXO[M/F]: ')).upper()[0]
    if cor in 'PARDO/PARDA':
        qtd_pardos += 1
    if cor in 'NEGRO/NEGRA':
        qtd_negros += 1
    if cor in 'BRANCO/BRANCA':
        qtd_brancos += 1
    if sexo in 'M' and idade > 21:
        homens_maior += 1
    if sexo in 'F' and cor in 'NEGRO/NEGRA' and idade < 40:
        mulher_negra += 1
        sleep(2)
print('ANLISANDO OS DADOS FORNECIDOS...')
print('AGUARDE...')
sleep(3)
print('RESULTADO DA ANÁLISE:')
print(f'Número de pardos: {qtd_pardos}')
print(f'Número de negros: {qtd_negros}')
print(f'Número de brancos: {qtd_brancos}')
print(f'Homens com idade superior a 21 anos: {homens_maior}')
print(f'Mulheres negras com idade inferior a 40 anos: {mulher_negra}')

