import math

class Fobject:
    def __init__(self, x, y, r, mass, orbit_target):
        self.x, self.y = x, y
        self.r = r
        self.mass = mass
        self.orbit_target = orbit_target
        self.angle_speed = 0
        if self.orbit_target:
            self.dist_from_target = ((self.x-self.orbit_target.x)**2+(self.y-self.orbit_target.y)**2)**0.5
            self.angle_speed = 4/self.dist_from_target*self.mass
            self.orbit_target.children.append(self)
        self.children = []
        self.cur_angle = 0
        
    def rotate(self):
        cx, cy = self.x, self.y
        if self.orbit_target:
            loc_x, loc_y = self.x - self.orbit_target.x, self.y - self.orbit_target.y
            s, c = math.sin(math.radians(self.angle_speed)), math.cos(math.radians(self.angle_speed))
            self.x = (loc_x * c - loc_y * s) + self.orbit_target.x
            self.y = (loc_x * s + loc_y * c) + self.orbit_target.y
            self.cur_angle = (self.cur_angle + self.angle_speed) % 361
        for child in self.children:
            child.x += (self.x - cx)
            child.y += (self.y - cy)

        
class Planet(Fobject):
    def __init__(self, x, y, r, mass, orbit_target):
        super().__init__(x, y, r, mass, orbit_target)

class Star(Fobject):
    def __init__(self, x, y, r, mass, orbit_target):
        super().__init__(x, y, r, mass, orbit_target)
        
    
