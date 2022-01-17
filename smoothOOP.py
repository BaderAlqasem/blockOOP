import pygame
import random

#Image stuff
displaySurface = pygame.display.set_mode((1000, 600))
player = pygame.image.load("playerBlock.jpg").convert()
scaledPlayer = pygame.transform.scale(player, (20, 20)).convert()
pizza = pygame.image.load("foodBlock.png").convert()
scaledPizza = pygame.transform.scale(pizza, (20, 20)).convert()

clock = pygame.time.Clock()

class Food:
    #Self is food
    def __init__(self, screen):
        self.screen = screen
        self.image = scaledPizza
        self.x = 1
        self.y = 1
        
    def draw(self):
        #add food to screen 
        self.screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1,25)* 20
        self.y = random.randint(1,20)* 20
        
class Snake:
    #Snake is self
    def __init__(self, screen):
        self.screen = screen
        self.player = scaledPlayer
        self.x = 100
        self.y = 100
        self.direction = 'down'

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def walk(self):
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
        self.screen.fill((110, 110, 5))

        self.screen.blit(self.player, (self.x, self.y))
        pygame.display.flip()

class Game:
    #Self is game
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 600))
        self.snake = Snake(self.surface)
        self.snake.draw()
        self.food = Food(self.surface)
        self.food.draw()
        
    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + 20:
            if y1 >= y2 and y1 < y2 + 20:
                return True
        return False
    
    def display_score(self):
        score = 0
        if self.is_collision(self.snake.x, self.snake.y, self.food.x, self.food.y):
            score +=1
            print(score)
            self.food.move()
        
        font = pygame.font.SysFont('arial',30)
        score = font.render(f"Score: {score}",True,(200,200,200))
        self.surface.blit(score,(850,10))
        
    def play(self):
        self.snake.walk()
        self.food.draw()
        self.display_score()
        pygame.display.flip()
        
        if self.is_collision(self.snake.x, self.snake.y, self.food.x, self.food.y):
            self.food.move()

    def run(self):
        loop = True

        while loop:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        loop = False

                    if event.key == pygame.K_LEFT:
                        self.snake.move_left()

                    if event.key == pygame.K_RIGHT:
                        self.snake.move_right()

                    if event.key == pygame.K_UP:
                        self.snake.move_up()

                    if event.key == pygame.K_DOWN:
                        self.snake.move_down()

                elif event.type == pygame.QUIT:
                    loop = False

            self.play()
            clock.tick(60)

game = Game()
game.run()