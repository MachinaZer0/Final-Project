import pygame
from PIL import Image

#global variables
turn = 1
screen = pygame.display.set_mode((525,700))
click_time = 0

#display turn counter in top right
def TurnCounter():
     global screen
     global turn

     turn_str = "{}".format(turn)
     pygame.font.init()
     turn_font = pygame.font.SysFont('Ariel', 50)
     text_surface = turn_font.render(f"Turn "+turn_str, False, (255, 255, 255))
     pygame.draw.rect(screen, 'black', pygame.Rect(390, 5, 140, 45))
     screen.blit(text_surface, (400, 10))

#display attack prompt
def UI():
     global screen

     pygame.font.init()
     UI_font = pygame.font.SysFont('Ariel', 60)
     attack_surface = UI_font.render("Attack[1]", False, (255, 255, 255))
     block_surface = UI_font.render("Block[2]", False, (255, 255, 255))
     heal_surface = UI_font.render("Heal[3]", False, (255, 255, 255))
     screen.blit(attack_surface, (60, 600))
     screen.blit(block_surface, (280, 600))
     screen.blit(heal_surface, (190, 650))

#resize background image
def ImageResize(filename):
    with Image.open(filename) as img:
        out_img = img.resize((525, 550))
        out_img.save("FFBE_bg.webp")

def ImageResize2(filename):
    with Image.open(filename) as img:
        out_img = img.resize((525, 700))
        out_img.save("win_edit.png")

def ImageResize3(filename):
    with Image.open(filename) as img:
        out_img = img.resize((525, 700))
        out_img.save("lose_edit.png")

#creates all unit values
class Character:
    def __init__(self, name, hp, atk, defense, x, y, img_idle, img_atk=None, img_dead=None):
        self.name = name
        self.atk = atk
        self.basedef = defense
        self.defense = defense
        self.hp = hp
        self.maxhp = hp
        self.x = x
        self.y = y
        self.img_idle = img_idle
        self.img_atk = img_atk
        self.img_dead = img_dead
        self.alive = True
        self.is_attacking = False

    #when a unit attacks
    def attack(self, target):
            global turn
            """self.is_attacking = True"""
            if self.alive == False:
                pass
            elif self.alive == True:
                target.defend(self.atk)
                turn+=1

    def block(self, target):
        global turn
        self.defense += 100
        target.defend(0)
        turn+=1

    def heal(self, target):
        global turn
        self.hp += (0.2*self.maxhp)
        target.defend(0)
        turn+=1

    #when a unit takes damage
    def defend(self, atk):
            damage = max(atk - self.defense, 0)
            self.hp -= damage
            self.defense = self.basedef
            if self.hp <= 0:
                self.hp = 0
                print(f"{self.name} died")
                self.alive = False
                """Character.BossDeath(self.name, self.x, self.y)"""
            return damage

    #display name and stat values
    def characterUI(self, name, x, y):
        global screen
        pygame.font.init()

        #Name Display
        name_str = "{}".format(name)
        UI_font = pygame.font.SysFont('Ariel', 30)
        name_surface = UI_font.render(f""+name_str, False, (255, 255, 255))
        screen.blit(name_surface, (x, y))

        #Stat Display
        HP_str = "{}".format(self.hp)
        maxHP_str = "{}".format(self.maxhp)
        hp_font = pygame.font.SysFont('Ariel', 15)
        hp_surface = hp_font.render(f""+HP_str+"/"+maxHP_str, False, (255, 255, 255))
        screen.blit(hp_surface, (x, y+20))

        #attack image
        if self.is_attacking == True:
            self_atk = pygame.image.load(self.img_atk).convert()
            screen.blit(self_atk, (self.x, self.y))
            self.is_attacking = False      
        elif self.is_attacking == False:
            self_obj = pygame.image.load(self.img_idle).convert()
            screen.blit(self_obj, (self.x, self.y))

    def BossDeath(self, x, y):
        with Image.open(self.img_idle) as img:
            temp_img = Image.new(mode="RGBA", size=(img.width, img.height), color=(255, 255, 255, 50))
            img_blend = Image.blend(img, temp_img, 0.5)
            img_blend.save("test.png")
        test_img = "test.png"
        self_obj = pygame.image.load(test_img).convert()
        screen.blit(self_obj, (x, y))
         
def winscreen():
    global screen
    win = "win.png"
    ImageResize2(win)
    win2 = "win_edit.png"
    win_obj = pygame.image.load(win2).convert()
    screen.blit(win_obj, (0,0))

def losescreen():
    global screen
    lose = "lose.png"
    ImageResize3(lose)
    lose2 = "lose_edit.png"
    lose_obj = pygame.image.load(lose2).convert()
    screen.blit(lose_obj, (0,0))

def main():
    global turn
    pygame.init()
    pygame.display.set_caption("FFBE")
    bg_img = "FFBE_Lanzelt_Ruins_BG.webp"
    ImageResize(bg_img)
    bg_img_resize = "FFBE_bg.webp"
    bg_obj = pygame.image.load(bg_img_resize).convert()
    Rain = Character("Rain", 1000, 200, 50, 375, 300, "Rain_idle.png", "Rain_atk.png", "Rain_dead.png")
    Aranea = Character("Aranea", 1000, 200, 50, 30, 200, "Boss_idle.png")
    Bossheal = True
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                        running = False
            if turn%2 == 1:
                if event.type == pygame.KEYDOWN: 
                    print("Keydown")
                    if event.key == pygame.K_1: 
                        Character.attack(Rain, Aranea)
                    elif event.key == pygame.K_2: 
                        Character.block(Rain, Aranea)
                    elif event.key == pygame.K_3: 
                        Character.heal(Rain, Aranea)
            elif turn % 2 != 1:
                if Aranea.alive == False:
                    winscreen()
                elif (Aranea.hp <= 300) and (Bossheal == True):
                    Aranea.hp = Aranea.maxhp
                    Bossheal = False
                elif (Aranea.hp <= 300) and (Aranea.hp > 49):
                    Character.block(Aranea, Rain)
                elif Aranea.hp > (300):
                    Character.attack(Aranea, Rain)
            elif event.type == pygame.QUIT:
                running = False
        screen.fill('black')
        screen.blit(bg_obj, (0,0))
        TurnCounter()
        UI()
        Character.characterUI(Rain, "Rain", 300, 560)
        Character.characterUI(Aranea, "Aranea", 0, 560)
        if Aranea.alive == False:
            winscreen()
        if Rain.alive == False:
            losescreen()
        pygame.display.update()
    pygame.quit

if __name__ == "__main__":
    main()