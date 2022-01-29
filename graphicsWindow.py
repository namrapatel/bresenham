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

    def drawLine(self,point1,point2,color):
        x1 = point1.get(0,0)
        x2 = point2.get(0,0)

        y1 = point1.get(1,0)
        y2 = point2.get(1,0)
        
        if abs(y2-y1) < abs(x2-x1):
            if x1 > x2:
                self.drawLow(x2,y2,x1,y1,color)
            else:
                self.drawLow(x1,y1,x2,y2,color)
        else:
            if y1 > y2:
                self.drawHigh(x2,y2,x1,y1,color)
            else:
                self.drawHigh(x1,y1,x2,y2,color)

    def drawLow(self,x1,y1,x2,y2,color):
        dx = x2-x1
        dy = y2-y1
        yi = 1
        if dy < 0:
            yi = -1
            dy = -dy

        D = 2*dy - dx
        y = y1
        
        for x in range(int(x1),int(x2)):
            self.drawPoint((x,y),color)
            if D > 0:
                y = y + yi
                D = D + 2*(dy-dx)
            else:
                D = D + 2*dy

    def drawHigh(self,x1,y1,x2,y2,color):
        dx = x2-x1
        dy = y2-y1
        xi = 1
        if dx < 0:
            xi = -1
            dx = -dx

        D = 2*dx - dy
        x = x1

        for y in range(int(y1),int(y2)):
            self.drawPoint((x,y),color)
            if D > 0:
                x = x + xi
                D = D + 2*(dx-dy)
            else:
                D = D + 2*dx

    def saveImage(self,fileName):
        self.__canvas.save(fileName)

    def showImage(self):
        self.__canvas.show()

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height
