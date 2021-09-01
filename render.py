import pygame
import solar_system
import time

pygame.init()

class Camera:
    def __init__(self, screen, x, y, w, h, zoom=1):
        self.screen = screen
        self.fobjects = dict()
        self.x, self.y = x, y
        self.size = self.w, self.h = w, h
        self.zoom = zoom

    def render_frame(self, rotate=True):
        self.screen.fill((0, 0, 0))
        for fobject in self.fobjects.values():
            cords = (round(self.x - fobject[0].x), round(self.y - fobject[0].y)) #from global cords to cords on screen
            pygame.draw.circle(self.screen, fobject[1], cords, fobject[0].r)
            fobject[0].rotate()
        
        pygame.display.flip()

def main():
    fps = 120
    clock = pygame.time.Clock()

    size = w, h = (1024, 650)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Solar System')

    fobjects = dict()

    fobjects['star1'] = (solar_system.Star(0, 0, 60, 200, None), [255, 237, 0])
    fobjects['p1'] = (solar_system.Planet(120, -120, 30, 20, fobjects['star1'][0]),  [0, 255, 150])
    fobjects['p2'] = (solar_system.Planet(380, 480, 40, 30, fobjects['star1'][0]), [200, 240, 30])
    fobjects['s2_1'] = (solar_system.Planet(440, 540, 10, 8, fobjects['p2'][0]), [200, 200, 200])

    main_camera = Camera(screen, 0, 0, w, h)

    main_camera.fobjects = fobjects


    #mouse control
    lmx, lmy = 0, 0

    game = True
    while game:
        clock.tick(fps)
        
        #events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
        

        #keyboard camera control
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_a]:
            main_camera.x += 2
        elif pressed_keys[pygame.K_d]:
            main_camera.x -= 2

        if pressed_keys[pygame.K_s]:
            main_camera.y -= 2
        elif pressed_keys[pygame.K_w]:
            main_camera.y += 2  
        

        
        #mouse camera control
        pressed_m = pygame.mouse.get_pressed()

        mx, my = pygame.mouse.get_pos()

        if pressed_m[0]:
            vec = (mx - lmx, my - lmy) #get mouse movement vector
            main_camera.x += vec[0]
            main_camera.y += vec[1]
            lmx, lmy = mx, my
        else:
            lmx, lmy = mx, my
        
        main_camera.render_frame()

        


if __name__ == '__main__':
    main()
