#1) Função para comparar 2 números (par ou ímpar) – variáveis locais
def comparar_par_impar(num1, num2):
    # variáveis locais
    resultado1 = "par" if num1 % 2 == 0 else "ímpar"
    resultado2 = "par" if num2 % 2 == 0 else "ímpar"
    
    print(f"O número {num1} é {resultado1}")
    print(f"O número {num2} é {resultado2}")

#2) Função para multiplicar 3 números
def multiplicar(a, b, c):
    resultado = a * b * c  # variável local
    return resultado

print("Resultado:", multiplicar(2, 3, 4))

#3) Função para descobrir o valor elevado de um número
def calcular_potencia(base, expoente):
    resultado = base ** expoente
    return resultado

print("Resultado:", calcular_potencia(2, 3))  # 2³

#4) Função para mostrar mensagem se usuário digitar 18 anos
def verificar_idade(idade):
    if idade == 18:
        print("Você tem 18 anos! Parabéns pela maioridade!")
    else:
        print("Idade diferente de 18 anos.")

# Exemplo
verificar_idade(18)


#5) Função para descobrir a idade da pessoa
def calcular_idade(ano_nascimento, ano_atual):
    idade = ano_atual - ano_nascimento
    return idade

print("Sua idade é:", calcular_idade(2000, 2025))


#6) Função para verificar se o Brasil ganhou a Copa de 1999
def brasil_copa_1999():
    campeao_1999 = "França"  # variável local
    
    if campeao_1999 == "Brasil":
        print("O Brasil ganhou a Copa de 1999!")
    else:
        print("O Brasil NÃO ganhou a Copa de 1999.")

brasil_copa_1999()

#7) Sistema de Restaurante 

#Utilizando listas, loops e funções

# variável global
cardapio = ["Salada", "Macarronada", "Sanduíche", "Sorvete"]

# 1 - Função para cumprimentar
def cumprimentar():
    print("Seja bem-vindo ao nosso restaurante!")

# 2 - Função restaurante
def restaurante():
    while True:
        print("\nCardápio:")
        
        for i, item in enumerate(cardapio):
            print(f"{i + 1} - {item}")
        
        escolha = int(input("Escolha uma opção (0 para sair): "))
        
        if escolha == 0:
            print("Obrigado pela visita!")
            break
        elif 1 <= escolha <= len(cardapio):
            print(f"Você escolheu: {cardapio[escolha - 1]}")
        else:
            print("Opção inválida!")

# Executando o sistema
cumprimentar()
restaurante()

