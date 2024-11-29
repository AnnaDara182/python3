#Print com o cumprimento da loja para o cliente.
print('Bem vindo(a) a fabrica de camisetas da Anna Dara Moraes Araujo\n')
#Função criada para a escolha do modelo da camiseta.
def escolha_modelo():
  while True:
    print('Escolha o modelo desejado: \nMCS - Manga Curta Simples\nMLS - Manga Longa Simples\nMCE - Manga Curta Estampada\nMLE - Manga Longa Estampada\n')
    camiseta = str(input('>> ')).upper()
    if camiseta == 'MCS':
      return 1.80
    elif camiseta == 'MLS':
      return 2.10
    elif camiseta == 'MCE':
      return 2.90
    elif camiseta == 'MLE':
      return 3.20
    else:
      print('Modelo inválido, tente novamente!\n')
#Função criada para a escolha da quantia de camisetas.
def num_camisetas():
  while True:
    try:
      quantidade = float(input('Insira a quantidade de camisetas: '))
      if quantidade < 20:
        return quantidade
      elif quantidade >= 20 and quantidade < 200:
        return quantidade - quantidade * 0.05
      elif quantidade >= 200 and quantidade < 2000:
        return quantidade - quantidade * 0.07
      elif quantidade >= 2000 and quantidade <= 20000:
        return quantidade - quantidade * 0.12
      else:
        print('Não aceitamos essa quantidade de camisetas em um pedido!\nFavor escolher a quantia novamente!\n')
    except ValueError:
      print('Erro! Favor inserir uma quantia válida')
#Função criada para saber o tipo de frete.
def frete():
  entrega = 0
  while True:
    print('\nOpções de frete: \n1 - Transportadora - R$100,00\n2 - Sedex - R$200,00\n0 - Retirar na fábrica - Sem custo adicional\n')
    entrega = float(input('Escolha a opção da entrega: '))
    if entrega == 1:
      return 100.00
    elif entrega == 2:
      return 200.00
    elif entrega == 0:
      return 0.00
    else:
      print('Opção de frete inválida, escolha outra opção!\n')
    break

#Programa principal.
camiseta = escolha_modelo()
quantidade = num_camisetas()
entrega = frete()
total = (camiseta*quantidade) + entrega
#Impressão final mostrando pro cliente o valor total e o valor de cada ação separadamente.
print(f'\nTotal a pagar: R${total:.2f} (Modelo: {camiseta:.2f} * Quantidade (com desconto): {quantidade:.2f} + Frete: {entrega:.2f})')