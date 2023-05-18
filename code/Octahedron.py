from vpython import *

# Create the pyramid objects
pyramid1 = pyramid(pos=vector(0, 0, 0), size=vector(5, 5, 5), color=color.red)
pyramid2 = pyramid(pos=vector(0, 0, 0), size=vector(5, 5, 5), color=color.red)
pyramid3 = pyramid(pos=vector(0, 0, 0), size=vector(5, 5, 5), color=color.red)
pyramid4 = pyramid(pos=vector(0, 0, 0), size=vector(5, 5, 5), color=color.red)

# Set rotation parameters
rotate_objects = True
rotation_speed = 0.01

def toggle_rotation():
    global rotate_objects
    rotate_objects = not rotate_objects

# Create a button to toggle rotation
toggle_button = button(bind=toggle_rotation, text="Toggle Rotation")

# Create a scene to display the objects
scene = canvas(title="Rotating Octahedron", width=800, height=600)

# Arrange the pyramid objects to form an octahedron
pyramid1.rotate(angle=0.785, axis=vector(0, 1, 0))
pyramid2.rotate(angle=2.356, axis=vector(0, 1, 0))
pyramid3.rotate(angle=3.927, axis=vector(0, 1, 0))
pyramid4.rotate(angle=5.498, axis=vector(0, 1, 0))

# Run the simulation
while True:
    rate(60)
    if rotate_objects:
        pyramid1.rotate(angle=rotation_speed, axis=vector(0, 1, 0))
        pyramid2.rotate(angle=rotation_speed, axis=vector(0, 1, 0))
        pyramid3.rotate(angle=rotation_speed, axis=vector(0, 1, 0))
        pyramid4.rotate(angle=rotation_speed, axis=vector(0, 1, 0))