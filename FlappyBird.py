import pygame as game
import os
import random

import pygame.image

#Frame de exibição
telaLargura = 500
telaAltura  = 800

#Importando as imagens
imageCano  = pygame.transform.scale2x(pygame.image.load("/Users/PedroVitorPereira/Documents"
                         "/GitHub/Python_Projects/Flappy-Bird/imagens/pipe.png"))

imagemChao = pygame.transform.scale2x(pygame.image.load("/Users/PedroVitorPereira/Documents"
                        "/GitHub/Python_Projects/Flappy-Bird/imagens/base.png"))
imagemFundo  = pygame.transform.scale2x(pygame.image.load("/Users/PedroVitorPereira/Documents"
                            "/GitHub/Python_Projects/Flappy-Bird/imagens/bg.png"))


##As imagems do passaroa para dar a impressão de estar voando será
# necessário utilizar uma lista que pegue esses vetores.
imagemPassaro = pygame.transform.scale2x(pygame.image.load("/Users/PedroVitorPereira/"
        "Documents/GitHub/Python_Projects/Flappy-Bird/imagens/bird1.png"))






