class Vector:
    def __init__(self, x_coordinate=0, y_coordinate=0, z_coordinate=0):
        self.__x_coordinate = x_coordinate
        self.__y_coordinate = y_coordinate
        self.__z_coordinate = z_coordinate

    def magnitude(self):
        mag = (self.__x_coordinate**2 + self.__y_coordinate**2 + self.__z_coordinate**2)**(1/2)
        return mag

    def __str__(self):
        if not self.__z_coordinate:
            return f'The Details of the vector are:\nX - Coordinate: {self.__x_coordinate}\nY - Coordinate: {self.__y_coordinate}\n'
        else:
            return f'The Details of the vector are:\nX - Coordinate: {self.__x_coordinate}\nY - Coordinate: {self.__y_coordinate}\nZ - Coordinate: {self.__z_coordinate}\n'


pointObj = Vector(1, 2, 2)
print(pointObj.magnitude())
