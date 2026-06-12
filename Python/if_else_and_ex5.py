# Qual deve ser o bônus do funcionário?
# Se a empresa tem a meta de vendas de 10.000 e o funcionário meta de 1.000
# Bonus = 250 , Se não 50
#Se meta da empresa não for atingida, bonus 0

Vendas = 1200
meta = 1000
vendas_empresa = 11000
Meta_empresa = 10000

if vendas_empresa > Meta_empresa:
    if Vendas > meta:
        bonus = 250
    else:
        bonus = 50
else:
    bonus = 50

print(bonus)
