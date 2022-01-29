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

    def drawLow(self,x2,y2,x1,y1,color):
        return 1

    def drawHigh(self,x2,y2,x1,y1,color):
        return 1

    def saveImage(self,fileName):
        self.__canvas.save(fileName)

    def showImage(self):
        self.__canvas.show()

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height
