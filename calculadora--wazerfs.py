from math import sqrt
from time import sleep
print(''' \033[32mCalculadora WazerFs\033[m
\nEscolha uma opção: 
[ 1 ] Soma por quantidade
[ 2 ] Tabuada
[ 3 ] Raiz Quadrada
[ 4 ] Divisão
[ 5 ] Compra com desconto ''')
opc = int(input('\nEscolha uma opção: '))
if opc == 1:
	print('''
[ 1 ] Soma simples
[ 2 ] Soma 6 valores ''')
	op = int(input('\nOpção: '))
	if op == 1:
		soma = 0
		cont = 0
		for c in range(1, 3):
			mat = int(input('\nDigite o {} valor: '.format(c)))
			soma += mat
			cont += 1
		print('Sua soma deu {}'.format(soma))
	elif op == 2:
			soma = 0
			cont = 0
			for m in range(1, 7):
				mt = int(input('\nDigite o {} valor: '.format(m)))
				soma += mt
				cont += 1
				print('\nSua soma resultou em {} '.format(soma))
elif opc == 2:
	nu = int(input('\nDigite um número para a tabuada: '))
	print('___'*12)
	for tb in range(1, 11):
		print('\n\033[36m{} x {:2} = {}\033[m'.format(nu, tb, nu * tb))
	print('___'*12)
elif opc == 3:
	nru = float(input('\nDigite um valor pra saber a raiz quadrada: '))
	print('\nA raiz quadrada de {:.0f} \ne igual a {:.2f} '.format(nru, sqrt(nru)))
elif opc == 4:
	nmu = float(input('\nDigite um valor pra ser  dividido: '))
	dv = float(input('Digite o numero pra dividir: '))
	print('\nA divisão de {} \ne igual a {}'.format(nmu, nmu / dv))
elif opc == 5:
	print('\033[33mEssa opção vai vim na v2\033[m')
else:
	print('\033[31mOpção Inválida, Tente Novamente\033[m')
		