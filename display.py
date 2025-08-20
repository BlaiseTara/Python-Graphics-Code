import gpu
import random

width = 640
height = 480

graphics = gpu.GPU(width, height)


# Define a "object" using these 4 vars

pos = [150,150]

scale = 20

verts = [
    [0,0],
    [0,1],
    [1,1],
]

edges = [
    [0,1],
    [1,2],
    [2,0],
]



graphics.init()

# Main Loop
while graphics.running:

    # Draw some random triangles on the screen to test performance
    # Randomize it each frame
    graphics.objects = []
    for i in range(150):
        randPos = [random.randint(0, width), random.randint(0, height)]
        scale = random.randint(10, 50)
        graphics.objects.append([randPos, scale, verts, edges])

    graphics.render()


graphics.stop()