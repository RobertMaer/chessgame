import pygame

pygame.init()

# Создаем окно
screen = pygame.display.set_mode((600, 600))

# Создаем объект поверхности для доски
board_surface = pygame.Surface((600, 600))

# Закрашиваем клетки доски чередуя белый и черный цвета
cell_size = 75
for row in range(8):
    for col in range(8):
        x = col * cell_size
        y = row * cell_size
        if (row + col) % 2 == 0:
            color = (187, 187, 187)
        else:
            color = (128,64 , 64)
        pygame.draw.rect(board_surface, color, (x, y, cell_size, cell_size))

# Размещаем поверхность с доской на экране
screen.blit(board_surface, (0, 0))

img_path = 'b_king.png'
king_image = pygame.image.load(img_path)

# Создаем объект поверхности для короля
king_surface = pygame.Surface((75, 75))

# Размещаем изображение короля на поверхности
king_surface.blit(king_image, (0,0))

# Размещаем поверхность с королем на доске
screen.blit(king_surface, (300, 300))

# Отображаем изменения на экране
pygame.display.update()

# Ждем закрытия окна
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()