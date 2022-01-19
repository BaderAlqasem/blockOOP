import pygame
import random
import sys

#Image stuff
screenHeight = 600
screenWidth = 1000
displaySurface = pygame.display.set_mode((screenWidth, screenHeight))
player = pygame.image.load("playerBlock.jpg").convert()
scaledPlayer = pygame.transform.scale(player, (20, 20)).convert()
food = pygame.image.load("foodBlock.png").convert()
scaledFood = pygame.transform.scale(food, (20, 20)).convert()
obstacle = pygame.image.load("obstacle.png").convert()
scaledObstacle = pygame.transform.scale(player, (20, 20)).convert()

clock = pygame.time.Clock()

class Food:
    def __init__(self, screen):
        self.screen = screen
        self.image = scaledFood
        self.x = 500
        self.y = 300

    def draw(self):
        #Add food to screen 
        self.screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1,25)* 20
        self.y = random.randint(1,20)* 20
        print("moving")

class Obstacle:
    def __init__(self, screen):
        self.screen = screen
        self.image = scaledObstacle
        self.x = random.randrange(screenWidth)
        self.y = random.randrange(screenHeight)

    def draw(self):
        for i in range (10):
            self.screen.blit(self.image, (self.x, self.y))
            pygame.display.flip()

class Player:
    #Player is self
    def __init__(self, screen):
        self.screen = screen
        self.player = scaledPlayer
        self.x = 50
        self.y = 50
        self.direction = 'down'

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    #Player Speed
    def move(self):
        if self.direction == 'left':
            self.x -= 2.5
        if self.direction == 'right':
            self.x += 2.5
        if self.direction == 'up':
            self.y -= 2.5
        if self.direction == 'down':
            self.y += 2.5

        self.draw()

    def draw(self):
        self.screen.fill((0, 0, 0))

        self.screen.blit(self.player, (self.x, self.y))
        pygame.display.flip()

class Game:
    #Self is game
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((1000, 600))
        self.Player = Player(self.display)
        self.Player.draw()
        self.food = Food(self.display)
        self.food.draw()
        self.obstacle = Obstacle(self.display)
        self.obstacle.draw()
        
    def blocksCollide(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + 20 and y1 >= y2 and y1 < y2 + 20:
            return True
        return False
            
    def display_score(self):
        score = 0

        if self.blocksCollide(self.Player.x, self.Player.y, self.food.x, self.food.y):
            score +=1
            print(score)
            self.food.move()

        font = pygame.font.SysFont('arial',30)
        score = font.render(f"Score: {score}",True,(200,200,200))
        self.display.blit(score,(850,10))

    def gameOver(self):
        if self.blocksCollide(self.Player.x, self.Player.y, self.obstacle.x, self.obstacle.y):
            print("GAME OVER")
            sys.exit()

    def play(self):
        self.Player.move()
        self.food.draw()
        self.obstacle.draw()
        self.display_score()
        self.gameOver()
        pygame.display.flip()

        if self.blocksCollide(self.Player.x, self.Player.y, self.food.x, self.food.y):
            self.food.move()

    def run(self):
        loop = True

        while loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        loop = False
                        sys.exit()

                elif event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_a:
                        self.Player.move_left()

                    if event.key == pygame.K_d:
                        self.Player.move_right()

                    if event.key == pygame.K_w:
                        self.Player.move_up()

                    if event.key == pygame.K_s:
                        self.Player.move_down()
                    
                    elif event.type == pygame.QUIT:
                        loop = False

            self.play()
            clock.tick(60)

game = Game()
game.run()


#   obstacles, score and glitch and screen border