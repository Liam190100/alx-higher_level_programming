#!/usr/bin/python3

from models.base import Base


class Rectangle(Base):
    """Rectangle class, inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the Rectangle instance"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width of the rectangle"""
        return self.__width

    @property
    def height(self):
        """Get the height of the rectangle"""
        return self.__height

    @property
    def x(self):
        """Get the x-coordinate of the rectangle"""
        return self.__x

    @property
    def y(self):
        """Get the y-coordinate of the rectangle"""
        return self.__y

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Set the x-coordinate of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Set the y-coordinate of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Display the rectangle using '#' characters"""
        print("\n" * self.__y + "\n".join((" " * self.__x + "#" * self.__width)
            for _ in range(self.__height)))

    def __str__(self):
        """String representation of the rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Update attributes of the rectangle"""
        if kwargs:
            self.id = kwargs.get('id', self.id)
            self.width = kwargs.get('width', self.width)
            self.height = kwargs.get('height', self.height)
            self.x = kwargs.get('x', self.x)
            self.y = kwargs.get('y', self.y)
        elif args:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])

    def to_dictionary(self):
        """Return a dictionary representation of the rectangle"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
