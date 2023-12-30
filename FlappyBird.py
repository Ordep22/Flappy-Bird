import pygame as game
import os
import random

import pygame.image

# Frame de exibição
telaLargura = 500
telaAltura = 800

# Importando as imagens
imageCano = pygame.transform.scale2x(pygame.image.load(os.path.join("Images", "pipe.png")))
imagemChao = pygame.transform.scale2x(pygame.image.load(os.path.join("Images", "base.png")))
imagemFundo = pygame.transform.scale2x(pygame.image.load(os.path.join("Images", "bg.png")))

##As imagems do passaroa para dar a impressão de estar voando será
# necessário utilizar uma lista que pegue esses vetores.
imagemPassaro = [pygame.transform.scale2x((pygame.image.load(os.path.join("Images", "bird1.png")))),
                 pygame.transform.scale2x((pygame.image.load(os.path.join("Images", "bird2.png")))),
                 pygame.transform.scale2x((pygame.image.load(os.path.join("Images", "bird3.png"))))]

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
        self.imagem = imagemPassaro[0]

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

        self.y += 1

        # Restringir o angulo do passaro
        if deslocamento < 0 or self.y < (self.altura + 50):
            if self.angulo < self.rotacaoMaxima:
                self.angulo = self.rotacaoMaxima
        else:
            if self.angulo > -90:
                self.angulo -= self.velocidadeRotacao

    def desenhar(self,tela):
        #definir qual imagem do passaro vai usar
        self.contagemImagem += 1

        if self.contagemImagem < self.tempoAnimacao:
            self.imagem = self.imagens[0]

        elif self.contagemImagem < self.tempoAnimacao*2:
            self.imagem = self.imagens[1]

        elif self.contagemImagem < self.tempoAnimacao*3:
            self.imagem = self.imagens[2]

        elif self.contagemImagem < self.tempoAnimacao*4:
            self.imagem = self.imagens[1]

        elif self.contagemImagem < self.tempoAnimacao*4 + 1:
            self.imagem = self.imagens[0]
            self.contagemImagem = 0



        #Se o passaro estiver caindo o passaro não vai bater asa
        if self.angulo <= -80:
            self.imagem = self.imagens[1]
            self.contagemImagem = self.tempoAnimacao*2



        #Desenhar a imgem
        imagemRotacionada = pygame.transform.rotate(self.imagem,self.angulo)
        coordenadaCentro  = self.imagem.get_rect(topleft = (self.x,self.y)).center
        retangulo  = imagemRotacionada.get_rect(center = coordenadaCentro)
        tela.blit(imagemRotacionada,retangulo.topleft)

    def GetMask(self):

             return pygame.mask.from_surface(self.imagem)

class Cano:

    distancia  = 200

    velocidade  = 5

    def __init__(self, x):

        self.x = x
        self.altura  = 0
        self.posTopo = 0
        self.posBase = 0
        self.canoTopo = pygame.transform.flip(imageCano,False,True)
        self.canoBase = imageCano
        self.passou = False
        self.DefinirAltura()

    def DefinirAltura(self):
        self.altura  = random.randrange(50,450)
        self.posTopo = self.altura - self.canoTopo.get_height()
        self.posBase = self.altura + self.distancia

    def mover(self):

        self.x -= self.velocidade

    def desenhar(self,tela):
        tela.blit(self.canoTopo,(self.x,self.canoTopo))
        tela.blit(self.canoBase, (self.x, self.canoBase))

    def colidir(self,passaro):

        pass
        '''
        passaroMask = passaro.GetMask()
        #topoMask = pygame.mask.from_surface(self.canoTopo)
        #baseMask = pygame.mask.from_surface(self.canoBase)

        distanciaTopo = (self.x - passaro.x, self.posTopo - round(passaro.y))
        distanciaBase = (self.x - passaro.x, self.posBase - round(passaro.y))

        #Este parâmetro é verdadeiro quando exite um ponto de colisão do cano com o Topo
        #topoPonto = passaroMask.overlap(baseMask,distanciaTopo)

        # Este parâmetro é verdadeiro quando exite um ponto de colisão do cano com a Base
        #basePonto = passaroMask.overlap(baseMask,distanciaBase)


        if basePonto or basePonto:
            return True
        else:
            return False

        
        '''

class Chao:

        velocidade  = 5

        largura  = imagemChao.get_height()

        imagem = imagemChao

        def __init__(self,y):
            self.y = y
            self.x1 = 0
            self.x2 = self.largura

        def Mover(self):

            self.x0 -= self.velocidade

            self.x2 -= self.velocidade

            if self.x1 + self.largura < 0:

                self.x1 += self.largura

            elif self.x2 + self.largura < 0:

                self.x2 += self.largura


        def desenhar(self,tela):

            tela.blit(self.imagem,(self.x1,self.y))

            tela.blit(self.imagem, (self.x2, self.y))



def desenharTela(tela, passaros, canos, chao, pontos):

        #Desenhando o fundo do jogo
        tela.blit(imagemFundo,(0,0))

        #Desenhando os passaros com base no array de passaros
        for passaro in passaros:
            passaro.desenhar(tela)

        #Desenhando os canos na tela
        for cano in canos:
            cano.desenhar(tela)

        texto = fontPontos.render(f"Pontos:{pontos}", 1, (0,0,0))
        tela.blit(texto,(telaLargura-10 - texto.get_height(), 10))

        chao.desenhar(tela)

        pygame.display.update()

def main(removerCanos=None):

    passaros  = [Passaro(300,200)]

    chao = Chao(730)

    canos = [Cano(700)]

    tela = pygame.display.set_mode((telaLargura,telaAltura))

    pontos = 0

    relogio = pygame.time.Clock()

    loop = True

    while loop:

        relogio.tick(30)

        for evento in pygame.event.get():
            #Se o botão de fechar for pressinado
            if evento.type == pygame.QUIT:
                    loop  = False
                    pygame.quit()
                    quit()

            #Se alguma tecla for pressionada
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    for passaro in passaros:
                        passaro.pular()

        for passaro in passaros:
            passaro.mover()
        #Chao.Mover()
        adicionarCano = False

        for cano in canos:
            for i, passaro in enumerate(passaros):
                if Cano.colidir(i,passaro):
                    passaros.pop(i)
                if not cano.passou and passaro.x > cano.x:
                        cano.passou = True
                        adicionarCano = True
            cano.mover()
            if cano.x + cano.canoTopo.get_width() < 0:
                removerCanos.append(cano)

        if adicionarCano:
            pontos += 1
            canos.append(Cano(600))

        for cano in removerCanos:
            canos.remove(cano)

        for i, passaro in enumerate(passaros):
            if (passaro.y + passaro.imagem.get_height()) > chao.y or (passaro.y + passaro.imagem.get_height()) < 0 :

                passaros.pop(i)

        desenharTela(tela,passaros,canos,chao,pontos)

if __name__ == "__main__":
    main()
















