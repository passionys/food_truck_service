import csv


class FoodTruckData:
    def __init__(self, logger):
        self.trucks = []
        self.logger = logger

    def load_CSV(self, filepath):
        data = []
        with open(filepath, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
        return data

    @property
    def trucks(self):
        return self.trucks

    @trucks.setter
    def trucks(self, value):
        self._trucks = value


if __name__ == '__main__':
    foodTruckData = FoodTruckData(None)
    foodTruckData.load_CSV("/Users/youngshinkim/PycharmProjects/take-home-engineering-challenge/resources/Mobile_Food_Facility_Permit.csv")
