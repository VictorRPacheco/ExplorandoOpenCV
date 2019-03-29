# -*- coding: utf-8 -*-
# Codigo para detectar e destacar cores similares
"""
-> Abre uma imagem
-> Quando clicado na imagem ideintifica onde foi o clique
-> Idenfica a cor de onde foi clicado
-> Calcula as cores similares a ela e detaca-as de vermelho
Rode o codigo com -> python Trabalho.py
Para rodar o codigo eh necessaria uma pasta ../data com um arquivo test.jpg

Para sair pressione 'q'
"""

import cv2
import numpy as np
color = None


def Cor_e_Posicao(event, x, y, flags, param):
	global clickPoint
	global color

	if event == cv2.EVENT_LBUTTONDOWN:
		clickPoint = [x, y]
		color = image[y,x]
		print("----------------------")		
		#Identidica se a imagem eh em tons de cinza
		if color[0] == color[1] == color[2]:
			print"Posicao [X, Y]: ", (x, y), "Intensidade: ", color[0]
		else:
			print "Posicao [X, Y]: ", (x, y), "Cor: ", str(color)


print "╔═══════════════════════════════════════╗"
print "║	Escolha um dos requisitos	║"
print "╠═══════════════════════╦═══════════════╣"
print "║	Requisito 1	║ digite 1	║"
print "║	Requisito 2	║ digite 2	║"
print "║	Requisito 3	║ digite 3	║"
print "║	Requisito 4	║ digite 4	║"
print "║	Sair		║ digite 0	║"
flag = input("╚═══════════════════════╩═══════════════╝\n")

if flag == 1 or flag == 2:
	print "╔═══════════════════════════════════════╗"
	print "║	Escolha o arquivo de entrada	║"
	print "╠═════════════════════╦═════════════════╣"
	print "║ Imagem Colorida     ║ digite 1	║"
	print "║ Imagem P&B	      ║ digite 2	║"
	print "║ Escolher arquivo    ║ nome do arquivo	║"
	print "║	Sair	      ║ digite 0	║"
	file = raw_input("╚═════════════════════╩═════════════════╝\n")
	if file == '0':
		cv2.destroyAllWindows()
		flag = 0
	elif file == '1':
		image = cv2.imread("../data/test.jpg")
	elif file == '2':
		image = cv2.imread("../data/testPeB.jpg")
	else:
		try:
			image = cv2.imread(file)
		except:
			print "Arquivo inválido, abortando"
			cv2.destroyAllWindows()
	raw = image.copy()
	cv2.namedWindow("Trabalho")
	cv2.setMouseCallback("Trabalho", Cor_e_Posicao)


if flag == 1:
	print "╔═══════════════════════════════╗"
	print "║	Para sair pressione 'q'	║"
	print "╚═══════════════════════════════╝\n"
	cv2.imshow("Trabalho", raw)

if flag == 2:
	while True:
		cv2.imshow("Trabalho", raw)
		if color is not None:
		        # Separa as 3 cores
		        R = raw[:, :, 0].astype(np.float32)
		        G = raw[:, :, 1].astype(np.float32)
		        B = raw[:, :, 2].astype(np.float32)
		        raw = image.copy()
		        # Calcula quais pixels serão marcados com base na distância euclidiana para imagens coloridas
			if color[0] == color[1] == color[2]:
			        euclidiano = ((R - color[0]) ** 2) + ((G - color[1]) ** 2) + ((B - color[2]) ** 2)
			        mask = euclidiano < (13 ** 2)
			# Calcula a diferenca de intensidade para imagens em tons de cinza
			else:
				diferenca = abs(R - color[0])
				mask = diferenca < 13
			raw[np.where(mask)] = [0,0,255]
			color = None
		if cv2.waitKey(25) & 0xFF == ord('q'):
			cv2.destroyAllWindows()
			break

cv2.destroyAllWindows()





