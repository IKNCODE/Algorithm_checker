import pygame
import sys
import math 
import time
pygame.font.init()
font = pygame.font.SysFont('arial', 20)

class Display:   
    def __init__(self,width,height):
        self.x = width
        self.y = height
        pygame.init()
        global screen
        screen = pygame.display.set_mode((self.x,self.y)) #Creating a pygame window with shown x and y
    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
        


class Button:
    def __init__(self,text,pos,font,bg='white',feedback=''):
        self.x, self.y = pos
        self.font = pygame.font.SysFont("arial", font)
        if feedback == '':
            self.feedback = 'text'
        else:
            self.feedback = feedback
        self.change_text(text,bg)

    def change_text(self,text,bg='green'):
        self.text = self.font.render(text,1,pygame.Color('White'))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0,0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def show_btn(self):
        screen.blit(self.surface, (self.x, self.y))
        



if __name__ == '__main__':
    d = Display(500, 600)
    d.start()
    btn1 = Button("Hello world", (100,100),font=30,bg='white')
    btn1.show_btn()
    pygame.display.update()
