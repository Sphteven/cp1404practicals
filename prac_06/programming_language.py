"""
Programming_languages

Estimate: 30 minutes
Actual: 25 minutes

"""


class ProgrammingLanguage:
    """Represent a programming language object."""
    def __init__(self, name, typing, reflection, year):
        """Initialise a programming language instance.
        name: string, The name of the programming language.
        typing: string, Programming language type.
        reflection: boolean, Programming language is reflection or not.
        year: integer, The year of the programming language was released.
        """
        self.name = name.title()
        self.typing = typing.title()
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine if a programming language is dynamic."""
        return self.typing == 'Dynamic'

    def __str__(self):
        """Provide object details in a neat format."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
