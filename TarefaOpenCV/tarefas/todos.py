import cv2
import numpy as np

caminho_da_imagem = 'C:/Users/tinho/OneDrive/Imagens/WallPapers/teste.png'
imagem = cv2.imread(caminho_da_imagem)

# Verificação se Lê a imagem corretamente
if imagem is None:
    print("Erro: A imagem não foi encontrada ou não pôde ser carregada.")
else:
    print("Imagem carregada com sucesso! Prosseguindo com as operações.")

    # Redimensiona a imagem
    imagem_redimensionada = cv2.resize(imagem, None, fx=0.35, fy=0.35)

    # Converte a imagem para tons de cinza
    gray_img = cv2.cvtColor(imagem_redimensionada, cv2.COLOR_BGR2GRAY)

    # Tranforma a imagem em preto e branco (binária)
    ret, binary_img = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)

    # Cria o Kernel
    kernel = np.ones((5, 5), np.uint8)

    # Realização das funções
    erosion = cv2.erode(gray_img, kernel, iterations=1)
    dilation = cv2.dilate(gray_img, kernel, iterations=1)
    opening = cv2.morphologyEx(gray_img, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(gray_img, cv2.MORPH_CLOSE, kernel)

    # Exibir os resultados
    cv2.imshow('Original', gray_img)
    cv2.imshow('Erosao', erosion)
    cv2.imshow('Dilatacao', dilation)
    cv2.imshow('Abertura', opening)
    cv2.imshow('Fechamento', closing)

    # Fechamento
    cv2.waitKey(0)
    cv2.destroyAllWindows()