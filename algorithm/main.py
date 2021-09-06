from display import disp
import pygame
import sys
lines = [23,65,43,11,23,76,4,55,54,77,33,26,98,54]
def main():
    j=1
    d = disp.Display(800, 600)
    btn1 = disp.Button('Start', (50,500), 60 , bg='red')
    btn1.show_btn()
    btn2 = disp.Button('Select', (250,500), 60)
    btn2.show_btn()
    for i in lines:
        pygame.draw.rect(d.get_screen(), 'white', ((j * 25)+ 300, 180, 15, i))
        j +=1
    d.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

main()