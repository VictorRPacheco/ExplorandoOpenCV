# Codigo para identificar cliques e indicar cores
'''
-> Abre uma imagem
-> Quando clicado na imagem ideintifica onde foi o clique
-> Exibe as coordenadas [X,Y] do clique no terminal
-> Exibe a cor do pixel selecionado em RGB para imagens coloridas e a intensidade para imagens em nivel de cinza
Rode o codigo com -> python Requisito1.py
Para rodar o codigo eh necessaria uma pasta ../data com um arquivo test.jpg
'''

import cv2
clickPoint = []

def mouse_click(event, x, y, flags, param):
	global clickPoint

	if event == cv2.EVENT_LBUTTONDOWN:
		clickPoint = [x, y]
		print('Posicao [X, Y]:')
		print(clickPoint)

		X = clickPoint[0]
		Y = clickPoint[1]
		print('Cor:')
		color = (image[X,Y])
		print(color)

image = cv2.imread('../data/test2.jpg', 0)
cv2.namedWindow("Requisito1")
cv2.setMouseCallback("Requisito1", mouse_click)
while True:
	cv2.imshow("Requisito1", image)
	if cv2.waitKey(20) & 0xFF == ord('q'):
		break


# close all open windows
cv2.destroyAllWindows()
