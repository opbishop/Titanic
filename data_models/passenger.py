class Passenger:
    def __init__(self, last_name, first_name, age, boarded, survived):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age
        self.boarded = boarded
        self.survived = survived
        self.gender = None

    def to_string(self):
        print(self.first_name + self.last_name)

    def get_values(self):
        return[self.last_name, self.first_name, self.age, self.boarded, self.survived, self.gender]