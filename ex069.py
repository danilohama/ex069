"""Crie um programa que leia a IDADE e o SEXO de várias pessoas cadastradas, O programa deverá perguntar se o usúario
quer ou não continuar no final, Mostre:
A - quantas pessoas tem mais de 18 anos
B - Quantos homens foram cadastrados
C - quantas mulheres tem menos de 20 anos
"""
totM20 = totH = total18 = 0
while True:
    print('==' * 20)
    print('         CADASTRO DE PESSOAS')
    print('==' * 20)
    idade = int(input('Qual sua idade? '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if total18 >= 18:
            total18 += 1
        if sexo == 'M':
            totH += 1
        if sexo == 'F' and idade < 20:
            totM20 += 1
    print('--' * 20)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('quantas pessoas tem mais de 18 anos: {}'.format(total18))
print('Ao todo temos {} homens cadastrados'.format(totH))
print('E temos {} mulheres com menos de 20 anos'.format(totM20))
