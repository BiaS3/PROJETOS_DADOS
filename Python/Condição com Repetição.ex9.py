#construa um programa que calcule. Tenho uma lista de preços de produtos, 
#todos os produtoos acima de R$5.000 vão ser reajustados em 5% e todos abaixo de R$5.000 em 10% 
# como ficam os preços dos produtos?

lista_precos =[100,6000,1000,1500]
reajuste_faixa1 = 0.05
reajuste_faixa2 = 0.1
corte_faixa = 5000
lista_reajustada = []
for preco in lista_precos:
    if preco > corte_faixa:
        novo_preco = round(preco * (1 + reajuste_faixa1), 2)
    else:
        novo_preco = round(preco * (1 + reajuste_faixa2), 2)
    lista_reajustada.append(novo_preco)
print(lista_reajustada)
