#!/usr/bin/python3
"""This module contains a rectangle class"""

from models.base import Base


class Rectangle(Base):
    """Represent a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes attributes of the object"""
        self.width = width
        self.height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
    
    # getter methods
    @property
    def width(self):
        """Get the value of width"""
        return self.__width
    
    @property
    def height(self):
        """Get the value of height"""
        return self.__height
    
    @property
    def x(self):
        """Get the value of x"""
        return self.__x
    
    @property
    def y(self):
        """Get the value of y"""
        return self.__y
    
    #setter methods
    @width.setter
    def width(self, value):
        """ Set the value of width"""
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        
        if value <= 0:
            raise ValueError("width must be > 0")
        
        self.__width = value

    @height.setter
    def height(self, value):
        """ Set the value of height"""
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        
        if value <= 0:
            raise ValueError("height must be > 0")
        
        self.__height = value

    @x.setter
    def x(self, value):
        """ Set the value of x"""
        if (type(value) is not int):
            raise TypeError("x must be an integer")
        
        if value < 0:
            raise ValueError("x must be >= 0")
        
        self.__x = value

    @y.setter
    def y(self, value):
        """ Set the value of y"""
        if (type(value) is not int):
            raise TypeError("y must be an integer")
        
        if value < 0:
            raise ValueError("y must be >= 0")
        
        self.__y = value

    def area(self):
        """Defines the area value of the Rectangle"""
        return (self.__width * self.__height)
    
    def display(self):
        """Display the Rectangle with the character #"""
        for row in range(self.__height):
            for x in range(self.x):
                print(" ", end="")
            for column in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Defines a format for the string representation of the class"""
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}")
    


    