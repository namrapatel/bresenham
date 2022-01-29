import operator
from PIL import Image

class graphicsWindow:

    def __init__(self,width=640,height=480):
        self.__mode = 'RGB'
        self.__width = width
        self.__height = height
        self.__canvas = Image.new(self.__mode,(self.__width,self.__height))
        self.__image = self.__canvas.load()

    def drawPoint(self,point,color):
        if 0 <= point[0] < self.__width and 0 <= point[1] < self.__height:
            self.__image[point[0],point[1]] = color


    """
    Module Name: drawLine
    Author: Namra Patel
    Date: 28/01/2022
    Purpose: Performs various checks to determine line slope and direction, then calls
    the appropriate line drawing function that implements Bresenham's Integer Line Algorithm.

    Parameters:
        self: The graphicsWindow object.
        point1: The first point of the line.
        point2: The second point of the line.
        color: The color of the line.
    """
    def drawLine(self,point1,point2,color):
        # Get the values for x1 and x2 from the matrix.
        x1 = point1.get(0,0)
        x2 = point2.get(0,0)

        # Get the values for y1 and y2 from the matrix.
        y1 = point1.get(1,0)
        y2 = point2.get(1,0)
        
        # Check if the line has a low slope, if so, use the drawLowSlope (for slopes between -1 and 1) function.
        # Otherwise, use the drawSteepSlope (for slopes less than -1 or greater than 1) function. 
        if abs(y2 - y1) < abs(x2 - x1):
            # Reverse the points if the line is going left to right (when x1 > x2).
            if x1 > x2:
                self.drawLowSlope(x2, y2, x1, y1, color)
            else:
                self.drawLowSlope(x1, y1, x2, y2, color)
        else:
            # Reverse the points if the line is going up to down (when y1 > y2).
            if y1 > y2:
                self.drawSteepSlope(x2, y2, x1, y1, color)
            else:
                self.drawSteepSlope(x1, y1, x2, y2, color)


    """
    Module Name: drawLowSlope
    Author: Namra Patel
    Date: 28/01/2022
    Purpose: Implementation of Bresenham's Integer Line Algorithm for lines with a slope between -1 and 1.

    Parameters:
        self: The graphicsWindow object.
        x1: The x-coordinate of the first point of the line.
        y1: The y-coordinate of the first point of the line.
        x2: The x-coordinate of the second point of the line.
        y2: The y-coordinate of the second point of the line.
        color: The color of the line.
    """
    def drawLowSlope(self, x1, y1, x2, y2, color):
        # Calculate the total change in x and y for the line.
        dx = x2 - x1
        dy = y2 - y1
        y_increment = 1 # Initialize the y step direction.

        # Check if y needs to increase or decrease, if decreasing, set y_increment and dy to negatives.
        if dy < 0:
            y_increment = -1
            dy = -dy

        # Calculate the initial error term (difference).
        difference = 2*dy - dx
        # Initialize y (used to draw point) as y1 to begin.
        y = y1 

        # Loop through all points between x1 and x2.
        # Cast coords to int because they are originally floats.
        for x in range(int(x1), int(x2)):
            self.drawPoint((x, y), color) # Draw the point.

            # If the error term is greater than, increment y in the predetermined direction,
            # and adjust the error term.
            if difference > 0:
                y = y + y_increment
                difference = difference + 2*(dy - dx)
            else:
                difference = difference + 2*dy

    """
    Module Name: drawSteepSlope
    Author: Namra Patel
    Date: 28/01/2022
    Purpose: Implementation of Bresenham's Integer Line Algorithm for lines with a slope between less than -1 or greater than 1.

    Parameters:
        self: The graphicsWindow object.
        x1: The x-coordinate of the first point of the line.
        y1: The y-coordinate of the first point of the line.
        x2: The x-coordinate of the second point of the line.
        y2: The y-coordinate of the second point of the line.
        color: The color of the line.
    """
    def drawSteepSlope(self, x1, y1, x2, y2, color):
        # Calculate the total change in x and y for the line.
        dx = x2 - x1
        dy = y2 - y1
        x_increment = 1 # Initialize the x step direction.

        # Check if x needs to increase or decrease, if decreasing, set x_increment and dx to negatives.
        if dx < 0:
            x_increment = -1
            dx = -dx

        # Calculate the initial error term (difference).
        difference = 2*dx - dy
        # Initialize x (used to draw point) as x1 to begin.
        x = x1

        # Loop through all points between y1 and y2.
        # Cast coords to int because they are originally floats.
        for y in range(int(y1), int(y2)):
            self.drawPoint((x, y), color) # Draw the point.

            # If the error term is greater than, increment y in the predetermined direction,
            # and adjust the error term.
            if difference > 0:
                x = x + x_increment
                difference = difference + 2*(dx - dy)
            else:
                difference = difference + 2*dx

    def saveImage(self,fileName):
        self.__canvas.save(fileName)

    def showImage(self):
        self.__canvas.show()

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height
