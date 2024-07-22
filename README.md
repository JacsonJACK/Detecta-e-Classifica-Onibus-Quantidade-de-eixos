# QtdEixos

Detecção e Classificação de Ônibus em Imagens com Python e YOLOv5
Este repositório contém um script Python para detectar e classificar ônibus em imagens usando o modelo YOLOv5 pré-treinado.

Funcionalidades:

Carrega um modelo YOLOv5 pré-treinado.
Detecta objetos de classe "ônibus" em uma imagem.
Classifica os ônibus detectados em diferentes categorias (por exemplo, "ônibus simples", "ônibus duplo").
Desenha caixas delimitadoras e rótulos de classe nas imagens.
Salva as imagens com os resultados da classificação em um diretório de saída.
Requisitos:

Python 3.6 ou superior
pip
OpenCV
NumPy
Torch
Modelo YOLOv5 pré-treinado (incluído no repositório)
Uso:

Clone o repositório para o seu computador.
Instale as dependências usando o comando pip install -r requirements.txt.
Substitua o caminho para a imagem de entrada na variável image_path no script detect_and_classify_bus.py.
Execute o script usando o comando python detect_and_classify_bus.py.
As imagens com os resultados da classificação serão salvas no diretório output.

Modelo Pré-Treinado:

O modelo YOLOv5 pré-treinado usado neste script está incluído no repositório no diretório models/yolov5s.pt. Este modelo foi treinado em um conjunto de dados de imagens de ônibus de diversas categorias.

Observações:

A precisão da detecção e classificação pode variar dependendo da qualidade e do tipo de imagem de entrada.
Você pode ajustar o limite de confiança na função detect_and_classify_bus para controlar a sensibilidade da detecção.
Este script é um exemplo básico e pode ser adaptado para outras tarefas de detecção de objetos.
Contribuições:

Sinta-se à vontade para contribuir com este projeto reportando bugs, sugerindo melhorias ou criando pull requests com suas próprias modificações.

Licença:

Este projeto está licenciado sob a licença MIT.

