import sys, pygame, random

pygame.init()

size = WIDTH, HEIGHT = 1028, 720
white = 255, 255, 255

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Particle Sim")


class Particle:
    def __init__(self, x: float, y: float, radius: float = 4, color: tuple[float, ...] = (255, 0, 0)):
        self.x = x
        self.y = y
        self.x_vel = 0
        self.y_vel = 0
        self.radius = radius
        self.color = color

    def set_x_vel(self, vel: float) -> None:
        self.x_vel = vel

    def set_y_vel(self, vel: float) -> None:
        self.y_vel = vel

    def set_x(self, x) -> None:
        self.x = x

    def set_y(self, y) -> None:
        self.y = y

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def update(self):
        if self.x <= 4 or self.x >= WIDTH - 4:
            self.x_vel *= -0.9
        if self.y <= 4 or self.y >= HEIGHT - 4:
            self.y_vel *= -0.9
        self.x = self.x + self.x_vel
        self.y = self.y + self.y_vel

class ParticleSystem:
    def __init__(self, particle_count: int):
        self.particles: List[Particle] = []
        self.particle_count = particle_count
        self.seed_particles()

    def seed_particles(self):
        # Place Particles in random positions inside the window.
        for _ in range(self.particle_count):
            new_particle = Particle(x=WIDTH * random.random(), y=HEIGHT * random.random(), color=(255*random.random(), 255*random.random(), 255*random.random()))
            new_particle.set_x_vel(random.uniform(-0.6, 0.6))
            new_particle.set_y_vel(random.uniform(-0.6, 0.6))
            self.particles.append(new_particle)

    def update_particles(self):

        for particle in self.particles:
            particle.set_y_vel(particle.y_vel + 0.001)
            particle.update()



    def draw_all(self):
        self.update_particles()
        for particle in self.particles:
            particle.draw()


particle_system = ParticleSystem(1)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(white)
    keys = pygame.key.get_pressed()

    if keys[pygame.K_r]:
        particle_system.particles.clear()
        particle_system.seed_particles()

    pygame.draw.line(screen,(0,0,0),(0,HEIGHT - 4),(WIDTH, HEIGHT-4))
    particle_system.draw_all()
    pygame.display.flip()