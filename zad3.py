import math

class Line:
    def __init__(self, coord1, coord2):
        self.x1 = coord1[0]
        self.y1 = coord1[1]
        self.x2 = coord2[0]
        self.y2 = coord2[1]

    def distance(self):
        return math.sqrt(math.pow(self.x2 - self.x1, 2) + math.pow(self.y2 - self.y1, 2))
        
    def slope(self):
        return (self.y2 - self.y1)/(self.x2 - self.x1)

line = Line((3, 2), (8, 10))

print("Distance = " + "%.2f" % line.distance() + "; Slope = " + "%.2f" % line.slope())


    


