class Vector:
    def __init__(self, x_coordinate=0, y_coordinate=0, z_coordinate=0):
        self.__x_coordinate = x_coordinate
        self.__y_coordinate = y_coordinate
        self.__z_coordinate = z_coordinate

    # The property decorator creates a property vector for the class Vector
    @property
    def vector(self):
        return f'{self.__x_coordinate}i + {self.__y_coordinate}j + {self.__z_coordinate}k'

    # Once a property has been created then the setter can be created ..
    @vector.setter
    def vector(self, value):
        value = value.split(' ')
        self.__x_coordinate = value[0]
        self.__y_coordinate = value[1]
        self.__z_coordinate = value[2]

    # This is a destructor function which is called during the destruction of the vector property.
    @vector.deleter
    def vector(self):
        print("Deleting Vector!")
        self.__x_coordinate = None
        self.__y_coordinate = None
        self.__z_coordinate = None

    def magnitude(self):
        mag = (self.__x_coordinate**2 + self.__y_coordinate**2 + self.__z_coordinate**2)**(1/2)
        return mag

    def __str__(self):
        if not self.__z_coordinate:
            return f'The Details of the vector are:\nX - Coordinate: {self.__x_coordinate}\nY - Coordinate: {self.__y_coordinate}\n'
        else:
            return f'The Details of the vector are:\nX - Coordinate: {self.__x_coordinate}\nY - Coordinate: {self.__y_coordinate}\nZ - Coordinate: {self.__z_coordinate}\n'

    # OVERRIDING THE * OPERATOR THROUGH __mul__ magic function ...
    def __mul__(self, other):
        x_prod = self.__x_coordinate * other.__x_coordinate
        y_prod = self.__y_coordinate * other.__y_coordinate
        z_prod = self.__z_coordinate * other.__z_coordinate
        return x_prod + y_prod + z_prod

    # OVERRIDING THE + OPERATOR THROUGH __add__ magic function ...
    def __add__(self, other):
        angle = (self * other)/(self.magnitude() * other.magnitude())
        value = self.magnitude() ** 2 + other.magnitude() ** 2 + 2*self.magnitude()*other.magnitude()*angle
        return value**(1/2)


vector1 = Vector(1, 2, 2)
vector2 = Vector(1, 2, 2)
print(vector1+vector2)
print(vector1*vector2)
print(vector1.magnitude())
print(vector2.magnitude())
print("<<<<< @property decorator : Result >>>>>>")
print(vector1.vector)
vector1.vector = '1 2 4'
print(vector1)
del vector1.vector