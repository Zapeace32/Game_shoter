from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
x1 = 596
y1 = 393

class Enemy(GameSprite):
    side = 'left'
    def update(self):
        if self.rect.x <= 690:
            self.side = 'right'
        if self.rect.x >= win_width - 82:
            self.side = 'left'
        if self.side == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
 
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
#окно игры
win_height = 1000
win_width = 1000
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
w1 = Wall(83,55,162,100,90,100,10)
player_speed = 10

font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0))
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()



background = transform.scale(image.load("background.jpg"),(win_height, win_width))
ghost = Player('hero.png', 5, win_height -  80, 4)
monster = Enemy('cyborg.png', 700, win_height - 260, 2)
money = GameSprite('treasure.png', 770,win_height -  270, 5)


game = True
clock = time.Clock()
FPS = 60
while game:
    window.blit(background,(0, 0))
        
    ghost.update()
    monster.update()
    
    ghost.reset()
    monster.reset()
    
    w1.draw_wall()
    for e in event.get():
        if e.type == QUIT:
            game = False
    if sprite.collide_rect(ghost, monster) or sprite.collide_rect(ghost, w1): 
        window.blit(lose,(200,200))
        finish = True
        
    if sprite.collide_rect(ghost, money):
        window.blit(win,(200,200))
        finish = True
        
    display.update()
    clock.tick(FPS)
