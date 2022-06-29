
##GENERAL:
# Jogadores: DE 2 Á 3 
# Número de dados: 5 de 6 faces
# Objetivo: Atingir a maior pontuação.
# 13 Rodadas:

# cada rodada o jogador PODE jogaR os dados 3 vezes:
# 	1x - Obrigatório jogar todos os dados
# 	2x - pode escolher quantos dados quer jogar
# 	3x - pode escolher quantos dados quer jogar

##CHAMAR A RODADA:


import random
from statistics import mode


def chamarRodada():
  j = 0
  nDados = 5
  jogada1 = jogarDado(nDados)
  j += 1
  print(jogada1)
  for n in range(0,2):
    answer01 = input("Você gostaria de jogar novamente?\n[S/N]\nR:")
    if answer01 in "Ss":
      j += 1
      nDados = int(input("Quantos dados você gostaria de jogar novamente? "))
      if nDados == 1:
        delDados = int(input("Selecione o valor do dado que você gostaria de jogar novamente: "))
        jogada1.remove(delDados)
        jogada = jogarDado(nDados)
        jogada1 += jogada
        print(jogada1)

      elif nDados == 2:
        n1 = (int(input("Digite o valor a ser deletado e pressione enter: ")))
        n2 = (int(input("Digite o valor a ser deletado e pressione enter:")))
        jogada1.remove(n1)
        jogada1.remove(n2)
        jogada = jogarDado(nDados)
        jogada1 += jogada
        print(jogada1)

      elif nDados == 3:
        n1 = (int(input("Digite o valor a ser deletado e pressione enter: ")))
        n2 = (int(input("Digite o valor a ser deletado e pressione enter: ")))
        n3 = (int(input("Digite o valor a ser deletado e pressione enter: ")))
        jogada1.remove(n1)
        jogada1.remove(n2)
        jogada1.remove(n3)
        jogada = jogarDado(nDados)
        jogada1 += jogada
        print(jogada1)

      elif nDados == 4:
        n1 = (int(input("Digite o valor a ser deletado e pressione enter: ")))
        n2 = (int(input("Digite o valor a ser deletado e pressione enter: ")))
        n3 = (int(input("Digite o valor a ser deletado e pressione enter: ")))
        n4 = (int(input("Digite o valor a ser deletado e pressione enter: ")))
        jogada1.remove(n1)
        jogada1.remove(n2)
        jogada1.remove(n3)
        jogada1.remove(n4)
        jogada = jogarDado(nDados)
        jogada1 += jogada
        print(jogada1)

      elif nDados == 5:
        jogada1 = jogarDado(nDados)
        print(jogada1)

    else:
      break
  if j == 3:
    print("Esta foi a sua última jogada!\nEscolha a sua pontuação da rodada:")
  return jogada1

##JOGAR O DADO:
def jogarDado(nDados):
  jogada = []
  start = input("Jogue os dados pressionando ENTER:")
  dado = [1,2,3,4,5,6]
  for i in range (0,nDados):
    elemento = random.choice(dado)
    jogada.append(elemento)
  return jogada

## PONTUAÇÃO DAS RODADAS:
def pontuacaoRodada(answer02,jogada1):
  lista1 = []
  count = 0
  sequenciaAlta = [2,3,4,5,6]
  sequenciaBaixa = [1,2,3,4,5]
  if answer02 in "1": ##soma todos os dados que deram o mesmo valor nas três jogadas
    repetido = mode(jogada1)
    for c, n in enumerate(jogada1):
      if n == repetido:
        count += 1
    totalRodada = int(repetido * count)
    return totalRodada
  elif answer02 in "2": ##Caso haja três dados do mesmo valor na jogada serão marcados 20 pontos
    answer02 = 2
    repetido = mode(jogada1)
    for c, n in enumerate(jogada1):
      if n == repetido:
        count += 1
    if count == 3:
      totalRodada = 20
      return totalRodada
    print('Sua pontuação não foi validada!\nEscolha uma nova opção!')
    totalRodada = 0
    return totalRodada
  elif answer02 in "3": ##Caso haja quatro dados do mesmo valor na jogada, serão marcados 30 pontos
    repetido = mode(jogada1)
    for c, n in enumerate(jogada1):
      if n == repetido:
        count += 1
    if count == 4:
      totalRodada = 30
      return totalRodada
    print('Sua pontuação não foi validada!\nEscolha uma nova opção!')
    totalRodada = 0
    return totalRodada
  elif answer02 in "4": ##Full House: caso hajam 3 dados de um mesmo valor e 2 dados também com o mesmo valor:
    repetido = mode(jogada1)
    for c, n in enumerate(jogada1):
      if n == repetido:
        count += 1
    if count == 3:
      for n in (jogada1):
        if n != repetido:
          lista1.append(n)
    x = len(set(lista1)) == 1
    if x:
      totalRodada = 25
      return totalRodada
    print('Sua pontuação não foi validada!\nEscolha uma nova opção!')
    totalRodada = 0
    return totalRodada
  elif answer02 in "5": ##Sequência alta: caso haja a sequência de 2 à 6 na mesa;
      if jogada1 == sequenciaAlta:
        totalRodada = 30
        return totalRodada
      print('Sua pontuação não foi validada!\nEscolha uma nova opção!')
      totalRodada = 0
      return totalRodada
  elif answer02 in "6": ##Sequência baixa: caso haja a sequência de 1 à 5 na mesa;
    if jogada1 == sequenciaBaixa:
      totalRodada = 30
      return totalRodada
    print('Sua pontuação não foi validada!\nEscolha uma nova opção!')
    totalRodada = 0
    return totalRodada
  elif answer02 in "7": ##General: caso todos os dados deem o mesmo valor;
    x = len(set(jogada1)) == 1
    if x:
      totalRodada = 50
      return totalRodada
    print('Sua pontuação não foi validada!\nEscolha uma nova opção!')
    totalRodada = 0
    return totalRodada
  elif answer02 in "8": ##Aleatória: É marcada a soma dos cinco dados;
    totalRodada = sum(jogada1)
    return totalRodada

##RESULTADO POR JOGADA:
def resultadoRodada(jgdr,totalRodada): 
    print(f"O jogador (a) {jgdr} conquistou nessa rodada: {totalRodada} pontos!")
#resultadoRodada(jogador01,totalRodada)

##CHAMAR TABELA DE PONTUAÇÃO:
def chamarMenu():
  print("TIPOS DE PONTUAÇÃO:\n1. Jogada de mesmo valor:\n2. Trinca:\n3. Quadra:\n4. Full House:\n5. Sequência Alta:\n6. Sequência Baixa:\n7. General:\n8. Aleatória:")
  answer02 = input("Qual o tipo de pontuação da rodada? ")
  if answer02 in "1,2,3,4,5,6,7,8":
    return answer02
  else:
    print("Número Inválido!\nDigite novamente!")

##CHAMAR MENU INICIAL
def chamarMenu_Inicial():
  print(("-="*30),"\n",(" "*10),"1-2-3","###JOGO GENERAL###","4-5-6",(" "*10))
  print((" "*18),"Teste a sua sorte",(" "*18))
  print(("=-"*30),"\n",("=-"*30))
  print(("  "*8),"SEJAM BEM VINDOS",("  "*15))
  print(" Preparem seus copinhos e dados virtuais para se divertirem!")
  start = input(">>>>Vamos Começar a Diversão?      [Pressione ENTER!]")
  print("-="*30)

chamarMenu_Inicial()
numJogador = int(input("Quantos Jogadores vão se divertir hoje?"))
jogador01 = input("Insira o nome do primeiro jogador(a): ")
jogador01_pontos = []
jogador02= input("Insira o nome do segundo jogador(a): ")

jogador02_pontos = []
if numJogador == 3:
  jogador03 = input("Insira o nome do terceiro jogador(a): ")
  jogador03_pontos = []
print("Let's go!")

rodada = 0
j = 0
while rodada <= 2:  ##A regra do jogo solicita 13 rodadas: para tal, alterar a linha 191 para: "While rodada <= 13:"
  rodada +=1
  ##RODADA PARA O PRIMEIRO JOGADOR:
  if rodada == 1:
    print(f"Hora do jogador(a) {jogador01} iniciar!")
  else: 
    print(f"Agora é a vez do jogador(a) {jogador01}:")
  jogada1 = chamarRodada()
  answer02 = chamarMenu()
  totalRodada = pontuacaoRodada(answer02,jogada1)  
  if totalRodada == 0:
    answer02 = chamarMenu()
    totalRodada = pontuacaoRodada(answer02,jogada1)
  total = resultadoRodada(jogador01,totalRodada)
  jogador01_pontos.append(totalRodada)

  ##RODADA DO SEGUNDO JOGADOR:
  print(f"Agora é a vez do jogador(a) {jogador02}: ")
  jogada1 = chamarRodada()
  answer02 = chamarMenu()
  totalRodada = pontuacaoRodada(answer02,jogada1)
  if totalRodada == 0:
    answer02 = chamarMenu()
    totalRodada = pontuacaoRodada(answer02,jogada1)
  total = resultadoRodada(jogador02,totalRodada)
  jogador02_pontos.append(totalRodada)

  #RODADA DO TERCEIRO JOGADOR (SE APLICÁVEL):
  if numJogador == 3:
    print(f"Agora é a vez do jogador (a): {jogador03}")
    jogada1 = chamarRodada()
    if j == 3:
      print("Esta foi a sua última jogada!\Escolha a sua pontuação da rodada:")
    answer02 = chamarMenu()
    totalRodada = pontuacaoRodada(answer02,jogada1)
    if totalRodada == 0:
      answer02 = chamarMenu()
      totalRodada = pontuacaoRodada(answer02,jogada1) 
    total = resultadoRodada(jogador03,totalRodada)
    jogador03_pontos.append(totalRodada)
##PONTUAÇÃO FINAL E DEFINIÇÃO DO VENCEDOR:
pontosfinais = []
print("Resultado do jogo!\n")
jogador01_final= sum(jogador01_pontos)
jogador02_final = sum(jogador02_pontos)

if jogador01_final > jogador02_final:
    vencedor = jogador01
else:
  vencedor = jogador02
if numJogador == 3:
  jogador03_final = sum(jogador03_pontos)
  if jogador01_final < jogador03_final > jogador02_final:
    vencedor1 = jogador03
    vencedor = vencedor1
print("TABELA DE PONTUAÇÃO:")
print(jogador01, ":", jogador01_final)
print(jogador02, ":", jogador02_final)
if numJogador == 3:
  print(jogador03, ":", jogador03_final)
print(("-="*30),"\n",(" "*10),"1-2-3","###JOGO GENERAL###","4-5-6",(" "*10))
print((" "*18),"PARABÉNS", vencedor,(" "*18))
print(("=-"*30),"\n",("=-"*30))


