# EXERCÍCIOS 1: 
# Utilize condicionais

# Acessar a Aula - 8

# 1* 
# Peça para o usuário digitar um número, verifique se um número é positivo, 
# negativo ou zero.
numero = int(input("Digite um número: "))

if numero > 0:
    print("O número é positivo")
elif numero < 0:
    print("O número é negativo")
else:
    print("O número é zero")



# 2*

# Peça para o usuário digitar a idade, verifique se uma pessoa pode votar com 
# base na idade.
idade = int(input("Digite sua idade: "))

if idade >= 16:
    print("Pode votar")
else:
    print("Não pode votar")



# 3*

# Declara uma variável com um número qualquer, 
# determine se um número é par ou ímpar.
numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print("O número é par")
else:
    print("O número é ímpar")




# 4*

# Usuário vai digitar 3  números, para criar um triângulo, verifique se um triângulo 
# é equilátero, isósceles ou escaleno
lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))

if lado1 == lado2 == lado3:
    print("Triângulo Equilatero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Triângulo Isosceles")
else:
    print("Triângulo Escaleno")




# Um triângulo é chamado de equilátero se todos os lados possuem a mesma medida. 
# Um triângulo é chamado de isósceles se dois lados possuem a mesma medida. 
# Um triângulo é chamado de escaleno se todos os lados possuem medidas diferentes.

# 5*

	# Determine se um número é múltiplo de 5 e 7.
numero = int(input("Digite um número: "))

if numero % 5 == 0 and numero % 7 == 0:
    print("É múltiplo de 5 e 7")
else:
    print("Não é múltiplo de 5 e 7")






# 6*

# Verifique se um número é positivo e maior que 10
numero = int(input("Digite um número: "))

if numero > 10:
    print("O número é positivo e maior que 10")
else:
    print("O número não atende às condições")




# 7*

# Verifique se um número é divisível por 3 ou 5.
numero = int(input("Digite um número: "))

if numero % 3 == 0 or numero % 5 == 0:
    print("O número é divisível por 3 ou 5")
else:
    print("O número não é divisível por 3 nem por 5")




