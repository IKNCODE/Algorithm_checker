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
    def update(self):
        pygame.display.update()
    def get_screen(self):
        return screen


class Button:
    def __init__(self,text,pos,font,bg='green',feedback=''):
        self.x, self.y = pos
        self.font = pygame.font.SysFont("arial", font)
        if feedback == '':
            self.feedback = 'text'
        else:
            self.feedback = feedback
        self.change_text(text,bg)

    def change_text(self,text,bg='green'):
        self.text = self.font.render(text,1,pygame.Color('Black'))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0,0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def show_btn(self):
        screen.blit(self.surface, (self.x, self.y))

        



if __name__ == '__main__':
    d = Display(500, 600)
    btn1 = Button("Hello world", (100,100),font=30,bg='Green')
    d.update()
    btn1.show_btn()
    d.update()