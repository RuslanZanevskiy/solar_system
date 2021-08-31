import pygame
import solar_system
import time

pygame.init()

class Camera:
    def __init__(self, screen, x, y, w, h, zoom=1):
        self.screen = screen
        self.planets = dict()
        self.stars = dict()
        self.x, self.y = x, y
        self.size = self.w, self.h = w, h
        self.zoom = zoom

    def render_frame(self, rotate=True):
        self.screen.fill((0, 0, 0))
        for star in self.stars.values():
            cords = (round(self.x - star[0].x), round(self.y - star[0].y)) #from global cords to cords on screen
            pygame.draw.circle(self.screen, star[1], cords, star[0].r)
            star[0].rotate()

        for planet in self.planets.values():
            cords = (round(self.x - planet[0].x), round(self.y - planet[0].y)) #from global cords to cords on screen
            pygame.draw.circle(self.screen, planet[1], cords, planet[0].r)
            planet[0].rotate()
        
        pygame.display.flip()

def main():
    fps = 180
    clock = pygame.time.Clock()

    size = w, h = (800, 600)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Solar System')

    stars = dict()
    planets = dict()
    points = dict()

    stars['main'] = (solar_system.Star(0, 0, 60, 200), [255, 237, 0])
    planets['main1'] = (solar_system.Planet(80, -80, 20, 20, stars['main'][0], 0.5),  [0, 255, 150])
    planets['main2'] = (solar_system.Planet(-150, 150, 28, 30, stars['main'][0], 0.2), [200, 240, 30])

    main_camera = Camera(screen, 0, 0, w, h)

    main_camera.stars = stars
    main_camera.planets = planets


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
