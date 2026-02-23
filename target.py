# Defines 'objects' that can be tracked by the radar, such as planes, missiles, etc.

class Target:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity
        
    def update(self, dt):
        self.position += self.velocity * dt

    