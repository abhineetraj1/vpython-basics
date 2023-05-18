from vpython import *

# Create the cone object
cone = cone(pos=vector(0, 0, 0), axis=vector(0, 5, 0), radius=3, color=color.blue)

# Set cone rotation parameters
rotate_cone = True
rotation_speed = 0.01

def toggle_rotation():
    global rotate_cone
    rotate_cone = not rotate_cone

# Create a button to toggle cone rotation
toggle_button = button(bind=toggle_rotation, text="Toggle Rotation")

# Create a scene to display the cone
scene = canvas(title="Rotating Cone", width=800, height=600)

# Run the simulation
while True:
    rate(60)
    if rotate_cone:
        cone.rotate(axis=vector(0, 1, 0), angle=rotation_speed)