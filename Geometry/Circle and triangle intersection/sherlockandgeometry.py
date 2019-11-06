from math import sqrt
class CircleTriangleIntersection:
    def __init__(self,x,y,r,t1,t2,t3):
        self.x = x
        self.y = y
        self.radius = r
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3

    def is_intersect(self):
        """
        Analytical solving:
            The equation of the 2-dimensional circle is  (x - x0)^2 + (y - yo)^ = r^2
            The triangle can be presented as three lines. We can write down the equation of a point on a line.
            For each line:
                x = x1 + t(x2 - x1)
                y = y1 + t(y2 - y1)
            To solve the task we substitute our equation of the line into the equation of circle.
            It gives us a quadratic equation:
                a*t^2 + b*t + c = 0, where:
                    x0 = x3
                    y0 = y3
                    a = (x2 - x1)^2 + (y2 - y1)^2
                    b = 2[ (x2 - x1)(x1 - x3) + (y2 -y1)(y1 - y3) ]
                    c = x3^2 + y3^2 + x1^2 + y1^2  - 2[ x3x1 + y3y1 ] - r^2

                Knowing the coefficients a, b and c we can find discriminant:
                    D = b^2 - 4ac
                    If D < 0: the line and the circle does not intersect
                    If D = 0: the line intersect the circle at one point
                    If D > 0: the line intersect the circle at two points

            So, we must check if at least one side of the triangle crosses the circle
        :return: string
        """
        if self.calculate_roots(self.t1, self.t3, self.x, self.y, self.radius) == "YES":
            return F"YES"
        elif self.calculate_roots(self.t1, self.t2, self.x, self.y, self.radius) == "YES":
            return F"YES"
        elif self.calculate_roots(self.t2, self.t3, self.x, self.y, self.radius) == "YES":
            return F"YES"
        else:
            return F"NO"

    def calculate_roots(self, point1, point2, x, y, r):
        """
        Because we solving the equation with respect to parametrized lines, there must be an imposed condition on the roots:
        0 <= root <= 1
        :param point1:
        :param point2:
        :param x:
        :param y:
        :param r:
        :return: string / "YES"/"NO"
        """
        a = (point2[0] - point1[0])**2 + (point2[1]- point1[1])**2
        b = 2*((point2[0]-point1[0])*(point1[0]-x) + (point2[1]-point1[1])*(point1[1]-y))
        c = x**2 + y**2 + point1[0]**2 + point1[1]**2 - 2*(x*point1[0] + y*point1[1]) - r**2
        discriminant = b**2 - 4*a*c
        if discriminant < 0:
            return F"NO"
        elif discriminant == 0:
            root = -b/(2*a)
            if 0.0 <= root <= 1.0:
                return F"YES"
            else:
                return F"NO"
        elif discriminant >= 0:
            root1 = (-b + sqrt(discriminant))/(2*a)
            root2 = (-b - sqrt(discriminant))/(2 * a)
            if 0.0 <= root1 <= 1.0 or 0.0 <= root2 <= 1.0:
                return F"YES"
            else:
                return F"NO"


r = CircleTriangleIntersection(0,0,10,[10,0],[15,0],[15,5])
print(r.is_intersect())