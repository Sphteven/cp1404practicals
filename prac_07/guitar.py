"""
Guitar

Estimate: 30 minutes
Actual: 25 minutes

5:06
"""


class Guitar:
    """Represent a guitar object. """

    def __init__(self, name="", year=0, cost=0):
        """Initialise a programming language instance.
            name: string, Name of the guitar
            year: int, The year the guitar was made
            cost: float, The cost of the guitar.
        """
        self.name = name.title()
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the guitar object."""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def __lt__(self, other):
        return self.year < other.year

    def get_age(self):
        """Calculate the age of the guitar."""
        return 2025 - self.year

    def is_vintage(self):
        """Determines if guitar is a vintage if it's more than 50 years old"""
        if self.get_age() > 50:
            return True
        return False
