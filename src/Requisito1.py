# Codigo para identificar cliques e indicar cores
'''
-> Abre uma imagem
-> Quando clicado na imagem ideintifica onde foi o clique
-> Exibe as coordenadas [X,Y] do clique no terminal
-> Exibe a cor do pixel selecionado em RGB para imagens coloridas e a intensidade para imagens em nivel de cinza
Rode o codigo com -> python Requisito1.py
Para rodar o codigo eh necessaria uma pasta ../data com um arquivo test.jpg

Para sair pressione 'q'
'''

import cv2
clickPoint = []

def mouse_click(event, x, y, flags, param):
	global clickPoint

	if event == cv2.EVENT_LBUTTONDOWN:
		clickPoint = [x, y]

		# Print da posicao
		print('----------------------')
		print('Posicao [X, Y]:')
		print(y, x)
		
		# Print da cor
		color = (image[y,x])
		#Identidica se a imagem eh em tons de cinza
		if color[0] == color[1] == color[2]:
			print('Intensidade do pixel')
			print(color[0])
		else:
			print('Cor RGB')
			print(color)

# Escolha da imagem
image = cv2.imread('../data/test.jpg')
cv2.namedWindow("Requisito1")
cv2.setMouseCallback("Requisito1", mouse_click)
while True:
	cv2.imshow("Requisito1", image)
	if cv2.waitKey(20) & 0xFF == ord('q'):
		break

cv2.destroyAllWindows()
