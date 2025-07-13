"""
Programming_languages

Estimate: 30 minutes
Actual:    minutes

"""


class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing.lower()
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.typing == 'dynamic'

