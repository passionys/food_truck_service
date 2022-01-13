import csv


class FoodTruckData:
    def __init__(self, logger):
        self.trucks = []
        self.logger = logger

    def load_csv(self, filepath):
        with open(filepath, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.trucks.append(row)

    @property
    def trucks(self):
        return self._trucks

    @trucks.setter
    def trucks(self, value):
        self._trucks = value
