from pygame import *
h = 1000
w = 700
font.init()
font = font.Font(None, 35)
lose1 =  font.render('PLAYER 1 LOSE!', True, (180, 0 ,0))
lose2 =  font.render('PLAYER 2 LOSE!', True, (180, 0 ,0))
win1 = font.render('PLAYER 2 WIN!', True, (0, 255, 0))
win2 = font.render('PLAYER 1 WIN!', True, (0, 255, 0))
back = (200, 255, 255)
display.set_caption('Ping-pong')
mw = display.set_mode((h,w))
mw.fill(back)
clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)

        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed


        self.rect = self.image.get_rect()
        self.rect.x =player_x
        self.rect.y = player_y


    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))



class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__(player_image, player_x, player_y, size_x, size_y, player_speed)
        
    def updater(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 30:
            self.rect.y += self.speed


    def updatel(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 80:
            self.rect.y += self.speed


racket1 = Player('rocket.png', 30, 200, 4, 50, 150)
racket2 = Player('rocket.png', 520, 200, 4, 50, 150)
ball = GameSprite('ball.png', 200, 200, 4, 50, 50)

speed_x = 3
speed_y = 3

score_1 = 0
score_2 = 0

finish = False

m = True
while m:
    for e in event.get():
        if e.type == QUIT:
            m = False

    if finish != True:
        mw.fill(back)
        racket1.updater()
        racket2.updatel()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        game_score = font.render(str(score_1)+'-'+str(score_2), True, (245, 215, 198))
        mw.blit(game_score, (200, 0))


        if sprite.collide_rect(racket1, ball) or  sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= 1

        if ball.rect.y > h-50 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
            score_1 += 1
        if score_1 >= 3:
            finish = True
            mw.blit(win1, (200, 200))
            mw.blit(lose1, (100, 200))
        else:
            ball.rect.x = 200
            ball.rect.y = 200


        if ball.rect.y < 0:
            score_2 += 1
        if score_2 >= 3:
            finish = True
            mw.blit(win2, (200, 200))
            mw.blit(lose2, (100, 200))
        else:
            ball.rect.x = 200
            ball.rect.y = 200


        racket1.reset()
        racket2.reset()
        ball.reset()


    display.update()
    clock.tick(FPS)