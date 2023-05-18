from vpython import *

# Create the tetrahedron object
tetrahedron = tetrahedron(pos=vector(0, 0, 0), size=5, color=color.blue)

# Create the octahedron object
octahedron = octahedron(pos=vector(0, 0, 0), size=5, color=color.red)

# Set rotation parameters
rotate_objects = True
rotation_speed = 0.01

def toggle_rotation():
    global rotate_objects
    rotate_objects = not rotate_objects

# Create a button to toggle rotation
toggle_button = button(bind=toggle_rotation, text="Toggle Rotation")

# Create a scene to display the objects
scene = canvas(title="Rotating Shapes", width=800, height=600)

# Run the simulation
while True:
    rate(60)
    if rotate_objects:
        tetrahedron.rotate(axis=vector(0, 1, 0), angle=rotation_speed)
        octahedron.rotate(axis=vector(0, 1, 0), angle=rotation_speed)