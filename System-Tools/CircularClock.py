import turtle, time  # Import the turtle graphics and time modules
from datetime import datetime  # Import the datetime module to get the current time

# Set up the turtle screen (background color, size, and disabling automatic updates)
screen = turtle.Screen(); screen.bgcolor("black"); screen.setup(600, 600); screen.tracer(0)

# Set up the turtle (hide it, set speed, and color for drawing)
pen = turtle.Turtle(); pen.hideturtle(); pen.speed(0); pen.color("white")

# Function to draw the clock face, hour markers, digits, and hands
def draw_clock(h, m, s):
    pen.clear()  # Clear the previous drawing
    pen.penup(); pen.goto(0, 210); pen.setheading(180); pen.pendown(); pen.circle(210)
    # Draw the clock's outer circle

    # Draw the 12 hour markers and digits
    for i in range(12):
        angle = i * 30
        pen.penup(); pen.goto(0, 0); pen.setheading(90); pen.rt(angle); pen.fd(190); pen.pendown(); pen.fd(20)
        # For each hour marker, move to the starting position, rotate to the correct angle, and draw the marker

        pen.penup(); pen.goto(0, 0); pen.setheading(90); pen.rt(angle); pen.fd(160)
        pen.write(str(i + 1), align="center", font=("Arial", 18, "normal"))
        # Move the pen slightly inward and write the corresponding digit

    # Draw the hour, minute, and second hands
    for angle, length, color in [(h * 30 + m * 0.5, 100, "white"), (m * 6, 150, "blue"), (s * 6, 180, "red")]:
        pen.penup(); pen.goto(0, 0); pen.setheading(90); pen.rt(angle); pen.color(color); pen.pendown(); pen.fd(length)
        # Calculate the angle and length for each hand, set the color, and draw the hand from the center

# Main loop to update the clock every second
while True:
    # Get the current hour, minute, and second
    h, m, s = datetime.now().hour % 12, datetime.now().minute, datetime.now().second
    draw_clock(h, m, s); screen.update(); time.sleep(1)  # Draw the clock and update the screen every second

turtle.done()  # Keep the window open


