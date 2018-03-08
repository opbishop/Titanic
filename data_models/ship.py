class Ship:
    def __init__(self, name, passengers):
        self.name = name
        self.passengers = passengers

    def to_string(self):
        print(self.name)
        for x in self.passengers:
            print(self.passengers.index(x))
            for passenger in x:
                passenger.to_string()
