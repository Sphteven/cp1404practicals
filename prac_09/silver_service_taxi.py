from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of Tax that includes fanciness"""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi object based on parent class Taxi"""
        super().__init__(name, fuel)
        self.price_per_km = fanciness * super().price_per_km

    def __str__(self):
        """Return a string like a taxi but with the added fanciness"""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Return the price for the taxi trip as Parent but adds flagfall value """
        return (super().get_fare()) + self.flagfall

