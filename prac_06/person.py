class Person:
    """Represents a person object."""
    def __init__(self, first_name, last_name, age):
        """Initialise a person instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.first_name} {self.last_name}, age={self.age}"