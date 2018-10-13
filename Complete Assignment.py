#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n10000569  
#    Student name: SEAN O'CONNELL
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  BUILDING BLOCKS
#
#  This assignment tests your skills at defining functions, processing
#  data stored in lists and performing the arithmetic calculations
#  necessary to display a complex visual image.  The incomplete
#  Python script below is missing a crucial function, "stack_blocks".
#  You are required to complete this function so that when the
#  program is run it produces a picture of a pile of building blocks
#  whose arrangement is determined by data stored in a list which
#  specifies the blocks' locations.  See the instruction
#  sheet accompanying this file for full details.
#
#  Note that this assignment is in two parts, the second of which
#  will be released only just before the final deadline.  This
#  template file will be used for both parts and you will submit
#  your final solution as a single file, whether or not you
#  complete both parts of the assignment.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.

from turtle import *
from math import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

block_size = 250 # pixels
top_and_bottom_border = 75 # pixels
left_and_right_border = 150 # pixels
canvas_width = (block_size + left_and_right_border) * 2
canvas_height = (block_size + top_and_bottom_border) * 2

#
#--------------------------------------------------------------------#



#-----Functions for Managing the Canvas------------------------------#
#
# The functions in this section are called by the main program to
# set up the drawing canvas for your image.  You should not change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image
def create_drawing_canvas():

    # Set up the drawing canvas
    setup(canvas_width, canvas_height)

    # Set the coordinate system so that location (0, 0) is centred on
    # the point where the blocks will be stacked
    setworldcoordinates(-canvas_width / 2, -top_and_bottom_border,
                        canvas_width / 2, canvas_height - top_and_bottom_border)

    # Draw as fast as possible
    tracer(False)

    # Colour the sky blue
    bgcolor('sky blue')

    # Draw the ground as a big green rectangle (sticking out of the
    # bottom edge of the drawing canvas slightly)
    overlap = 50 # pixels
    penup()
    goto(-(canvas_width / 2 + overlap), -(top_and_bottom_border + overlap)) # start at the bottom-left
    fillcolor('pale green')
    begin_fill()
    setheading(90) # face north
    forward(top_and_bottom_border + overlap)
    right(90) # face east
    forward(canvas_width + overlap * 2)
    right(90) # face south
    forward(top_and_bottom_border + overlap)
    end_fill()
    penup()

    # Draw a friendly sun peeking into the image
    goto(-canvas_width / 2, block_size * 2)
    color('yellow')
    dot(250)

    # Reset everything ready for the student's solution
    color('black')
    width(1)
    penup()
    home()
    setheading(0)
    tracer(True)
    

# As a debugging aid, mark the coordinates of the centres and corners
# of the places where the blocks will appear
def mark_coords(show_corners = False, show_centres = False):

    # Go to each coordinate, draw a dot and print the coordinate, in the given colour
    def draw_each_coordinate(colour):
        color(colour)
        for x_coord, y_coord in coordinates:
            goto(x_coord, y_coord)
            dot(4)
            write(' ' + str(x_coord) + ', ' + str(y_coord), font = ('Arial', 12, 'normal'))

    # Don't draw lines between the coordinates
    penup()

    # The list of coordinates to display
    coordinates = []

    # Only mark the corners if the corresponding argument is True
    if show_corners:
        coordinates = [[-block_size, block_size * 2], [0, block_size * 2], [block_size, block_size * 2],
                       [-block_size, block_size], [0, block_size], [block_size, block_size],
                       [-block_size, 0], [0, 0], [block_size, 0]]
        draw_each_coordinate('dark blue')

    # Only mark the centres if the corresponding argument is True
    if show_centres:
        coordinates = [[-block_size / 2, block_size / 2], [block_size / 2, block_size / 2],
                       [-block_size / 2, block_size + block_size / 2], [block_size / 2, block_size + block_size / 2]]
        draw_each_coordinate('red')

    # Put the cursor back how it was
    color('black')
    home()


# End the program by hiding the cursor and releasing the window
def release_drawing_canvas():
    tracer(True)
    hideturtle()
    done()
    
#
#--------------------------------------------------------------------#



#-----Test data------------------------------------------------------#
#
# These are the data sets you will use to test your code.
# Each of the data sets is a list specifying the locations of
# the building blocks:
#
# 1. The name of the block, from 'Block A' to 'Block D'
# 2. The place to put the block, either 'Top left', 'Top right',
#    'Bottom left' or 'Bottom right'
# 3. The block's orientation, meaning the direction in which the top
#    of the block is pointing, either 'Up', 'Down', 'Left' or 'Right'
# 4. An optional mystery value, 'X' or 'O', whose purpose will be
#    revealed only in the second part of the assignment
#
# Each data set does not necessarily mention all four blocks.
#
# You can create further data sets, but do not change any of the
# given ones below because they will be used to test your submission.
#

# The following data set doesn't require drawing any blocks
# at all.  You may find it useful as a dummy argument when you
# first start developing your "draw_attempt" function.

arrangement_00 = []

# Each of the following data sets specifies drawing just one block
# in an upright orientation.  You may find them useful when
# creating your individual pieces.

arrangement_01 = [['Block A', 'Bottom left', 'Up', 'O']]
arrangement_02 = [['Block B', 'Bottom right', 'Up', 'O']]
arrangement_03 = [['Block C', 'Bottom left', 'Up', 'O']]
arrangement_04 = [['Block D', 'Bottom right', 'Up', 'O']]

# Each of the following data sets specifies drawing just one block
# in non-upright orientations.  You may find them useful when
# ensuring that you can draw all the blocks facing in different
# directions.

arrangement_10 = [['Block A', 'Bottom left', 'Down', 'O']]
arrangement_11 = [['Block A', 'Bottom right', 'Left', 'O']]
arrangement_12 = [['Block A', 'Bottom left', 'Right', 'O']]

arrangement_13 = [['Block B', 'Bottom left', 'Down', 'O']]
arrangement_14 = [['Block B', 'Bottom right', 'Left', 'O']]
arrangement_15 = [['Block B', 'Bottom left', 'Right', 'O']]

arrangement_16 = [['Block C', 'Bottom left', 'Down', 'O']]
arrangement_17 = [['Block C', 'Bottom right', 'Left', 'O']]
arrangement_18 = [['Block C', 'Bottom left', 'Right', 'O']]

arrangement_19 = [['Block D', 'Bottom left', 'Down', 'O']]
arrangement_20 = [['Block D', 'Bottom right', 'Left', 'O']]
arrangement_21 = [['Block D', 'Bottom left', 'Right', 'O']]

# The following data sets all stack various numbers of
# blocks in various orientations

arrangement_30 = [['Block C', 'Bottom right', 'Up', 'O'],
                  ['Block D', 'Top right', 'Up', 'O']]
arrangement_31 = [['Block A', 'Bottom left', 'Up', 'O'],
                  ['Block C', 'Bottom left', 'Up', 'O']]

arrangement_32 = [['Block B', 'Bottom right', 'Up', 'O'],
                  ['Block D', 'Bottom left', 'Up', 'O'],
                  ['Block C', 'Top right', 'Up', 'O']]
arrangement_33 = [['Block B', 'Bottom right', 'Up', 'O'],
                  ['Block D', 'Bottom left', 'Up', 'O'],
                  ['Block A', 'Top left', 'Up', 'O']]
arrangement_34 = [['Block B', 'Bottom left', 'Up', 'O'],
                  ['Block A', 'Bottom right', 'Up', 'O'],
                  ['Block D', 'Top left', 'Up', 'O'],
                  ['Block C', 'Top right', 'Up', 'O']]

arrangement_40 = [['Block C', 'Bottom right', 'Left', 'O'],
                  ['Block D', 'Top right', 'Right', 'O']]
arrangement_41 = [['Block A', 'Bottom left', 'Down', 'O'],
                  ['Block C', 'Bottom left', 'Up', 'O']]

arrangement_42 = [['Block B', 'Bottom right', 'Left', 'O'],
                  ['Block D', 'Bottom left', 'Left', 'O'],
                  ['Block C', 'Top right', 'Down', 'O']]
arrangement_43 = [['Block B', 'Bottom right', 'Right', 'O'],
                  ['Block D', 'Bottom left', 'Left', 'O'],
                  ['Block A', 'Top left', 'Right', 'O']]
arrangement_44 = [['Block B', 'Bottom left', 'Down', 'O'],
                  ['Block A', 'Bottom right', 'Left', 'O'],
                  ['Block D', 'Top left', 'Right', 'O'],
                  ['Block C', 'Top right', 'Up', 'O']]

arrangement_50 = [['Block B', 'Bottom right', 'Left', 'O'],
                  ['Block D', 'Bottom left', 'Left', 'O'],
                  ['Block C', 'Top right', 'Down', 'X']]
arrangement_51 = [['Block B', 'Bottom right', 'Right', 'O'],
                  ['Block D', 'Bottom left', 'Left', 'O'],
                  ['Block A', 'Top left', 'Right', 'X']]
arrangement_52 = [['Block B', 'Bottom left', 'Down', 'O'],
                  ['Block A', 'Bottom right', 'Left', 'O'],
                  ['Block D', 'Top left', 'Right', 'O'],
                  ['Block C', 'Top right', 'Up', 'X']]

arrangement_60 = [['Block B', 'Bottom right', 'Left', 'X'],
                  ['Block D', 'Bottom left', 'Left', 'O'],
                  ['Block C', 'Top right', 'Down', 'O']]
arrangement_61 = [['Block B', 'Bottom right', 'Right', 'O'],
                  ['Block D', 'Bottom left', 'Left', 'X'],
                  ['Block A', 'Top left', 'Right', 'O']]
arrangement_62 = [['Block B', 'Bottom left', 'Down', 'X'],
                  ['Block A', 'Bottom right', 'Left', 'X'],
                  ['Block D', 'Top left', 'Right', 'O'],
                  ['Block C', 'Top right', 'Up', 'O']]

# The following arrangements create your complete image, but
# oriented the wrong way

arrangement_80 = [['Block C', 'Bottom right', 'Left', 'O'],
                  ['Block D', 'Top right', 'Left', 'X'],
                  ['Block A', 'Bottom left', 'Left', 'O'],
                  ['Block B', 'Top left', 'Left', 'O']]

arrangement_81 = [['Block B', 'Bottom right', 'Right', 'X'],
                  ['Block D', 'Bottom left', 'Right', 'X'],
                  ['Block A', 'Top right', 'Right', 'O'],
                  ['Block C', 'Top left', 'Right', 'O']]

arrangement_89 = [['Block A', 'Bottom right', 'Down', 'O'],
                  ['Block C', 'Top right', 'Down', 'O'],
                  ['Block B', 'Bottom left', 'Down', 'O'],
                  ['Block D', 'Top left', 'Down', 'O']]

# The following arrangements should create your complete image
# (but with the blocks stacked in a different order each time)

arrangement_90 = [['Block C', 'Bottom left', 'Up', 'O'],
                  ['Block D', 'Bottom right', 'Up', 'O'],
                  ['Block B', 'Top right', 'Up', 'X'],
                  ['Block A', 'Top left', 'Up', 'O']]

arrangement_91 = [['Block D', 'Bottom right', 'Up', 'X'],
                  ['Block C', 'Bottom left', 'Up', 'X'],
                  ['Block A', 'Top left', 'Up', 'O'],
                  ['Block B', 'Top right', 'Up', 'O']]

arrangement_92 = [['Block D', 'Bottom right', 'Up', 'X'],
                  ['Block B', 'Top right', 'Up', 'O'],
                  ['Block C', 'Bottom left', 'Up', 'O'],
                  ['Block A', 'Top left', 'Up', 'O']]

arrangement_99 = [['Block C', 'Bottom left', 'Up', 'O'],
                  ['Block D', 'Bottom right', 'Up', 'O'],
                  ['Block A', 'Top left', 'Up', 'O'],
                  ['Block B', 'Top right', 'Up', 'O']]

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "stack_blocks" function.
#

##Draw the stack of blocks as per the provided data set
def stack_blocks(arrangement):
    
    #Setting the width of all line drawings so that it is down to the exact pixel
    width(1)
            
    #A function to check the orientation of the block
    def direction(direct):
        
        #Make the variable head a global so that all functions can access it
        global head
        
        #Check which way the shape is orientated
        if arrangement[direct][2] == "Left":
            up = 0
            left = 90
            right = -90
            down = 180
            
        elif arrangement[direct][2] == "Right":
            up = 180
            left = -90
            right = 90
            down = 0
            
        elif arrangement[direct][2] == "Down":
            up = -90
            left = 0
            right = 180
            down = 90
            
        elif arrangement[direct][2] == "Up":
            up = 90
            left = 180
            right = 0
            down = -90

        #Return head so that the variables are correct when they are used
        head = (up,down,left,right)
        return head

    #Draw white background
    def bground(draw):            

        #Ask where the background should start to draw
        goto(bxx,byy)

        #Draw the background with a colour white and
        #start where the elif statement tells you
        color('white')
        begin_fill()
        pd()
        setheading(head[0])
        forward(250)
        setheading(head[3])
        forward(250)
        setheading(head[1])
        forward(250)
        setheading(head[2])
        forward(250)
        pu()
        end_fill()
        home()

    #Outline each block so that the 
    def outline():

        #Draws the action outline using the default variables
        setheading(head[0])
        color('black')
        pd()
        width(5)
        forward(250)
        setheading(head[3])
        forward(250)
        setheading(head[1])
        forward(250)
        setheading(head[2])
        forward(250)
        pu()

    #Function to determine where the drawing will start to draw from with the direction of the drawing
    def orientation(orient):
        
        #Setup some globalised variables so that other functions can access them
        global xx
        global yy
        global bxx
        global byy

        #Elif statement to decide which corner the drawing will start from
        if arrangement[orient][1] == 'Bottom left' and arrangement[orient][2] == 'Down':
            xx = -250
            yy = 0
            bxx = 0
            byy = 250
            
        elif arrangement[orient][1] == 'Bottom left' and arrangement[orient][2] == 'Left':
            xx = 0
            yy = 0
            bxx = -250
            byy = 250
            
        elif arrangement[orient][1] == 'Bottom left' and arrangement[orient][2] == 'Right':
            xx = -250
            yy = 250
            bxx = 0
            byy = 0
            
        elif arrangement[orient][1] == 'Bottom left' and arrangement[orient][2] == 'Up':
            xx = 0
            yy = 250
            bxx = -250
            byy = 0
            
        elif arrangement[orient][1] == 'Bottom right' and arrangement[orient][2] == 'Down':
            xx = 250
            yy = 0
            bxx = 250
            byy = 250
            
        elif arrangement[orient][1] == 'Bottom right' and arrangement[orient][2] == 'Left':
            xx = 250
            yy = 250
            bxx = 0
            byy = 250
            
        elif arrangement[orient][1] == 'Bottom right' and arrangement[orient][2] == 'Right':
            xx = 0
            yy = 0
            bxx = 250
            byy = 0
            
        elif arrangement[orient][1] == 'Bottom right' and arrangement[orient][2] == 'Up': 
            xx = 0
            yy = 250
            bxx = 0
            byy = 0
            
        elif arrangement[orient][1] == 'Top left' and arrangement[orient][2] == 'Down':
            xx = -250
            yy = 500
            bxx = 0
            byy = 500
            
        elif arrangement[orient][1] == 'Top left' and arrangement[orient][2] == 'Left':
            xx = -250
            yy = 250
            bxx = -250
            byy = 500
            
        elif arrangement[orient][1] == 'Top left' and arrangement[orient][2] == 'Right':
            xx = 0
            yy = 500
            bxx = 0
            byy = 250
            
        elif arrangement[orient][1] == 'Top left' and arrangement[orient][2] == 'Up': 
            xx = 0
            yy = 250
            bxx = -250
            byy = 250
            
        elif arrangement[orient][1] == 'Top right' and arrangement[orient][2] == 'Down':
            xx = 250
            yy = 500
            bxx = 250
            byy = 500
            
        elif arrangement[orient][1] == 'Top right' and arrangement[orient][2] == 'Left':
            xx = 0
            yy = 500
            bxx = 0
            byy = 250
            
        elif arrangement[orient][1] == 'Top right' and arrangement[orient][2] == 'Right':
            xx = 250
            yy = 250
            bxx = 250
            byy = 250
            
        elif arrangement[orient][1] == 'Top right' and arrangement[orient][2] == 'Up': 
            xx = 0
            yy = 250
            bxx = 0
            byy = 250 

        #Give the x and y co-ordinates so the other functions can move accordingly
        return xx
        return yy
        return bxx
        return byy

    #Draw the bottom left quadrant      
    def bleft():

        #All goto co-ordinates (xx,yy) are based
        #from the direction and orientation of the block
        
        #The shadow of the circle
        pu()
        color('dark green')
        begin_fill()
        goto(xx,yy)
        setheading(head[1])
        forward(250)
        setheading(head[2])
        circle(-200,100)
        setheading(head[3])
        goto(xx,yy)
        end_fill()

        #The actual circle
        color('green')
        goto(xx,yy)
        setheading(head[1])
        forward(200)
        setheading(head[2])
        begin_fill()
        circle(-200,90)
        setheading(head[3])
        goto(xx,yy)
        end_fill()

        #The shadow of the tick
        color('dark green')
        goto(xx,yy)
        setheading(head[1])
        forward(25)
        setheading(head[2])
        forward(50)
        setheading(head[2]+45)
        begin_fill()
        forward(50)
        setheading(head[1]+45)
        forward(90)
        setheading(head[3]+45)
        forward(30)
        setheading(head[0])
        forward(74)
        setheading(head[2])
        forward(5)
        setheading(head[2] + 45)
        forward(25)
        setheading(head[0]+45)
        forward(30)
        end_fill()

        #The white tick
        color('white')
        goto(xx,yy)
        setheading(head[2])
        forward(50)
        setheading(head[2]+45)
        begin_fill()
        forward(50)
        setheading(head[1]+45)
        forward(90)
        setheading(head[3]+45)
        forward(30)
        setheading(head[0])
        forward(77)
        setheading(head[2])
        forward(5)
        setheading(head[2] + 45)
        forward(25)
        setheading(head[0]+45)
        forward(25)
        end_fill()

        #Draw the outline by going to that co-ordinate
        goto(bxx,byy)
        outline()

    #Function for the bottom right square
    def bright():

        #All goto co-ordinates (xx,yy) are based
        #from the direction and orientation of the block
        
        #The shadow of the circle
        pu()
        color('dark green')
        begin_fill()
        goto(xx,yy)
        setheading(head[1])
        forward(250)
        setheading(head[3])
        circle(200,100)
        setheading(head[2])
        goto(xx,yy)
        end_fill()

        #The actual circle
        color('green')
        goto(xx,yy)
        setheading(head[3])
        forward(200)
        begin_fill()
        setheading(head[1])
        circle(-200,90)
        setheading(head[0])
        goto(xx,yy)
        end_fill()

        #The shadow of the tick
        color('dark green')
        goto(xx,yy)
        setheading(head[1])
        forward(102)
        begin_fill()
        setheading(head[3]+45)
        forward(145)
        setheading(head[2])
        goto(xx,yy)
        setheading(head[1])
        forward(77)
        end_fill()
        
        color('white')
        goto(xx,yy)
        setheading(head[1])
        forward(77.5)
        begin_fill()
        setheading(head[3]+45)
        forward(110)
        setheading(head[2])
        goto(xx,yy)
        setheading(head[1])
        forward(77)
        end_fill()

        #Outline the square starting from the goto co-ordinates
        goto(bxx,byy)
        outline()

    def tleft():

        #All goto co-ordinates (xx,yy) are based
        #from the direction and orientation of the block

        #The actual circle
        color('green')
        pu()
        goto(xx,yy)
        setheading(head[2])
        forward(200)
        setheading(head[0])
        begin_fill()
        circle(-200,90)
        setheading(head[1])
        goto(xx,yy)
        end_fill()

        #The tip of the tick
        color('white')
        goto(xx,yy)
        setheading(head[2])
        forward(50)
        setheading(head[0]-45)
        begin_fill()
        forward(6)
        setheading(head[3]-45)
        forward(6)
        end_fill()

        #The connection between the base of the tick
        #and the top of the tick
        goto(xx,yy)
        setheading(head[2])
        forward(5)
        begin_fill()
        setheading(head[0]-45)
        forward(8)
        setheading(head[1])
        forward(5)
        end_fill()

        #The outline of the square
        goto(bxx,byy)
        outline()

    def tright():

        #All goto co-ordinates (xx,yy) are based
        #from the direction and orientation of the block

        #The actual circle
        color('green')
        pu()
        goto(xx,yy)
        setheading(head[0])
        forward(200)
        setheading(head[3])
        begin_fill()
        circle(-200,90)
        setheading(head[2])
        goto(xx,yy)
        end_fill()

        #The shadow of the tick
        color('dark green')
        goto(xx,yy)
        begin_fill()
        setheading(head[0]-45)
        forward(130)
        setheading(head[3]-45)
        forward(71.8)
        setheading(head[1]-45)
        forward(60)
        goto(xx,yy)
        end_fill()

        #The white tick
        color('white')
        goto(xx,yy)
        begin_fill()
        setheading(head[0])
        forward(5.3578)
        setheading(head[0]-45)
        forward(140)
        setheading(head[3]-45)
        forward(57.8)
        setheading(head[1]-45)
        forward(89)
        goto(xx,yy)
        end_fill()

        #The outline of the square
        goto(bxx,byy)
        outline()
                
    
    ##Build the Top Left quadrant of the Superman logo
    def block(index):
    
        #Globalised the same variables so that other functions can access them
        global xx
        global yy
        global bxx
        global byy

        #Check which box it wants to draw in either bottom left, right or top left, right
        if arrangement[index][1] == "Bottom left":

            #Check if the square is to be drawn or not
            if arrangement[index][3] != "X":
                #Check which way the shape is orientated, directed
                orientation(index)
                direction(index)
                #Draw white background and the shape
                bground(index)
                bleft()
            
        elif arrangement[index][1] == "Bottom right":

            #Check if the square is to be drawn or not
            if arrangement[index][3] != "X":
                #Check which way the shape is orientated, directed
                orientation(index)
                direction(index)
                #Draw white background and the shape
                bground(index)
                bright()
            
        elif arrangement[index][1] == "Top left":

            #Check if it is to be drawn
            if arrangement[index][3] != "X":

                #Check every block to see if the bottom left block is present 
                for every_block in range(len(arrangement)):                    
                    if arrangement[every_block][1] == "Bottom left" and arrangement[every_block][3] == "X":

                        #BREAK is called to end the loop after teh vale has been found

                        #Find the angle of the shape and get the starting position for the drawing and background
                        if arrangement[index][2] == "Down":
                            xx = -250
                            yy = 0
                            bxx = -250
                            byy = 0
                            #Check which way the shape is directed
                            direction(index)
                            #Draw the background and shape
                            bground(index)
                            tleft()
                            break
                            
                        elif arrangement[index][2] == "Left":
                            xx = 0
                            yy = 0
                            bxx = 250
                            byy = 250
                            #Check which way the shape is directed
                            direction(index)
                            #Draw the background and shape
                            bground(index)
                            tleft()
                            break
                            
                        elif arrangement[index][2] == "Right":
                            xx = 0
                            yy = 250
                            bxx = 0
                            byy = 0
                            #Check which way the shape is directed
                            direction(index)
                            #Draw the background and shape
                            bground(index)
                            tleft()
                            break
                            
                        elif arrangement[index][2] == "Up": 
                            xx = 0
                            yy = 0
                            bxx = -250
                            byy = 0
                            #Check which way the shape is directed
                            direction(index)
                            #Draw the background and shape
                            bground(index)
                            tleft()
                            break

                    #Else print the top left block
                    elif every_block == (len(arrangement)-1) and arrangement[index][3] == "O":
                        #Check which way the shape is orientated, directed
                        orientation(index)
                        direction(index)
                        #Draw white background and the shape
                        bground(index)
                        tleft()
                        break
                        
            
        elif arrangement[index][1] == "Top right": 

            #Check if the square is to be drawn
            if arrangement[index][3] != "X":
                
                #Check every block to see if there is a bottom right block present
                for every_block in range(len(arrangement)):
                    if arrangement[every_block][1] == "Bottom right" and arrangement[every_block][3] == "X":

                        #BREAK is called to end the loop after teh vale has been found
                        
                        #Find the angle of the shape and get the starting position for the drawing and background
                        if arrangement[index][2] == "Down":
                            xx = 250
                            yy = 250
                            bxx = 250
                            byy = 250
                            #Check which way the shape is directed
                            direction(index)
                            #Draw the background and shape
                            bground(index)
                            tright()
                            break
                            
                        elif arrangement[index][2] == "Left":
                            xx = 0
                            yy = 250
                            bxx = 0
                            byy = 0
                            #Check which way the shape is directed
                            direction(index)
                            #Draw the background and shape
                            bground(index)
                            tright()
                            break
                            
                        elif arrangement[index][2] == "Right":
                            xx = 250
                            yy = 0
                            bxx = 250
                            byy = 0
                            #Check which way the shape is directed
                            direction(index)
                            #Draw the background and shape
                            bground(index)
                            tright()
                            break
                            
                        elif arrangement[index][2] == "Up":
                            xx = 0
                            yy = 0
                            bxx = 0
                            byy = 0
                            #Check which way the shape is directed
                            direction(index)
                            #Draw the background and shape
                            bground(index)
                            tright()
                            break

                    #Else print the top right block   
                    elif every_block == (len(arrangement)-1) and arrangement[index][3] == "O":
                        #Check which way the shape is orientated, directed
                        orientation(index)
                        direction(index)
                        #Draw white background and the shape
                        bground(index)
                        tright()
                        break


    #Loop for all blocks in the arrangement
    for blocks in arrangement:

        #Give the block an index value
        blockid = arrangement.index(blocks)

        #Loop through every value in the first slot [0] of the arrangement
        for arrange in blocks:
            
            #Wherever each block is give it that blockid and call the block function with that ID
            if arrange == "Block A":
                block(blockid)
                
            elif arrange == "Block B":
                block(blockid)
                
            elif arrange == "Block C":
                block(blockid)
                
            elif arrange == "Block D":
                block(blockid)

           
#
#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# drawing your jigsaw pieces.  Do not change any of this code except
# where indicated by comments marked '*****'.
#

# Set up the drawing canvas
create_drawing_canvas()

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** while the cursor moves around the screen
tracer(True)

# Give the window a title
# ***** Replace this title with one that describes the picture
# ***** produced by stacking your blocks correctly
title('A Tick With a Green Circle and Shadows')

# Display the corner and centre coordinates of the places where
# the blocks must be placed
# ***** If you don't want to display the coordinates change the
# ***** arguments below to False
mark_coords(True, True)

### Call the student's function to display the stack of blocks
### ***** Change the argument to this function to test your
### ***** code with different data sets
stack_blocks(arrangement_99)

# Exit gracefully
release_drawing_canvas()

#
#--------------------------------------------------------------------#

