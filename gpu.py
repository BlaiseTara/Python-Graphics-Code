import pygame
import random

pygame.init()

class GPU:
    def __init__(self, width, height):
        self.dimensions = [width, height]
        self.screen = pygame.display.set_mode(self.dimensions)
        self.clock = pygame.time.Clock()
        self.running = True

        self.objects = []

    # Probably will be needed eventually for something
    def init(self):
        pass

    def render(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        # Fill the screen with black
        self.screen.fill((0, 0, 0))

        # Draw all the "objects" on the screen
        for object in self.objects:
            pos = object[0]
            scale = object[1]
            vertices = object[2]
            edges = object[3]

            # Draw vertices
            for vertice in vertices:
                pixel_pos = (vertice[0] * scale + pos[0], vertice[1] * scale + pos[1])
                self.screen.set_at(pixel_pos, (255, 255, 255))


            # Set the color for the edges
            lineColor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

            # Draw edges
            for edge in edges:
                # Bresenham's line algorithm implementation
                # https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm

                pos_0 = (int(vertices[edge[0]][0] * scale + pos[0]), int(vertices[edge[0]][1] * scale + pos[1]))
                pos_1 = (int(vertices[edge[1]][0] * scale + pos[0]), int(vertices[edge[1]][1] * scale + pos[1]))

                x0, y0 = pos_0
                x1, y1 = pos_1

                dx = abs(x1 - x0)
                dy = abs(y1 - y0)
                sx = 1 if x0 < x1 else -1
                sy = 1 if y0 < y1 else -1
                err = dx - dy

                # ngl i forgot how this code even works...
                while True:
                    self.screen.set_at((x0, y0), lineColor)
                    if x0 == x1 and y0 == y1:
                        break
                    e2 = 2 * err
                    if e2 > -dy:
                        err -= dy
                        x0 += sx
                    if e2 < dx:
                        err += dx
                        y0 += sy


        pygame.display.flip()
        self.clock.tick()
        print(self.clock.get_fps())

    def stop(self):
        pygame.quit()