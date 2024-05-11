import pygame

def init():
    pygame.init()

    window = pygame.display.set_mode((400, 400))

def getkey(keyName):
    ans=False
    for event in pygame.event.get():
        pass
    KeyInput = pygame.key.get_pressed()
    myKey=getattr(pygame,'K_{}'.format(keyName))
    if KeyInput[myKey]:
        ans=True
    pygame.display.update()
    return  ans

def main():
    if getkey('LEFT'):
        print("Left Key")

    if getkey('RIGHT'):
        print("Right key")

if __name__=='__main__':
    init()

    while True:
        main()
