import pygame
 
pygame.init()
screen = pygame.display.set_mode((1080, 720))
done = False
is_blue = True
x = 30
y = 30
 
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue
                        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 1
        if pressed[pygame.K_DOWN]: y += 1
        if pressed[pygame.K_LEFT]: x -= 1
        if pressed[pygame.K_RIGHT]: x += 1
        
         
        if is_blue: color = (0, 128, 255)
        else: color = (255, 100, 0)
#         pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))
        pygame.draw.circle(screen, (255, 255, 255), (x+2, y+3), 30)
        pygame.draw.circle(screen, color, (x, y), 30)      
        pygame.draw.circle(screen, (0, 0, 0), (x-10, y-5), 5)
        pygame.draw.circle(screen, (0, 0, 0), (x+10, y-5), 5)
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(x-10, y+12, 20, 10))
         
        pygame.display.flip()