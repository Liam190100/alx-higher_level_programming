#!/usr/bin/python3

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class, inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the square instance"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of the square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """Get the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the square attributes"""
        if args:
            attrs = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                if attrs[i] == 'size':
                    setattr(self, 'width', arg)
                    setattr(self, 'height', arg)
                else:
                    setattr(self, attrs[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return a dictionary representation of the square"""
        attrs = ['id', 'size', 'x', 'y']
        return {key: getattr(self, key) for key in attrs}
