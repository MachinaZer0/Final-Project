import pygame

def main():
    pygame.init()
    pygame.display.set_caption("Digital Rain")
    width = 800
    height = 600
    screen = pygame.display.set_mode((width,height))
    bg_img = pygame.image.load("FFBE_Lanzelt_Ruins_BG.webp")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(bg_img, bg_img.get_rect())
    pygame.quit

if __name__ == "__main__":
    main()