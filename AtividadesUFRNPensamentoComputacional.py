# contador = int(0)
# saldoConta = float(1000.00)
# print('R$', saldoConta)
#
# while(contador == 0):
#   print('1 SAQUE')
#   print('2 DEPOSITO')
#   print('3 SALDO')
#   valor = int(input('Selecione uma Opcao'))
#   if(valor == 1):
#     valorSaque = float(input('Selecione o valor desejado'))
#     if(saldoConta >= valorSaque):
#       saldoConta = saldoConta - valorSaque
#       print('R$', saldoConta)
#     else:
#       print('Saldo Insuficiente')
#     if(valor == 2):
#       valorDeposito = float(input('Qual o valor a ser depositado'))
#       if(valorDeposito > 0):
#         saldoConta = saldoConta + valorDeposito
#         print('R$', saldoConta)
#       else:
#         print('Valor invalido')
#
#     if(valor == 3):
#       print('R$', saldoConta)
#       print('Agradecemos por usar os nossos servicos')
#       contador = 2

# numeros = []
# contador = int(1)
# print('Digite 5 numeros:')
#
# while(contador <= 5):
#   numeros.append(int(input()))
#   contador += 1
#
#
# valor1 = int(0)
# valor2 = int(1)
# mostrarValor = int()
#
# contador2 = int(1)
# x = str()
# n1 = int()
# n2 = int()
#
# listaMostrar = []
# while(contador2 < 5):
#   if(numeros[valor1] <= numeros[valor2]):
#     mostrarValor = numeros[valor1]
#     while(mostrarValor <= numeros[valor2]):
#       listaMostrar.append(str(mostrarValor))
#       mostrarValor += 1
#   else:
#     mostrarValor = numeros[valor2]
#     while(mostrarValor <= numeros[valor1]):
#       listaMostrar.append(str(mostrarValor))
#       mostrarValor += 1
#   contador2 += 1
#
#   if(numeros[valor1] > numeros[valor2]):
#     n1 = str(numeros[valor2])
#     n2 = str(numeros[valor1])
#   else:
#     n1 = str(numeros[valor1])
#     n2 = str(numeros[valor2])
#
#   x = ', '.join(listaMostrar)
#   print('intervalo [{}, {}] = {}'.format(n1,n2,x))
#   x = str()
#   listaMostrar.clear()
#
#   valor1 += 1
#   valor2 += 1






# lista1 = ['Julio', 'Anna', 'Isabel', 'Izaac', 'Eduardo']
# nameCheck = str()
# x = str()
#
# print('A lista contem os seguintes nomes:')
# x = '\n'.join(lista1)
# print(x)
# nameCheck = input('Qual nome voce quer verificar?')
# try:
#   lista1.index(nameCheck)
#   print(' O nome {} esta na lista!'.format(nameCheck))
# except:
#   print(' O nome {} nao esta na lista!'.format(nameCheck))




# lista = []
# contador = int(1)
#
# while(contador <= 5):
#   print('Digite o numero:',contador)
#   valor = int(input())
#   lista.append(valor)
#   valor = int()
#   contador += 1
#
# contador = int(0)
# while(contador <= 4):
#   if((lista[contador] % 2) == 0):
#     print('O numero {} e par'.format(lista[contador]))
#   else:
#     print('O numero {} e impar'.format(lista[contador]))
#   contador += 1





# lista1 = ['Jupter', 'Saturno', 'Urano', 'Netuno', 'Plutao']
# x = '\n'.join(lista1)
# contador = int(1)
# nameDelet = str()
#
# while(contador == 1):
#   x = '\n'.join(lista1)
#   print('Os nomes da lista sao:')
#   print(x)
#   nameDelet = input('Qual nome deseja apagar?')
#   try:
#     lista1.remove(nameDelet)
#     x = '\n'.join(lista1)
#     print('{} foi apagado da lista!'.format(nameDelet))
#     print('Os nomes da lista sao:')
#     print(x)
#     contador = int(2)
#   except:
#     print('{} nao foi encontrado na lista!'.format(nameDelet))






# valor = int(input('Qual valor voce quer testar?'))
#
# def verifica(num):
#   r = num % 2
#   if(r == 0):
#     print('{} e par'.format(num))
#   else:
#     print('{} e impar'.format(num))
#
# verifica(valor)






# fatori = int(input('Qual numero voce gostaria de saber o fatorial?'))
#
# def fatorial(fat):
#   contador = int()
#   r = int()
#   contador = fat - 1
#   r = fat
#   while(contador > 0):
#     r = r * contador
#     contador -= 1
#   if (r == 0):
#     r = 1
#   print('{}! e {}'.format(fat, r))
#
# fatorial(fatori)





# print('Quais sao as notas?')
# x1 = float(input())
# x2 = float(input())
# x3 = float(input())
# resultado = float()
#
# typeM = input('Que tipo de media voce quer?')
#
# def aritimetica(v1,v2,v3):
#   r = float()
#   r = (x1 + x2 + x3)/ 3
#   return r
#
# def ponderada(v1,v2,v3):
#   r = float()
#   r = ((x1*5)+(x2*3)+(x3*2))/10
#   return r
#
# if(typeM == 'A'):
#    resultado = aritimetica(x1,x2,x3)
# else:
#   resultado = ponderada(x1,x2,x3)
#
# print('A media e: {}'.format(resultado))




# l1 = []
# l2 = []
# #----------------------------#
# contadorLista1 = int(input('Digite a quantidade de numeros que deseja incluir na Lista 1: '))
# counterL1D = contadorLista1
# while(contadorLista1 > 0):
#     rl1 = int(input('Digite um numero: '))
#     l1.append(rl1)
#     contadorLista1 -= 1
# #----------------------------#
# contadorLista2 = int(input('Digite a quantidade de numeros que deseja incluir na Lista 2: '))
# counterL2D = contadorLista2
# while(contadorLista2 > 0):
#     rl2 = int(input('Digite um numero: '))
#     l2.append(rl2)
#     contadorLista2 -= 1
# #----------------------------#
# def divide(p1,p2):
#     l3 = []
#     va = int()
#     TF = int()
#     TF2 = int(1)
#     for i in p1:
#         for j in p2:
#             if((j % i) == 0):
#                 TF = 1
#             else:
#                 TF = 0
#                 TF2 = 0
#         if(TF == 1 and TF2 == 1):
#             l3.append(i)
#     return l3
# resultado = []
# resultado = divide(l1,l2)
# if(divide(l1,l2) == []):
#     print('Nao foram encontrados valores da Lista 1 que dividem todos os valores da Lista 2!')
# else:
#     print('Os valores da Lista 1 que divide todos os valores de L2 sao:')
#     for i in resultado:
#         print(i)


# box = []
# box.append(int(input('n1?')))
# box.append(int(input('n2?')))
# box.append(int(input('n3?')))
# box.sort()
# n1 = box[0]
# n2 = box[1]
# n3 = box[2]
#
# if(n1 == n2 and n1 == n3):
#     print('todos sao iguais a {}'.format(box[0]))
# elif(n1 == n2 or n2 == n3):
#     if(n1 == n2):
#         print('maior: {}'.format(n1))
#         print('menor: {}'.format(n3))
#         print('nao ha elementos do meio')
#     else:
#         print('maior: {}'.format(n1))
#         print('menor: {}'.format(n2))
#         print('nao ha elementos do meio')
# else:
#     print('maior: {}'.format(n1))
#     print('menor: {}'.format(n2))
#     print('menor: {}'.format(n3))
