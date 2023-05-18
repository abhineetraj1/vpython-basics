from vpython import *

# Create the cylinder object
cylinder = cylinder(pos=vector(0, 0, 0), axis=vector(0, 5, 0), radius=2, color=color.blue)

# Set cylinder rotation parameters
rotate_cylinder = True
rotation_speed = 0.01

def toggle_rotation():
    global rotate_cylinder
    rotate_cylinder = not rotate_cylinder

# Create a button to toggle cylinder rotation
toggle_button = button(bind=toggle_rotation, text="Toggle Rotation")

# Create a scene to display the cylinder
scene = canvas(title="Rotating Cylinder", width=800, height=600)

# Run the simulation
while True:
    rate(60)
    if rotate_cylinder:
        cylinder.rotate(axis=vector(0, 1, 0), angle=rotation_speed)