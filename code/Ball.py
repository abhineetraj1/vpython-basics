from vpython import *

# Create the ball object
ball = sphere(pos=vector(0, 0, 0), radius=1, color=color.red)

# Set ball rotation parameters
rotate_ball = True
rotation_speed = 0.01

def toggle_rotation():
    global rotate_ball
    rotate_ball = not rotate_ball

# Create a button to toggle ball rotation
toggle_button = button(bind=toggle_rotation, text="Toggle Rotation")

# Create a scene to display the ball
scene = canvas(title="Rotating Ball", width=800, height=600)

# Define the rotation animation
angle = 0

# Run the simulation
while True:
    rate(60)
    if rotate_ball:
        ball.rotate(axis=vector(0, 1, 0), angle=rotation_speed)