

import torch
import cv2
import numpy as np


# Defina o caminho correto para o arquivo de pesos
model_path = r'C:\Users\best.pt'

# Carregar o modelo treinado
model = torch.hub.load('C:/Users/yolov5', 'custom', path=model_path, source='local')

# Definir as classes (certifique-se de que estão na mesma ordem do arquivo data.yaml)
classes = ['ônibus simples', 'ônibus duplo', 'ônibus 2 eixos', 'ônibus 3 eixos']

# Função para detectar e classificar ônibus em uma imagem
def detect_and_classify_bus(image_path):
    # Carregar a imagem
    image = cv2.imread(image_path)
    if image is None:
        print("Erro ao carregar a imagem.")
        return

    # Redimensionar a imagem e normalizar
    image_resized = cv2.resize(image, (640, 640))  # Redimensionar para o tamanho esperado pelo modelo
    image_rgb = cv2.cvtColor(image_resized, cv2.COLOR_BGR2RGB)  # Converter BGR para RGB


    # Transformar a imagem em um tensor
    image_tensor = torch.from_numpy(image_rgb).float().unsqueeze(0).permute(0, 3, 1, 2) / 255.0  # Mudar de [batch, H, W, C] para [batch, C, H, W]

    # Fazer a inferência com o modelo YOLOv5
    results = model(image_tensor)

    # Obter as saídas
    detections = results[0].cpu().numpy()  # Converta para numpy array

    # Verificar se há detecções e processar
    if detections.size == 0:
        print("Nenhuma detecção encontrada.")
        return

    print("Formato dos resultados da detecção:")
    print(detections.shape)
    print(detections[:10])  # Exibir as primeiras 10 detecções para diagnóstico

    # Converter a imagem para RGB (para exibição)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Identificar e classificar ônibus
    detected_any = False
    for detection in detections:
        if len(detection) >= 6:  # Certifique-se de que há pelo menos 6 colunas
            x1, y1, x2, y2, conf, class_index = detection[:6]

            # Verificar se a confiança é maior que o limite
            if conf > 0.9:  # Ajuste o limite de confiança
                detected_any = True
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                class_index = int(class_index)  # Converter o índice da classe para inteiro

                # Desenhar o retângulo e a classe na imagem
                cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(image, f'{classes[class_index]} {conf:.2f}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                # Salvar a imagem com a classificação
                output_path = f'output01_image_{classes[class_index].replace(" ", "_")}.jpg'
                cv2.imwrite(output_path, cv2.cvtColor(image, cv2.COLOR_RGB2BGR))  # Converter de RGB para BGR para salvar

                print(f'Imagem salva em: {output_path}')

    if not detected_any:
        print("Nenhuma detecção com confiança suficiente foi encontrada.")

# Caminho para a imagem local
image_path = r'C:\Users\onibus\03.jpg'  # Substitua pelo caminho da sua imagem

# Executar a função de detecção e classificação
detect_and_classify_bus(image_path)

