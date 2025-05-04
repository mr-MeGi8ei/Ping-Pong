from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_img, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_img), (size_x, size_y))
        self.speed = player_speed
        #каждый спрайт должен хранить свойство rect
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()#получаем состояние клавиш
# проверка нажатия на определенную клавишу и выход за границу окна
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_r(self):
        keys_pressed = key.get_pressed()#получаем состояние клавиш
# проверка нажатия на определенную клавишу и выход за границу окна
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

win_width, win_height = 800, 600
window = display.set_mode((win_width, win_height))
display.set_caption("PingPong")
background = transform.scale(image.load("background.png"), (win_width, win_height))

game = True
finish = False
clock = time.Clock()
fps = 60

racket_l = Player('racket_l.png', 25, 400, 10, 80, 100)
racket_r = Player('racket_r.png', 700, 200, 10, 80, 100)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background, (0,0))
        racket_l.update_l()
        racket_r.update_r()
        racket_l.reset()
        racket_r.reset()

    display.update()
    clock.tick(fps)
