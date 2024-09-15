# square.py
# This code draws a square using the picture module. Replace the example code below with your own to draw the square.

import picture

# Creates a blank canvas that is 300 pixels tall and 300 pixels wide
picture.new_picture(300, 300)

# Sets the stroke width to 8 pixels and the color to purple
picture.set_pen_width(8)
picture.set_outline_color("purple")

# Starts the pen's location at 100 pixels down and right from the top-left corner
picture.set_position(100, 100)

# Sets the initial angle to 0 degrees: straight right.
picture.set_direction(0)

# Here is some code to show you what a drawing can look like.
picture.draw_forward(50)
picture.rotate(90)
picture.draw_forward(50)
picture.rotate(90)
picture.draw_forward(50)
picture.rotate(90)
picture.draw_forward(50)
picture.rotate(90)
picture.draw_forward(50)

# For Warmup part A, use the functions above and a for loop with a range to draw a square. Hint: How might you "loopify" the above code?
# Comment out lines 20-28 (can highlight them all and use the Control-/ or Command-/ keyboard shortcut) above and add new code below!



# Saves your picture as a png file
picture.save_picture("square_picture.png")
