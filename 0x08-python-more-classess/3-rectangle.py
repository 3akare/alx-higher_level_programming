#!/usr/bin/python3
"""Define a class"""


class Rectangle:
    """Represents a rectangle"""

    def __init__(self, width=0, height=0):
        """
            Intailize a new rectangle
            Args:
                width(int): width of new rectangle
                height(int): height of new rectangle
        """
        if (not isinstance(width, int)):
            raise TypeError('width must be an integer')
        if (width < 0):
            raise ValueError('width must be >= 0')
        if (not isinstance(height, int)):
            raise TypeError('height must be an integer')
        if (height < 0):
            raise ValueError('height must be >= 0')
        self.__width = width
        self.__height = height

    def area(self):
        """
            Area function
            Args:
                self: an instance of Rectangle
            Return: the area of a rectangle object
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
            perimeter function
            Args:
                self: an instance of Rectangle
            Return: the perimeter of a rectangle object
        """
        if (self.__width == 0 and self.__height == 0):
            return (0)
        return (2 * (self.__width + self.__height))

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise TypeError('height must be >= 0')
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise TypeError('width must be >= 0')
        self.__width = value

    def __str__(self):
        if (self.__height == 0 or self.__width == 0):
            print("")
        else:
            for i in range(self.__height):
                print("", end="")
                for j in range(self.__width):
                    print('#', end="")
                if (i != self.__height - 1):
                    print("")
        return ("")
