import pygame

pygame.init()

# Создаем окно
screen = pygame.display.set_mode((400, 400))

# Загружаем изображение короля
img_path = 'D:\Роберт\Роберт 2\python-chess\data\imgs'
king_image = pygame.image.load(img_path)

# Создаем объект поверхности для короля
king_surface = pygame.Surface((50, 50))

# Размещаем изображение короля на поверхности
king_surface.blit(king_image, (0, 0))

# Размещаем поверхность с королем на доске
screen.blit(king_surface, (100, 100))

# Отображаем изменения на экране
pygame.display.update()

# Ждем закрытия окна
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
