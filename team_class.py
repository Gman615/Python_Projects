class Team:
    def __init__(self, location, mascot, colors, sport):
        self.location=location
        self.mascot=mascot
        self.colors=colors
        self.sport=sport

car_pan = Team("Carolina", "Panthers", "Black, Light Blue, and Silver", "NFL")
print(car_pan.colors)
print(car_pan.mascot)
