#Construa um programa que calcule.
#Qual seria o salário de um funcionário após 10 anos, se todo ano ele ganhasse um aumento de 10%
#Salário inicial 2.000

Salario = 2000
Aumento = 0.1
Tempo = 10

for i in range(Tempo):
    Salario = Salario* (1 + Aumento)
print(Salario)

