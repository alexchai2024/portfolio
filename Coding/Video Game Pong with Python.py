import sys

import pygame

pygame.init()

font20 = pygame.font.Font('freesansbold.ttf', 35)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WIDTH, HEIGHT = 710, 275
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Selector")

clock = pygame.time.Clock() 
FPS = 30

def draw_start_screen(color):
    screen.fill(color)
    text = font20.render("Multiplayer Game Selector:", True, WHITE)
    textRect = text.get_rect()
    textRect.center = (WIDTH // 2, HEIGHT // 2)
    screen.blit(text, textRect)

    button1 = pygame.Rect(100, 200, 200, 50)
    pygame.draw.rect(screen, BLACK, button1)
    text = font20.render("Tic-Tac-Toe", True, WHITE)
    textRect = text.get_rect()
    textRect.center = button1.center
    screen.blit(text, textRect)

    button2 = pygame.Rect(400, 200, 200, 50)
    pygame.draw.rect(screen, BLACK, button2)
    text = font20.render("Pong", True, WHITE)
    textRect = text.get_rect()
    textRect.center = button2.center
    screen.blit(text, textRect)

    pygame.display.flip()

def tictactoe_game():
    WIDTH, HEIGHT = 300, 300
    LINE_WIDTH = 15
    BOARD_ROWS, BOARD_COLS = 3, 3
    SQUARE_SIZE = WIDTH // BOARD_COLS
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    LINE_COLOR = (0, 0, 0)

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tic-Tac-Toe")

    board = [['' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

    def draw_lines():
        pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)

    def draw_figures():
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if board[row][col] == 'X':
                    pygame.draw.line(screen, RED, (col * SQUARE_SIZE + 15, row * SQUARE_SIZE + 15),
                                     ((col + 1) * SQUARE_SIZE - 15, (row + 1) * SQUARE_SIZE - 15), LINE_WIDTH)
                    pygame.draw.line(screen, RED, ((col + 1) * SQUARE_SIZE - 15, row * SQUARE_SIZE + 15),
                                     (col * SQUARE_SIZE + 15, (row + 1) * SQUARE_SIZE - 15), LINE_WIDTH)
                elif board[row][col] == 'O':
                    pygame.draw.circle(screen, BLUE, (int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)), SQUARE_SIZE // 2 - 15, LINE_WIDTH)

    def mark_square(row, col, player):
        if board[row][col] == '':
            board[row][col] = player
            draw_figures()
            return True
        return False

    def check_win(player):
        for row in range(BOARD_ROWS):
            if board[row][0] == board[row][1] == board[row][2] == player:
                return True
        for col in range(BOARD_COLS):
            if board[0][col] == board[1][col] == board[2][col] == player:
                return True
        if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
            return True
        return False

    def check_draw():
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if board[row][col] == '':
                    return False
        return True

    def reset_game():
        screen.fill(WHITE)
        draw_lines()
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                board[row][col] = ''

    screen.fill(WHITE)
    draw_lines()

    player = 'X'
    player1_score = 0
    player2_score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX = event.pos[0]
                mouseY = event.pos[1]
                clicked_row = mouseY // SQUARE_SIZE
                clicked_col = mouseX // SQUARE_SIZE
                if mark_square(clicked_row, clicked_col, player):
                    if check_win(player):
                        if player == 'X':
                            player1_score += 1
                        else:
                            player2_score += 1
                        reset_game()
                        draw_lines()
                        if player1_score >= 3:
                            print("Player 1 wins!")
                            pygame.time.wait(3000)
                            reset_game()
                            player1_score = 0
                            player2_score = 0
                        elif player2_score >= 3:
                            print("Player 2 wins!")
                            pygame.time.wait(3000)
                            reset_game()
                            player1_score = 0
                            player2_score = 0
                    elif check_draw():
                        reset_game()
                        draw_lines()
                        print("It's a draw!")
                        pygame.time.wait(3000)
                    else:
                        player = 'O' if player == 'X' else 'X'

        draw_figures()
        pygame.display.update()

def pong_game():
    font20 = pygame.font.Font('freesansbold.ttf', 20)

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)

    WIDTH, HEIGHT = 700, 400
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pong")

    clock = pygame.time.Clock() 
    FPS = 30

    class Striker:
        def __init__(self, posx, posy, width, height, speed, color):
            self.posx = posx
            self.posy = posy
            self.width = width
            self.height = height
            self.speed = speed
            self.color = color
            self.geekRect = pygame.Rect(posx, posy, width, height)
            self.geek = pygame.draw.rect(screen, self.color, self.geekRect)

        def display(self):
            self.geek = pygame.draw.rect(screen, self.color, self.geekRect)

        def update(self, yFac):
            self.posy = self.posy + self.speed*yFac

            if self.posy <= 0:
                self.posy = 0
            elif self.posy + self.height >= HEIGHT:
                self.posy = HEIGHT-self.height

            self.geekRect = (self.posx, self.posy, self.width, self.height)

        def displayScore(self, text, score, x, y, color):
            text = font20.render(text+str(score), True, color)
            textRect = text.get_rect()
            textRect.center = (x, y)

            screen.blit(text, textRect)

        def getRect(self):
            return self.geekRect

    class Ball:
        def __init__(self, posx, posy, radius, speed, color):
            self.posx = posx
            self.posy = posy
            self.radius = radius
            self.speed = speed
            self.color = color
            self.xFac = 1
            self.yFac = -1
            self.ball = pygame.draw.circle(
                screen, self.color, (self.posx, self.posy), self.radius)
            self.firstTime = 1

        def display(self):
            self.ball = pygame.draw.circle(
                screen, self.color, (self.posx, self.posy), self.radius)

        def update(self):
            self.posx += self.speed*self.xFac
            self.posy += self.speed*self.yFac

            if self.posy <= 0 or self.posy >= HEIGHT:
                self.yFac *= -1

            if self.posx <= 0 and self.firstTime:
                self.firstTime = 0
                return 1
            elif self.posx >= WIDTH and self.firstTime:
                self.firstTime = 0
                return -1
            else:
                return 0

        def reset(self):
            self.posx = WIDTH//2
            self.posy = HEIGHT//2
            self.xFac *= -1
            self.firstTime = 1

        def hit(self):
            self.xFac *= -1

        def getRect(self):
            return self.ball

    def main():
        running = True

        geek1 = Striker(20, 0, 10, 100, 10, GREEN)
        geek2 = Striker(WIDTH-30, 0, 10, 100, 10, GREEN)
        ball = Ball(WIDTH//2, HEIGHT//2, 7, 9, WHITE)

        listOfGeeks = [geek1, geek2]

        geek1Score, geek2Score = 0, 0
        geek1YFac, geek2YFac = 0, 0

        countdown_text = font20.render("3", True, WHITE)
        screen.blit(countdown_text, (WIDTH // 2 - 10, HEIGHT // 2 - 40))
        instructions_text = font20.render("Instructions:", True, WHITE)
        screen.blit(instructions_text, (WIDTH // 2 - 60, HEIGHT // 2 - 10))
        geek1_instructions_text = font20.render("W and S for left player", True, WHITE)
        screen.blit(geek1_instructions_text, (WIDTH // 2 - 160, HEIGHT // 2 + 20))
        geek2_instructions_text = font20.render("Up and Down arrow keys for right player", True, WHITE)
        screen.blit(geek2_instructions_text, (WIDTH // 2 - 240, HEIGHT // 2 + 50))
        win_condition_text = font20.render("First to 5 points wins", True, WHITE)
        screen.blit(win_condition_text, (WIDTH // 2 - 90, HEIGHT // 2 + 80))
        pygame.display.flip()
        pygame.time.wait(1000)

        for i in range(2, 0, -1):
            screen.fill(BLACK)
            countdown_text = font20.render(str(i), True, WHITE)
            screen.blit(countdown_text, (WIDTH // 2 - 10, HEIGHT // 2 - 40))
            screen.blit(instructions_text, (WIDTH // 2 - 60, HEIGHT // 2 - 10))
            screen.blit(geek1_instructions_text, (WIDTH // 2 - 160, HEIGHT // 2 + 20))
            screen.blit(geek2_instructions_text, (WIDTH // 2 - 240, HEIGHT // 2 + 50))
            screen.blit(win_condition_text, (WIDTH // 2 - 90, HEIGHT // 2 + 80))
            pygame.display.flip()
            pygame.time.wait(1000)

        while running:
            screen.fill(BLACK)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        geek2YFac = -1
                    if event.key == pygame.K_DOWN:
                        geek2YFac = 1
                    if event.key == pygame.K_w:
                        geek1YFac = -1
                    if event.key == pygame.K_s:
                        geek1YFac = 1
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        geek2YFac = 0
                    if event.key == pygame.K_w or event.key == pygame.K_s:
                        geek1YFac = 0

            for geek in listOfGeeks:
                if pygame.Rect.colliderect(ball.getRect(), geek.getRect()):
                    ball.hit()

            geek1.update(geek1YFac)
            geek2.update(geek2YFac)
            point = ball.update()

            if point == -1:
                geek1Score += 1
            elif point == 1:
                geek2Score += 1

            if point: 
                ball.reset()

            geek1.display()
            geek2.display()
            ball.display()

            geek1.displayScore("Geek_1 : ", 
                    geek1Score, 100, 20, WHITE)
            geek2.displayScore("Geek_2 : ", 
                    geek2Score, WIDTH-100, 20, WHITE)

            if geek1Score >= 5:
                text = "player 1 wins!"
                pygame.time.wait(3000)
                running = False
                if text:
                  text = font20.render(text, True, WHITE)
                  screen.blit(text, (WIDTH // 2 - 100, HEIGHT // 2))
                  pygame.display.update()
                  pygame.time.wait(1000)
            elif geek2Score >= 5:
                text = "player 2 wins!"
                pygame.time.wait(3000)
                running = False
                if text:
                  text = font20.render(text, True, WHITE)
                  screen.blit(text, (WIDTH // 2 - 100, HEIGHT // 2))
                  pygame.display.update()
                  pygame.time.wait(1000)

            pygame.display.update()
            clock.tick(FPS)	 

    if __name__ == "__main__":
        main()
        pygame.quit()

def main():
    start_screen_color = GREEN
    running = True
    game_selected = False

    while running:
        if not game_selected:
            draw_start_screen(start_screen_color)
        else:
            if game_selected == "Tic-Tac-Toe":
                tictactoe_game()
            elif game_selected == "Pong":
                pong_game()
            game_selected = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and not game_selected:
                x, y = pygame.mouse.get_pos()
                if 100 <= x <= 300 and 200 <= y <= 250:
                    game_selected = "Tic-Tac-Toe"
                elif 400 <= x <= 600 and 200 <= y <= 250:
                    game_selected = "Pong"

        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()