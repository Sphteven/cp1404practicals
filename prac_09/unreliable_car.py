"""
CP1404/CP5632 Practical
Car class
"""

from prac_09.car import Car
import random


class UnreliableCar(Car):
    """Specialised version of a car that includes a reliability attribute."""

    def __init__(self, name, fuel, reliability):
        """Initialise an Unreliable Car instance, based on parent class Car"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive like parent Car but will check to see if the car is reliable through a random num check."""
        start_value = random.randint(0, 100)  # gives a random int to check if car drives
        if start_value < self.reliability:
            distance_driven = super().drive(distance)
            return distance_driven

