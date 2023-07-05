import secrets
import pygame

pygame.init()

game_window = pygame.display.set_mode(size=(800, 500))
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Ping Pong')


class Player(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.width = 20
        self.height = 70
        self.speed = 0
        self.score = 0
        self.rect = pygame.Rect(x_pos, y_pos, self.width, self.height)

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), self.rect, 0)

    def update(self):
        if self.rect.y <= 5:
            self.rect.y = 5
        elif self.rect.y >= 425:
            self.rect.y = 425
        self.rect.y += self.speed


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x_pos = 368
        self.y_pos = 218
        self.speed_x = 0
        self.speed_y = 0
        self.movement = False
        self.image = pygame.image.load('ball.png')
        self.rect = pygame.Rect(self.x_pos, self.y_pos, 50, 50)

    def draw(self, surface):
        surface.blit(self.image, (self.x_pos, self.y_pos))

    def update(self):
        if self.y_pos <= 0:
            self.speed_y = -self.speed_y
        elif self.y_pos >= 436:
            self.speed_y = -self.speed_y

        if self.x_pos <= -64:
            player2.score += 1
            self.__init__()
        elif self.x_pos >= 800:
            player1.score += 1
            self.__init__()

        self.x_pos += self.speed_x
        self.y_pos += self.speed_y

        self.rect.x = self.x_pos + 7
        self.rect.y = self.y_pos + 7


player1 = Player(20, 215)
player2 = Player(760, 215)
ball = Ball()

font = pygame.font.SysFont('calibri', 23, False, False)

pygame.mixer.music.load('bg_music.mp3')
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()

running = True
while running:

    clock.tick(60)

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player1.speed = -12
            elif event.key == pygame.K_s:
                player1.speed = 12

            if event.key == pygame.K_UP:
                player2.speed = -12
            elif event.key == pygame.K_DOWN:
                player2.speed = 12

            if event.key == pygame.K_SPACE:
                ball.movement = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                player1.speed = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player2.speed = 0

    # Game Logic
    player1.update()
    player2.update()
    if ball.movement:
        ball.speed_x = secrets.choice([-10, 10])
        ball.speed_y = secrets.choice([-10, -8, -6, 6, 8, 10])
        ball.movement = False

    ball.update()

    if pygame.sprite.collide_rect(ball, player2):
        ball.speed_x = -10
    if pygame.sprite.collide_rect(ball, player1):
        ball.speed_x = 10

    # Rendering the Graphics
    game_window.fill((69, 90, 170))
    pygame.draw.line(game_window, (255, 255, 255), (400, 0), (400, 500), 1)

    player1.draw(game_window)
    player2.draw(game_window)

    ball.draw(game_window)

    text = font.render(f"{player1.score} - SCORE - {player2.score}", True, (119, 153, 198))
    game_window.blit(text, (347, 10))

    # Updating the Display
    pygame.display.flip()

pygame.quit()