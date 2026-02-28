
#1 Peça ao usuário para inserir um número e manipule a exceção caso ele insira algo que não seja um número inteiro.
try:
    numero = int(input("Digite um número inteiro: "))
    print(f"Você digitou o número {numero}.")
except ValueError:
    print("Erro: Você não digitou um número inteiro válido.")

#2 Peça ao usuário para inserir dois números e realize uma divisão. Manipule a exceção caso ocorra erro de divisão por zero (ZeroDivisionError).

try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    resultado = num1 / num2
    print(f"O resultado da divisão é: {resultado}")
    
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")
except ValueError:
    print("Erro: Digite apenas números válidos.")



#3 Crie uma lista e peça um índice como entrada. Manipule a exceção caso o índice seja inválido.

lista = ["Python", "Java", "C++", "JavaScript"]

try:
    indice = int(input("Digite um índice da lista (0 a 3): "))
    print(f"O elemento no índice {indice} é: {lista[indice]}")
    
except IndexError:
    print("Erro: Índice inválido. Esse índice não existe na lista.")
except ValueError:
    print("Erro: Digite um número inteiro válido.")