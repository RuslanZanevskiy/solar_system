import math

class Fobject:
    def __init__(self, x, y, r, mass, orbit_target, angle_speed):
        self.x, self.y = x, y
        self.r = r
        self.mass = mass
        self.orbit_target = orbit_target
        self.angle_speed = angle_speed
        self.cur_angle = 0
        
    def rotate(self):
        if self.orbit_target:
            loc_x, loc_y = self.x - self.orbit_target.x, self.y - self.orbit_target.y
            s, c = math.sin(math.radians(self.angle_speed)), math.cos(math.radians(self.angle_speed))
            self.x = (loc_x * c - loc_y * s) + self.orbit_target.x
            self.y = (loc_x * s + loc_y * c) + self.orbit_target.y
            self.cur_angle = (self.cur_angle + self.angle_speed) % 361
        
class Planet(Fobject):
    def __init__(self, x, y, r, mass, orbit_target, angle_speed=0.5):
        super().__init__(x, y, r, mass, orbit_target, angle_speed)

class Star(Fobject):
    def __init__(self, x, y, r, mass, orbit_target=None, angle_speed=0):
        super().__init__(x, y, r, mass, orbit_target, angle_speed)
        
    