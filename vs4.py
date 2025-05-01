class Carro:
    def __init__(self, modelo, ano, combustivel):
        self.modelo = modelo 
        self.ano = ano
        self.combustivel = combustivel

    def tipo_de_carro(self):
        print(f"esse carro e um:{self.modelo}")
        print(f'{self.ano}: foi sua fabricaçao!')
        print(f'utiliza {self.combustivel}')
# entrada de dados 

#coleta de dados
informacoes = []
while True:
  modelo = input("insira seu modelo: \n  "  )
  ano = input("insira o ano de fabricaçao: \n  " )
  combustivel = input("insira o tipo de combustivel: \n")
  novo_carro = Carro(modelo, ano, combustivel)
  informacoes.append(novo_carro)

  continuar = input("deseja continuar inserindo dados? (s/n)"  )
  if continuar.lower() == 'n'  :
    print("obrigado!")
    break # interrompendo coleta

#Exibiçao!
print("\n informaçoes dos carros:")
for carro in informacoes:
    carro.tipo_de_carro()


            
            