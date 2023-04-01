import pygame
import module2

pygame.init()


# Загружаем изображение короля
img_path = 'b_king.png'
king_image = pygame.image.load(img_path)

# Создаем объект поверхности для короля
king_surface = pygame.Surface((50, 50))

# Размещаем изображение короля на поверхности
king_surface.blit(king_image, (150, 150))

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
