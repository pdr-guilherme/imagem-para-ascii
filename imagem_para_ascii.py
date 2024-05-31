"""Imagem Para ASCII

Este módulo fornece ferramentas para converter imagens em representações ASCII.

"""

import argparse

from PIL import Image

CHARS = '`^",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'


def brilho_para_indice(brilho: int) -> int:
    """
    Transforma um valor de brilho entre 0 e 255 para um índice entre 0 e 64.

    Argumentos:
        brilho: Um valor inteiro entre 0 e 255.

    Retorno:
        indice: Um valor inteiro entre 0 e 64.
    """
    if brilho == 0:
        indice = 0
    else:
        indice = int(brilho / 255 * 64)
    return indice


def redimensionar_imagem(imagem: Image.Image) -> Image.Image:
    """
    Redimensiona uma imagem para que ela tenha 120 pixeis de largura, mantendo a proporção original dela.

    Argumentos:
        imagem: Uma instância de PIL.Image que representa a imagem a ser redimensionada.

    Retorno:
        imagem_redimensionada: Uma nova instância de PIL.Image que representa a imagem redimensionada.
    """
    nova_largura = 120
    percentual_largura = nova_largura / imagem.width
    nova_altura = int(float(imagem.height) * float(percentual_largura))
    imagem_redimensionada = imagem.resize((nova_largura, nova_altura))
    return imagem_redimensionada


def gerar_matriz_brilho(local_imagem: str) -> list[list[int]]:
    """
    Gera uma matriz bidimensional de uma imagem, em que cada elemento é um valor entre 0 e 255.

    Argumentos:
        local_imagem: O caminho para a imagem.

    Retorno:
        matriz_brilho: Uma matriz bidimensional de valores de brilho.
    """
    imagem = Image.open(local_imagem).convert("RGB")
    if imagem.width > 120:
        imagem = redimensionar_imagem(imagem)

    matriz_brilho = []
    for y in range(imagem.height):
        linha = []
        for x in range(imagem.width):
            pixel = imagem.getpixel((x, y))
            r = pixel[0]
            g = pixel[1]
            b = pixel[2]
            brilho = int(0.21 * r + 0.72 * g + 0.07 * b)
            linha.append(brilho)
        matriz_brilho.append(linha)
    return matriz_brilho


def mostrar_imagem(local_imagem: str) -> None:
    """
    Mostra a imagem no terminal utilizando um conjunto de caractéres pré-definidos.

    Argumentos:
        local_imagem: O caminho para a imagem.
    """
    matriz_brilho = gerar_matriz_brilho(local_imagem)
    for linha in matriz_brilho:
        for pixel in linha:
            indice = brilho_para_indice(pixel)
            print(CHARS[indice], end="")
        print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Converte imagens em arte ASCII.",
    )
    parser.add_argument(
        "imagem", type=str, help="Caminho para a imagem a ser convertida"
    )
    args = parser.parse_args()
    mostrar_imagem(args.imagem)
