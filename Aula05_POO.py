
#  Exercício 1: Faça um programa que leia dados do usuário (nome, sobrenome, idade)
#  Adcione em uma lista seus elementos na tela.

exercicio = int(input('Digite o exercío que você quer executar 1 ou 2: ')) # Referente a questão Extra++: (Faça um menu onde o usuário consiga selecionar qual questão quer executar). 

if exercicio == 1:
    
    nome = input('Digite o nome: ')
    sobrenome = input('Digite o sobrenome: ')
    idade = input('Digite a idade: ')

    lista1 = [nome, sobrenome, idade]
    print(lista1)


else:

# Exercício 2: Faça um programa onde o usuário informe um número de 1 a 12 em seguida imprima qual o mês que se refere.

    numeros = int(input('Digite um número de 1 ao 12 referente ao mês: '))
    lista_mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Nutubro','Novembro','Dezembro']
    numeros = numeros - 1
    print(lista_mes[numeros])




 
