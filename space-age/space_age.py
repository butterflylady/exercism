class SpaceAge:
    def __init__(self, seconds):
        self.seconds=seconds
        self.earth_year=31557600
        self.mercury_period=0.2408467
        self.venus_period = 0.61519726
        self.mars_period = 1.8808158
        self.jupiter_period = 11.862615
        self.saturn_period = 29.447498
        self.uranus_period = 84.016846
        self.neptune_period = 164.79132

    def on_earth(self):
        return round(self.seconds/self.earth_year,2)

    def on_mercury(self):
        return round(self.seconds/(self.earth_year*self.mercury_period),2)

    def on_venus(self):
        return round(self.seconds / (self.earth_year * self.venus_period), 2)

    def on_mars(self):
        return round(self.seconds / (self.earth_year * self.mars_period), 2)

    def on_jupiter(self):
        return round(self.seconds / (self.earth_year * self.jupiter_period), 2)

    def on_saturn(self):
        return round(self.seconds / (self.earth_year * self.saturn_period), 2)

    def on_uranus(self):
        return round(self.seconds / (self.earth_year * self.uranus_period), 2)

    def on_neptune(self):
        return round(self.seconds / (self.earth_year * self.neptune_period), 2)