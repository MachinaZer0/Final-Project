import pygame
from PIL import Image

turn = 1

"""class Rain():
    def __init__(self, image, pos=(0,0)):
            self.pos = pos
            self.image = image
            keys=pygame.key.get_pressed()
            self.live = True
            if keys[1]:
                 ATK()

    def ATK(self):
         ATK = 200

         

    def is_alive(self):
        return self.HP> 0 

    def Win():
         

    def Lose():

def Rain(self, image):
         HP = 1000
         ATK = 200
         DEF = 50"""
         
class Character:
    def __init__(self, name, hp, atk, defense):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.is_alive()
        keys = pygame.key.get_pressed()
        if keys[1]:
            self.attack()
        elif keys[2]:
            self.defend()

    def attack(self, target):
        # Calculate damage considering target's defense
        damage = self.atk - target.defense
        damage = max(damage, 0)  # Ensure no negative damage
        target.hp -= damage
        return damage

    def defend(self):
        self.defense += 50

    def is_alive(self):
        if self.hp <= 0:
            pygame.QUIT

    def reset_defense(self):
        self.defense = 50 

class Enemy:
    def __init__(self, name, hp, atk, defense):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense

    def attack(self, target):
        # Calculate damage considering target's defense
        damage = self.atk - target.defense
        damage = max(damage, 0)  # Ensure no negative damage
        target.hp -= damage
        return damage

    def defend(self):
        # Increase defense temporarily
        self.defense += 5
        return 5

    def is_alive(self):
        return self.hp > 0

    def reset_defense(self):
        self.defense = 10  # Reset defense after a turn
         
def ImageResize(filename):
    with Image.open(filename) as img:
        out_img = img.resize((525, 550))
        out_img.save("FFBE_bg.webp")

def main():
    pygame.init()
    pygame.display.set_caption("Game")
    width = 525
    height = 900
    screen = pygame.display.set_mode((width,height))
    black = (0, 0, 0)
    bg_img = "FFBE_Lanzelt_Ruins_BG.webp"
    img_Rain = "Rain_idle.png"
    img_Boss = "Boss_idle.png"
    ImageResize(bg_img)
    bg_img_resize = "FFBE_bg.webp"
    bg_obj = pygame.image.load(bg_img_resize).convert()
    Rain_obj = pygame.image.load(img_Rain).convert()
    Boss_obj = pygame.image.load(img_Boss).convert()
    Character("Rain", 1000, 200, 50)
    Enemy("Aranea", 1000, 200, 50)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(black)
        screen.blit(bg_obj, (0,0))
        screen.blit(Rain_obj, (375,300))
        screen.blit(Boss_obj, (30,200))
        pygame.display.update()
    pygame.quit

if __name__ == "__main__":
    main()