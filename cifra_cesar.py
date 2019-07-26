escolha = int(input("""
[1] - Encriptar mensagem
[2] - Descriptar mensagem
Escolha:
"""))
#opção 1
if (escolha == 1):
  def cesar_encriptar(chave, letra):
    ascii = ord(letra) #função ord utilizada para pegar o seu parâmetro na tabela ascii
    if ascii >=97 and ascii <= 122: #checagem para ver se o parâmetro da letra (minuscula foi utilizado) encaixa-se apenas no limite do alfabeto
      novo_ascii = ascii + chave #colocado para uma nova variavel o número da letra + o parametro de encritação
      while(novo_ascii < 97 or novo_ascii > 122): #se quando somada a chave ao parâmetro ele ultrapassar o limite do alfabeto, é decrescido o número de letras do alfabeto ou acrescentado.
        if novo_ascii > 122:
          novo_ascii = novo_ascii - 26
        if novo_ascii < 97:
          novo_ascii = novo_ascii + 26
      return chr(novo_ascii)
    else:
      return letra #se o índice que está sendo verificado for outro símbolo, o mesmo será mantido.
  #entrada de dados
  chave = int(input('chave da cifra: '))
  letra = input('Frase ou letra: ')

  lista_aux = []
  for letra in list(letra): #colocada todas as letras dentro de uma lista para formar a frase
    lista_aux.append(cesar_encriptar(chave, letra)) #quando é para realizar a encritação da frase, a chave é positiva, para Descriptar a chave é negativa

  encriptado = ''.join(lista_aux) #junta-se todos os índices para formar a frase
  print(encriptado)
#opção 2
elif (escolha == 2):
  def cesar_descriptar(chave, letra):
    ascii = ord(letra)
    if ascii >=97 and ascii <= 122:
      novo_ascii = ascii + chave
      while(novo_ascii < 97 or novo_ascii > 122):
        if novo_ascii > 122:
          novo_ascii = novo_ascii - 26
        if novo_ascii < 97:
          novo_ascii = novo_ascii + 26
      return chr(novo_ascii)
    else:
      return letra
  chave = int(input('chave da cifra: '))
  letra = input('Frase ou letra: ')

  lista_aux = []
  for letra in list(letra):
    lista_aux.append(cesar_descriptar(-chave, letra))

  descriptado = ''.join(lista_aux)
  print(descriptado)
#opção fora do range
else:
  print('Opção inválida.')
