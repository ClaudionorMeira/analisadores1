maior_venda = 0
menor_venda = 0
mais_vendido = ''
menos_vendido = ''
melhor_periodo = ''
pior_periodo = ''
for item in range(1, 4):
    print(f'*****{item}º ITEM*****')
    mes = str(input('MÊS: ')).strip().upper()
    produto = str(input('PRODUTO: ')).strip().upper()
    vendas = int(input('TOTAL VENDAS: '))
    if item == 1:
        maior_venda = vendas
        menor_venda = vendas
        mais_vendido = produto
        menos_vendido = produto
        melhor_periodo = mes
        pior_periodo = mes
    else:
        if vendas > maior_venda:
            maior_venda = vendas
            mais_vendido = produto
            melhor_periodo = mes
        if vendas < menor_venda:
            menor_venda = vendas
            menos_vendido = produto
            pior_periodo = mes
print('¨' * 20)
print(f'Maior quantidade de produtos vendidos: {mais_vendido} - {maior_venda} unidades')
print(f'Melhor período: {melhor_periodo}')
print('¨' * 20)
print(f'Menor quantidade de produtos vendidos: {menos_vendido} - {menor_venda} unidades')
print(f'Pior período: {pior_periodo}')
print('¨' * 20)


