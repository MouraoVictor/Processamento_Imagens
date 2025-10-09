import cv2
import numpy as np

# Captura a imagem
caminho_da_imagem = "porsche.jpg"
imagem = cv2.imread(caminho_da_imagem)

# Verificação se Lê a imagem corretamente
if imagem is None:
    print("Erro: A imagem não foi encontrada ou não pôde ser carregada.")
else:
    print("Imagem carregada com sucesso! Prosseguindo com as operações.")

    # Redimensiona a imagem
    imagem_redimensionada = cv2.resize(imagem, None, fx=0.35, fy=0.35)
#    imagem_redimensionada = cv2.resize(imagem, None, fx=1, fy=1)

    # Converte a imagem para tons de cinza
    gray_img = cv2.cvtColor(imagem_redimensionada, cv2.COLOR_BGR2GRAY)

    # Tranforma a imagem em preto e branco (binária)
    ret, binary_img = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)

    # Cria o Kernel
    kernel = np.ones((5, 5), np.uint8)

    # Realização da função
    dilation = cv2.dilate(gray_img, kernel, iterations=1)

    # Exibir os resultados
    cv2.imshow('Original', gray_img)
    cv2.imshow('Dilatacao', dilation)
    print("A Dilatação expande as áreas de cor clara em uma imagem binária.")

    # Fechamento
    cv2.waitKey(0)
    cv2.destroyAllWindows()