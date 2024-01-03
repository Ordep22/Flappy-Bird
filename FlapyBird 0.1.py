import os
import random
import pygame.image
import pygame as game

# Screen size
screenHeight = 500
screenWidth = 800

# import images
pipeImage = pygame.transform.scale2x(pygame.image.load(os.path.join("Images", "pipe.png")))
floorImage = pygame.transform.scale2x(pygame.image.load(os.path.join("Images", "base.png")))
backgoundImage = pygame.transform.scale2x(pygame.image.load(os.path.join("Images", "bg.png")))

# Bird images
birdImage = [pygame.transform.scale2x((pygame.image.load(os.path.join("Images", "bird1.png")))),
             pygame.transform.scale2x((pygame.image.load(os.path.join("Images", "bird2.png")))),
             pygame.transform.scale2x((pygame.image.load(os.path.join("Images", "bird3.png"))))]

# Set the main font
pygame.font.init()
pontuationFont = pygame.font.SysFont("arial", 50, bold= True)


class Bird:
    Bird_Images = birdImage
    maxRotation = 25
    rotationVelocit = 20
    animationTime = 5

    def __init__(self,x,y):

        self.x = x
        self.y = y
        self.angule  = 0
        self.velocit = 0
        self.height = self.y
        self.time = 0
        self.imageCounting = 0
        self.image = self.Bird_Images[0]

    def JumpBird(self):
        self.velocit = -10.5
        self.time = 0
        self.height = self.y
    def MoveBird(self):
        self.time += 1
        displaciment = 1.5*(self.time**2) + self.velocit*self.time

        if displaciment > 16:
                  displaciment = 5

        elif displaciment < 0:
            displaciment -= 11

        self.y += displaciment

        if displaciment < 0 or self.y < (self.height + 50):
            if self.angule < self.maxRotation:
                self.angule = self.maxRotation
            else:
                if self.angule > -90:
                    self.angule -= self.rotationVelocit
    def DrawBird(self, screen):

        self.imageCounting += 1

        if self.imageCounting < self.animationTime:
            self.image = self.Bird_Images[0]
        elif self.imageCounting < self.animationTime * 2:
            self.image = self.Bird_Images[1]
        elif self.imageCounting < self.animationTime * 3:
            self.image = self.Bird_Images[2]
        elif self.imageCounting < self.animationTime * 4:
            self.image = self.Bird_Images[1]
        elif self.imageCounting >= self.animationTime * 4 + 1:
            self.image = self.Bird_Images[0]
            self.imageCounting = 0

        if self.angule <= -80:
            self.image = self.Bird_Images[1]
            self.imageCounting = self.animationTime*2


        rotadedImage = pygame.transform.rotate(self.image,self.angule)
        center_image = self.image.get_rect(topleft = (self.x,self.y)).center
        rectangle = rotadedImage.get_rect(center = center_image)
        screen.blit(rotadedImage,rectangle.topleft)
    def GetMasck(self):
        return pygame.mask.from_surface(self.image)


class Pipe:
    distance  = 200
    velocit = 5

    def __init__(self,x):
        self.x = x
        self.heigth = 0
        self.topPosition = 0
        self.basePosition = 0
        self.topPipe = pygame.transform.flip(pipeImage,False,True)
        self.basePipe = pipeImage
        self.way = False
        self.HeigthDefinition()

    def HeigthDefinition(self):
        self.heigth = random.randrange(50,450)
        self.topPosition = self.heigth - self.topPipe.get_height()
        self.basePosition = self.heigth + self.distance

    def MovePipe(self):
        self.x -= self.velocit
    def DrawPipe(self, screen):
        screen.blit(self.topPipe,(self.x, self.topPosition))
        screen.blit(self.basePipe, (self.x, self.basePosition))

    #Verify this point, becouse the mask collision its work only for top pipes!
    def PipeColision(self, bird):
        birdMasck = bird.GetMasck()
        topMasck = pygame.mask.from_surface(self.topPipe)
        baseMask = pygame.mask.from_surface(self.basePipe)

        topDistance  = (self.x - bird.x,self.topPosition - round(bird.y))
        baseDistance = (self.x - bird.x,self.topPosition - round(bird.y))

        topPoint = birdMasck.overlap(topMasck, topDistance)
        basePoint = birdMasck.overlap(baseMask, baseDistance)

        if topPoint or basePoint:
            return True
        else:
            return False


class Floor:
    velocit  = 5
    width = floorImage.get_width()
    image = floorImage

    def __init__(self,y):
        self.y = y
        self.x1 = 0
        self.x2 = self.width
    def MoveFloor(self):
        self.x1 -= self.velocit
        self.x2 -= self.velocit

        if self.x1 + self.width < 0:
            self.x1 = self.x2 + self.width
        if self.x2 + self.width < 0:
            self.x2 = self.x1 + self.width

    def DrawFloor(self, screen):
        screen.blit(self.image, (self.x1, self.y))
        screen.blit(self.image, (self.x2, self.y))


def DrawScreen(screen, birdes, pipes, floor, score):
    screen.blit(backgoundImage,(0,0))
    for bird in birdes:
        bird.DrawBird(screen)

    for pipe in pipes:
        pipe.DrawPipe(screen)

    text = pontuationFont.render(f"Score: {score}",1,(255,255,255))
    screen.blit(text,(screenWidth-10-text.get_width(),10))
    floor.DrawFloor(screen)
    pygame.display.update()


def main():
    birdes = [Bird(230,350)]
    floor  = Floor(730)
    pipes = [Pipe(700)]
    screen  = pygame.display.set_mode((screenHeight,screenWidth))
    score = 0
    time  = pygame.time.Clock()
    running = True

    while running:
        time.tick(30) #30 milliseconds

        for event in pygame.event.get():

            #Exit from application
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()

            #KEYDOWN is an event  ocour whem a button is pressure
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    for bird in birdes:
                        bird.JumpBird()



        for bird in birdes:
            bird.MoveBird()
        floor.MoveFloor()

        addPipe  = False
        removePipe = []

        for pipe in pipes:
            for i, bird in enumerate(birdes):

                if pipe.PipeColision(bird):
                    birdes.pop(i)
                if not pipe.way and bird.x > pipe.x:
                    pipe.way = True
                    addPipe = True
            pipe.MovePipe()
            if pipe.x + pipe.topPipe.get_width() < 0:
                removePipe.append(pipe)

        if addPipe:
            score += 1
            pipes.append(Pipe(600)) # I need to understand it better

        for pipe in removePipe:
            pipes.remove(pipe)

        for i, bird in enumerate(birdes):
            if (bird.y + bird.image.get_height()) > floor.y or bird.y < 0:
                birdes.pop(i)

        DrawScreen(screen, birdes, pipes, floor, score)










if __name__ == '__main__':
    main()