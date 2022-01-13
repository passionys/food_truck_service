import csv


class FoodTruckData:
    def __init__(self, logger):
        self.trucks = []
        self.logger = logger

    def load_csv(self, filepath):
        try:
            with open(filepath, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    self.trucks.append(row)
        except IOError as e:
            print(f"File {filepath} not found!")
            self.logger.debug(f'Cannot open the file {filepath} : {e}')

        return self.trucks

