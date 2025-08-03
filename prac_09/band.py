class Band:
    def __init__(self, band_name):
        """Initialise a Band instance"""
        self.band_name = band_name
        self.band_musicians = []

    def __str__(self):
        """Return a string representation of the Band"""
        print(self.band_name)
        musicians_str = []
        for musician in self.band_musicians:
            musicians_str.append(str(musician))
        musicians_converted = ", ".join(musicians_str)
        return f"{self.band_name} ({musicians_converted})"

    def add(self, new_musician):
        """Add a new musician to the Band"""
        self.band_musicians.append(new_musician)

    def play(self):
        """Will call musician.play() to show what instrument each musician plays"""
        for musician in self.band_musicians:
            print(musician.play())
