0x06. Python - Classes and Objects

Initialization:

The class Square is defined to represent a square.
It takes two optional parameters: size (the size of the square) and position (the position where the square will be printed).
Size Property:

The size property allows you to get and set the private attribute __size.
When setting the size, it checks if the provided value is an integer and if it's greater than or equal to 0. Otherwise, it raises appropriate errors.
This ensures that the size of the square is valid.
Position Property:

The position property allows you to get and set the private attribute __position.
When setting the position, it checks if the provided value is a tuple of two positive integers. If not, it raises an error.
This ensures that the position is valid and well-formatted.
Initialization Continued:

The __init__ method initializes the size and position attributes based on the provided parameters.
It uses the property setters to validate and set the attributes.
Area Method:

The area method calculates and returns the area of the square by squaring the value of the __size attribute.
This method provides the current area of the square.
Print Method:

The my_print method prints the square pattern using the "#" character.
If the __size attribute is 0, it prints an empty line.
If the __size is not 0, it considers the __position attribute for printing:
It prints empty lines equal to the vertical position (value at __position[1]).
It then prints lines of "#" characters, adjusted by the horizontal position (value at __position[0]).
Private Attributes:

Throughout the class, private attributes are denoted using a double underscore prefix (e.g., __size, __position).
This naming convention indicates that these attributes are not meant to be accessed directly from outside the class.
By following these steps, the Square class provides a way to create square objects with specified sizes and positions, calculate their areas, and print their patterns while accounting for the given position.
