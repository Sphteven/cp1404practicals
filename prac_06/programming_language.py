"""
Programming_languages

Estimate: 30 minutes
Actual:    minutes

"""


class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        self.name = name.title()
        self.typing = typing.title()
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.typing == 'Dynamic'

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
