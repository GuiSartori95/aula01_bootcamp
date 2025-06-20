CONSTANTE_BONUS = 1000
# 1) Solicita ao usuário que digite seu nome
nome_usuario = input("Digite seu nome: ")

# 2)Solicita ao usuário que digite o valor do seu salário
#Converte a entrada para um número de ponto flutuante
salario_usuario = float(input("Digite o seu salário: "))

# 3) Solicita ao usuário que digite o valor do bônus recebido
#Converte a entrada para um número de ponto flutuante
bonus_usuario = float(input("Digite seu bônus: "))

# 4) Calcule o valor do bônus final
valor_do_bonus = CONSTANTE_BONUS + salario_usuario * bonus_usuario

#Imprime a mensagem personalizada incluindo o nome do usário e o valor
print(f"O usuário {nome_usuario} possui o bonus de {valor_do_bonus}")

#Bônus: Quantos bugs e riscos você consegue identificar nesse programa?