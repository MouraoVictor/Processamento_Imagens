import cv2
import numpy as np

imagem = cv2.imread("C:/Users/tinho/OneDrive/Imagens/WallPapers/teste.png")

if imagem is None:
    print("Erro ao carregar a imagem")
else:
    print("Carregando...")

    imagem_redimensionada = cv2.resize(imagem, None, fx=0.35, fy=0.35)

    gray = cv2.cvtColor(imagem_redimensionada, cv2.COLOR_BGR2GRAY)

    ret, binary_img = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    kernel = np.ones((5,5), np.uint8)

    erosion = cv2.erode(gray, kernel, iterations=1)
    dilation = cv2.dilate(gray, kernel, iterations=1)
    gradiente = cv2.subtract(dilation, erosion)

    cv2.imshow("Original", imagem_redimensionada)
    cv2.imshow("Gradiente Morfologico", gradiente)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
