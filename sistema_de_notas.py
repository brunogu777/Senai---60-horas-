print("SISTEMA NOTA")
print ('...' * 10 )

nome_aluno = input('Nome do aluno: ')

n1_port = float(input('Nota portugues: '))
n2_mat = float(input('Nota matematica: '))
n3_ing = float(input('Nota ingles: '))


media = (n1_port + n2_mat + n3_ing/3)

print('SITUAÇÃO DO ALUNO: ')
aprovado = media > 7
reprovado = media < 5
recuperado = media >=5 and media < 7
print (nome_aluno, 'Aprovado? - ', aprovado)
print (nome_aluno, 'Reprovado? - ', reprovado)
print (nome_aluno, 'Recuperação? - ', recuperado)


