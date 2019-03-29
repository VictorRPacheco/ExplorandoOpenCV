# Codigo para detectar e destacar cores similares
"""
-> Abre uma imagem
-> Quando clicado na imagem ideintifica onde foi o clique
-> Idenfica a cor de onde foi clicado
-> Calcula as cores similares a ela e detaca-as de vermelho
Rode o codigo com -> python Requisito2.py
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


# Escolha da imagem
image = cv2.imread("../data/test.jpg")
cv2.namedWindow("Requisito2")
cv2.setMouseCallback("Requisito2", Cor_e_Posicao)

#image = np.zeros((400,400,3), dtype="uint8")


#image[np.where((image==[77,37,139]).all(axis = 2))] = [0,0,255]
#image[np.where(np.logical_and(LimiarBaixo <= image, image <= LimiarAlto))] = 0

cv2.imshow("Requisito2", image)
if cv2.waitKey() == ord('q'):
	cv2.destroyAllWindows()

# image[np.where((image==[0,0,0]).all(axis=2))] = [255,255,255]

cv2.destroyAllWindows()





