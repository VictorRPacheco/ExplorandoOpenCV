# ExplorandoOpenCV
Trabalho 1 da matéria de "Princípios da visão computacional" do professor "Teófilo E. de Campos" da Universidade de Brasília

## Trabalho feito e testado em uma Oracle VM Virtual Box com:
* Versão VM 6.0.4
* Versão OS: Ubuntu 16.04 LTS 64-bits
* Versão Python: 2.7
* Versão OpenCV: 3.2.0

## Para facilitar a correção os nomes dos arquivos correspondem aos requisitos do trabalho:
* Requisito 1
	Elabore uma aplicação utilizando OpenCV que abra um arquivo de imagem (do tipo JPG) e que permita ao usuário clicar com o botão esquerdo do mouse sobre um ponto na área da imagem e mostre no terminal a coordenada do ponto (row,column) na imagem, informando os valores do pixel RGB, quando a imagem for colorida ou o valor da intensidade do pixel quando a imagem for em nível de cinza (greyscale).
	
* Requisito 2
	Repita o procedimento desenvolvido no Requisito 1 e crie uma rotina de seleção de pixels baseado na cor de onde for clicado.
	Seu programa deve comparar o valor da cor (ou tom de cinza) de todos os pixels da imagem com o valor da cor (ou tom de cinza) de onde foi clicado.
	Se a diferença entre esses valores for menor que 13, marque o pixel com a cor vermelha e exiba o resultado na tela.
	Observação: no caso de imagens de tons de cinza, use valor absoluto da diferença. No caso de imagens coloridas, use a distância Euclidiana no espaço tridimensional de cores para calcular essa "diferença".

* Requisito 3
	Repita o procedimento desenvolvido no Requisito 2, em que ao invés de abrir uma imagem, abra um arquivo de vídeo (padrão avi ou x264) e realize os mesmos procedimentos do Requisito 2 durante toda a execução do vídeo.
	Cada vez que o usuário clica na imagem, o valor de referência deve ser atualizado.
	
* Requisito 4
	Repita o procedimento desenvolvido no Requisito 3, em que ao invés de abrir um arquivo de vídeo, a aplicação abra o streaming de vídeo de uma webcam ou câmera USB conectada ao computador e realize todos os procedimentos solicitados no requisito 3.
	
	
## Para executar o código:
	Para conseguir rodar o código em sua máquina é necessário possuir Python2 e OpenCV3 instalados. Além disso é nessário uma webcam para os código do Requisito4
	Na pasta /src rode o comando pelo terminal:
	```
		python RequisitoX.py
	```
	Sendo X o número referente ao código que se deseja executar

## Autor

* **VictorRPacheco** - *Autor* - [VictorRPacheco](https://github.com/VictorRPacheco)

