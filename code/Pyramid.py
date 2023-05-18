from vpython import *

# Create the pyramid object
pyramid = pyramid(pos=vector(0, 0, 0), size=vector(5, 3, 5), color=color.blue)

# Set pyramid rotation parameters
rotate_pyramid = True
rotation_speed = 0.01

def toggle_rotation():
    global rotate_pyramid
    rotate_pyramid = not rotate_pyramid

# Create a button to toggle pyramid rotation
toggle_button = button(bind=toggle_rotation, text="Toggle Rotation")

# Create a scene to display the pyramid
scene = canvas(title="Rotating Pyramid", width=800, height=600)

# Run the simulation
while True:
    rate(60)
    if rotate_pyramid:
        pyramid.rotate(axis=vector(0, 1, 0), angle=rotation_speed)