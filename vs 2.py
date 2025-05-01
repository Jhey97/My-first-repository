print("bem vindo a calculadora!")
valor1 = float(input("digite o primeiro valor:"    ))
valor2 = float(input("digite o segundo valor:"   ))
operador = input("entre com a operacao: +, -, /, * "   )

#funçao de operacao
def operacao(valor1, valor2, operador):
    if operador == '+':
        resultado = valor1 + valor2
        print("resultado:", resultado)
        return resultado
    elif operador == "-":
        if valor2 != 0:
         resultado = valor1 - valor2
        print("resultado:", resultado)
        return resultado
    elif operador == "/":
         if valor2 != 0:
          resultado = valor1 / valor2
         print("resultado:", resultado)
         return resultado
    elif operador == "*":
        resultado = valor1 * valor2
        print("resultado:", resultado)
        return resultado
    else:
        print("nao divisivel por zero, refaça operaçao")
        return None
#chamada de funçao
operacao(valor1, valor2, operador)

