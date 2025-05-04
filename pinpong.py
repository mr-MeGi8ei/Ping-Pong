from pygame import *

win_width, win_height = 800, 600
window = display.set_mode((win_width, win_height))
display.set_caption("PingPong")
background = transform.scale(image.load("background.png"), (win_width, win_height))


game = True
finish = False
clock = time.Clock()
fps = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background, (0,0))


    display.update()
    clock.tick(fps)
    