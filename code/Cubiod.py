from vpython import *

# Create the cuboid object
cuboid = box(pos=vector(0, 0, 0), size=vector(5, 3, 2), color=color.red)

# Set cuboid rotation parameters
rotate_cuboid = True
rotation_speed = 0.01

def toggle_rotation():
    global rotate_cuboid
    rotate_cuboid = not rotate_cuboid

# Create a button to toggle cuboid rotation
toggle_button = button(bind=toggle_rotation, text="Toggle Rotation")

# Create a scene to display the cuboid
scene = canvas(title="Rotating Cuboid", width=800, height=600)

# Run the simulation
while True:
    rate(60)
    if rotate_cuboid:
        cuboid.rotate(axis=vector(0, 1, 0), angle=rotation_speed)