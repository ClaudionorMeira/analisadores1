cont = soma = 0
mais_vendido = ' '
menos_vendido = ' '
desc_mais = ' '
desc_menos = ' '
maior_qtd = 0
menor_qtd = 0
pdt_caro = 0
pdt_barato = 0
while True:
    pdt = str(input('Nome do produto: ')).strip().upper()
    vu = float(input('Valor unitário: '))
    qtd = int(input('Quantidade: '))
    total = qtd * vu
    cont += 1
    soma += total
    resp = str(input('Encerrar: [s/n] ')).strip().upper()[0]
    if cont == 1:
        mais_vendido = pdt
        maior_qtd = qtd
        menos_vendido = pdt
        menor_qtd = qtd
        pdt_caro = vu
        pdt_barato = vu
        desc_mais = pdt
        desc_menos = pdt
    else:
        if vu > pdt_caro:
            pdt_caro = vu
            desc_mais = pdt
        if qtd > maior_qtd:
            maior_qtd = qtd
            mais_vendido = pdt
        if vu < pdt_barato:
            pdt_barato = vu
            desc_menos = pdt
        if qtd < menor_qtd:
            menor_qtd = qtd
            menos_vendido = pdt
        if resp == 'S':
            break
print('¨' * 50)
print(f'Produto mais vendido: {mais_vendido}...... {maior_qtd} unidades')
print(f'Produto menos vendido: {menos_vendido}...... {menor_qtd} unidades')
print('¨' * 50)
print(f'Produto mais caro: {desc_mais}...... R${pdt_caro:.2f}')  #desc_mais = descrição do mais caro
print(f'Produto mais barato: {desc_menos}...... R${pdt_barato:.2f}')   #desc_menos = descrição do mais barato
print('¨' * 50)
print(f'Valor total de vendas: {soma:.2f}')
print('¨' * 50)
print('FIM')