#Construa um programa que calcule.
#Quanto tempo demora para um funcionário chegar a um salário de 10.000
#Salário inicial 2.000 aumento de 10% ao ano.

salario = 2000
aumento = 0.1
tempo = 0
meta = 10000

while salario < meta:
    salario = salario * (1 + aumento)
    tempo = tempo + 1

print (tempo)
