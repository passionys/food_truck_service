import csv


class FoodTruckModel:
    """
    FoodTruckModel : Data model loaded from CSV file
    """
    def __init__(self, filepath, logger):
        self.trucks = []
        self.logger = logger
        self.load_csv(filepath)

    def load_csv(self, filepath):
        self.logger.info(f'load_csv: loading csv file for {filepath}')
        try:
            with open(filepath, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    self.trucks.append(row)
        except IOError as e:
            print(f"File {filepath} not found!")
            self.logger.debug(f'Cannot open the file {filepath} : {e}')

