# Mensagem de boas-vindas
print("Bem-vindo à calculadora!")

# Entrada de valores e operador
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
operador = input("Selecione a operação (+, -, *, /): ")

# Função para realizar a operação
def operacao(valor1, valor2, operador):
    if operador == '+':
        resultado = valor1 + valor2
        print("Resultado:", resultado)
        return resultado
    elif operador == '-':
        resultado = valor1 - valor2
        print("Resultado:", resultado)
        return resultado
    elif operador == '/':
        if valor2 != 0:
            resultado = valor1 / valor2
            print("Resultado:", resultado)
            return resultado
        else:
            print("Erro: Divisão por zero não é permitida.")
            return None
    elif operador == '*':
        resultado = valor1 * valor2
        print("Resultado:", resultado)
        return resultado
    else:
        print("Erro: Operador inválido.")
        return None

# Chamada da função com os valores fornecidos
operacao(valor1, valor2, operador)
