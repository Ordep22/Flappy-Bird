import pygame as game
import os
import random

import pygame.image

# Frame de exibição
telaLargura = 500
telaAltura = 800

# Importando as imagens
imageCano = pygame.transform.scale2x(pygame.image.load(os.path.join("imagens", "pipe.png")))

imagemChao = pygame.transform.scale2x(pygame.image.load(os.path.join("imagens", "base.png")))

imagemFundo = pygame.transform.scale2x(pygame.image.load(os.path.join("imagens", "bg.png")))

##As imagems do passaroa para dar a impressão de estar voando será
# necessário utilizar uma lista que pegue esses vetores.
imagemPassaro = [pygame.transform.scale2x((pygame.image.load(os.path.join("imagens", "bird1.png")))),
                 pygame.transform.scale2x((pygame.image.load(os.path.join("imagens", "bird2.png")))),
                 pygame.transform.scale2x((pygame.image.load(os.path.join("imagens", "bird3.png"))))]

pygame.font.init()

fontPontos = pygame.font.SysFont("arial", 50, bold=True)


class Passaro:
    imagens = imagemPassaro

    # Animações da movimentação de passaro

    rotacaoMaxima = 25

    velocidadeRotacao = 20

    tempoAnimacao = 5

    def __init__(self, x, y):

        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidade = 0
        self.altura = self.y
        self.tempo = 0
        self.contagemImagem = 0
        self.imagem = imagens[0]

    def pular(self):
        self.velocidade = -10.5
        self.tempo = 0
        self.altura = self.y

    def mover(self):
        # Quando devemos deslocar o passaro
        self.tempo += 1
        deslocamento = 1.5 * (self.tempo ** 2) + self.velocidade * self.tempo

        # Restringir o deslocamento
        if deslocamento > 16:
            deslocamento = 16
        elif deslocamento < 16:
            #incremento de deslocamento para facilitar a jogabilidade
            deslocamento -= 2

    # Restringir o angulo do passaro


class Cano:
    pass


class Chao:
    pass
