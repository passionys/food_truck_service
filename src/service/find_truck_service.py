from model.food_truck_data import FoodTruckData
import heapq


class FindTruckService:
    """
    FindTruckService:
    1. load CSV data of trucks
    2. find the closes trucks from (latitude, logitude) given by user

    """

    def __init__(self, latitude, longitude, num_trucks, logger):
        self.latitude = latitude
        self.longitude = longitude
        self.num_trucks = num_trucks
        self.logger = logger
        self.truck_data = FoodTruckData(logger)

    def import_csv(self, filepath):
        # check if the file exist, and load CSV
        self.truck_data.load_CSV(filepath)
        return self.truck_data.trucks()

    def find_trucks(self, filepath):
        trucks = self.import_csv(filepath)
        self.logger.info(f"{trucks[0]}, {trucks[1]}")
        closest = self.get_closest(trucks)
        return closest

    def get_closest(self, trucks):
        closest = []
#        for truck in trucks:

        return trucks
