import pygame

pygame.init()

font = pygame.font.Font(None, 36)


#1 кнопка
button_pos1 = (50, 50)
button_size = (150, 50)
button_rect_1 = pygame.Rect(button_pos1, button_size)
button_task_1 = pygame.Surface(button_size)
button_task_1.fill((255, 255, 255))
text_surf = font.render("task 1", True, (0,0, 0))
text_rect = text_surf.get_rect(center=button_task_1.get_rect().center)
button_task_1.blit(text_surf, text_rect)


#2 кнопка
button_pos2 = (220, 50)
button_rect_2 = pygame.Rect(button_pos2, button_size)
button_task_2 = pygame.Surface(button_size)
button_task_2.fill((255, 255, 255))
text_surf = font.render("task 2", True, (0,0, 0))
text_rect = text_surf.get_rect(center=button_task_2.get_rect().center)
button_task_2.blit(text_surf, text_rect)


#3 кнопка
button_pos3 = (390, 50)
button_rect_3 = pygame.Rect(button_pos3, button_size)
button_task_3 = pygame.Surface(button_size)
button_task_3.fill((255, 255, 255))
text_surf = font.render("task 3", True, (0,0, 0))
text_rect = text_surf.get_rect(center=button_task_3.get_rect().center)
button_task_3.blit(text_surf, text_rect)

#4 кнопка
button_pos4 = (100, 150)
button_rect_4 = pygame.Rect(button_pos4, button_size)
button_player_vs_player = pygame.Surface(button_size)
button_player_vs_player.fill((255, 255, 255))
text_surf = font.render("2 players", True, (0,0, 0))
text_rect = text_surf.get_rect(center=button_player_vs_player.get_rect().center)
button_player_vs_player.blit(text_surf, text_rect)


#5 кнопка
button_pos5 = (310, 150)
button_rect_5 = pygame.Rect(button_pos5, button_size)
button_quit = pygame.Surface(button_size)
button_quit.fill((255, 255, 255))
text_surf = font.render("quit", True, (0,0, 0))
text_rect = text_surf.get_rect(center=button_quit.get_rect().center)
button_quit.blit(text_surf, text_rect)


'''#кнопка выход в меню
button_pos6 = (600, 540)
button_size6=(60,60)
button_rect_6 = pygame.Rect(button_pos6, button_size6)
button_quit_to_menu = pygame.Surface(button_size6)
button_quit_to_menu.fill((255, 255, 255))
text_surf = font.render("back", True, (0,0, 0))
text_rect = text_surf.get_rect(center=button_quit_to_menu.get_rect().center)
button_quit_to_menu.blit(text_surf, text_rect) '''



# создание первого окна
screen1 = pygame.display.set_mode((600, 600))

#добавление кнопок на текущий экран
screen1.blit(button_task_1, button_pos1)
screen1.blit(button_task_2, button_pos2)
screen1.blit(button_task_3, button_pos3)
screen1.blit(button_player_vs_player, button_pos4)
screen1.blit(button_quit, button_pos5)
pygame.display.set_caption("Start window")



current_screen = screen1 # начальное окно

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


        elif event.type == pygame.MOUSEBUTTONDOWN:
            # проверка, была ли нажата кнопка
            if button_rect_4.collidepoint(event.pos):
                if screen1:
                    screen1=False

                    WINDOW_SIZE = (600, 600)

                    screen = pygame.display.set_mode(WINDOW_SIZE)
                    #screen.blit(button_quit_to_menu, button_pos6)

                    pygame.display.set_caption("Play window")

                    from data.classes.Board import Board
                    board = Board(600, 600)

                    def draw(display):
                    	#display.fill('black')
                    	board.draw(display)
                    	pygame.display.update()

                    if __name__ == '__main__':
                        running = True

                        while running:
                            mx, my = pygame.mouse.get_pos()
                            for event in pygame.event.get():
                    			# Quit the game if the user presses the close button
                                if event.type == pygame.QUIT:
                                    running = False
                                elif event.type == pygame.MOUSEBUTTONDOWN:
                           			# If the mouse is clicked
                                    if event.button == 1:
                                        board.handle_click(mx, my)
                                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                                    running=False
                            if board.is_in_checkmate('black'): # If black is in checkmate
                                print('White wins!')
                                running = False
                            elif board.is_in_checkmate('white'): # If white is in checkmate
                                print('Black wins!')

                                running = False


                    		# Draw the board
                            draw(screen)
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        screen=False
                        screen1 = pygame.display.set_mode((600, 600))
                        screen1.blit(button_task_1, button_pos1)
                        screen1.blit(button_task_2, button_pos2)
                        screen1.blit(button_task_3, button_pos3)
                        screen1.blit(button_player_vs_player, button_pos4)
                        screen1.blit(button_quit, button_pos5)
                        pygame.display.set_caption("Start window")
                        pygame.display.update()
                        #Если нажали кнопку обратно в меню, то
                        #screen=False
                        #screen1=True
            elif button_rect_1.collidepoint(event.pos):
                if screen1:
                    screen1=False
                    # создание второго окна
                    #screen2 = pygame.display.set_mode((600, 600))
                    #pygame.display.set_caption("Play window")
                    from data.classes.Board1 import Board

                    WINDOW_SIZE = (600, 600)
                    screen = pygame.display.set_mode(WINDOW_SIZE)
                    pygame.display.set_caption("Play window")
                    board = Board(WINDOW_SIZE[0], WINDOW_SIZE[1])

                    def draw(display):
                    	display.fill('white')
                    	board.draw(display)
                    	pygame.display.update()

                    if __name__ == '__main__':
                        running = True
                        while running:
                            mx, my = pygame.mouse.get_pos()
                            for event in pygame.event.get():
                    			# Quit the game if the user presses the close button
                                if event.type == pygame.QUIT:
                                    running = False
                                elif event.type == pygame.MOUSEBUTTONDOWN:
                           			# If the mouse is clicked
                                    if event.button == 1:
                                        board.handle_click(mx, my)
                                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                                    running=False

                            if board.is_in_checkmate('black'): # If black is in checkmate
                                print('White wins!')
                                running = False
                            elif board.is_in_checkmate('white'): # If white is in checkmate
                                print('Black wins!')
                                running = False



                    		# Draw the board
                            draw(screen)
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        screen=False
                        screen1 = pygame.display.set_mode((600, 600))
                        screen1.blit(button_task_1, button_pos1)
                        screen1.blit(button_task_2, button_pos2)
                        screen1.blit(button_task_3, button_pos3)
                        screen1.blit(button_player_vs_player, button_pos4)
                        screen1.blit(button_quit, button_pos5)
                        pygame.display.set_caption("Start window")
                        pygame.display.update()
                        #Если нажали кнопку обратно в меню, то
                        #screen=False
                        #screen1=True
            elif button_rect_2.collidepoint(event.pos):
                if screen1:
                    screen1=False
                    # создание второго окна
                    #screen2 = pygame.display.set_mode((600, 600))
                    #pygame.display.set_caption("Play window")
                    from data.classes.Board2 import Board

                    WINDOW_SIZE = (600, 600)
                    screen = pygame.display.set_mode(WINDOW_SIZE)
                    pygame.display.set_caption("Play window")
                    board = Board(WINDOW_SIZE[0], WINDOW_SIZE[1])

                    def draw(display):
                    	display.fill('white')
                    	board.draw(display)
                    	pygame.display.update()

                    if __name__ == '__main__':
                        running = True
                        while running:
                            mx, my = pygame.mouse.get_pos()
                            for event in pygame.event.get():
                    			# Quit the game if the user presses the close button
                                if event.type == pygame.QUIT:
                                    running = False
                                elif event.type == pygame.MOUSEBUTTONDOWN:
                           			# If the mouse is clicked
                                    if event.button == 1:
                                        board.handle_click(mx, my)
                                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                                    running=False

                            if board.is_in_checkmate('black'): # If black is in checkmate
                                running = False
                            elif board.is_in_checkmate('white'): # If white is in checkmate
                                running = False

                    		# Draw the board
                            draw(screen)
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        screen=False
                        screen1 = pygame.display.set_mode((600, 600))
                        screen1.blit(button_task_1, button_pos1)
                        screen1.blit(button_task_2, button_pos2)
                        screen1.blit(button_task_3, button_pos3)
                        screen1.blit(button_player_vs_player, button_pos4)
                        screen1.blit(button_quit, button_pos5)
                        pygame.display.set_caption("Start window")
                        pygame.display.update()
                        #Если нажали кнопку обратно в меню, то
                        #screen=False
                        #screen1=True

            elif button_rect_3.collidepoint(event.pos):
                if screen1:
                    screen1=False
                    # создание второго окна
                    #screen2 = pygame.display.set_mode((600, 600))
                    #pygame.display.set_caption("Play window")
                    from data.classes.Board3 import Board

                    WINDOW_SIZE = (600, 600)
                    screen = pygame.display.set_mode(WINDOW_SIZE)
                    pygame.display.set_caption("Play window")
                    board = Board(WINDOW_SIZE[0], WINDOW_SIZE[1])

                    def draw(display):
                    	display.fill('white')
                    	board.draw(display)
                    	pygame.display.update()

                    if __name__ == '__main__':
                        running = True
                        while running:
                            mx, my = pygame.mouse.get_pos()
                            for event in pygame.event.get():
                    			# Quit the game if the user presses the close button
                                if event.type == pygame.QUIT:
                                    running = False
                                elif event.type == pygame.MOUSEBUTTONDOWN:
                           			# If the mouse is clicked
                                    if event.button == 1:
                                        board.handle_click(mx, my)
                                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                                    running=False

                            if board.is_in_checkmate('black'): # If black is in checkmate
                                running = False
                            elif board.is_in_checkmate('white'): # If white is in checkmate
                                running = False

                    		# Draw the board
                            draw(screen)
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        screen=False
                        screen1 = pygame.display.set_mode((600, 600))
                        screen1.blit(button_task_1, button_pos1)
                        screen1.blit(button_task_2, button_pos2)
                        screen1.blit(button_task_3, button_pos3)
                        screen1.blit(button_player_vs_player, button_pos4)
                        screen1.blit(button_quit, button_pos5)
                        pygame.display.set_caption("Start window")
                        pygame.display.update()
                        #Если нажали кнопку обратно в меню, то
                        #screen=False
                        #screen1=True
            elif button_rect_5.collidepoint(event.pos):
                if screen1:
                    pygame.quit()
                    quit()

    # отрисовка текущего окна
    #current_screen_1.fill((0, 0, 0))
    pygame.display.update()