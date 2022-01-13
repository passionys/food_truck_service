from model.food_truck_data import FoodTruckData
import heapq


class FindTruckService:
    """
    FindTruckService:
    1. load CSV data of trucks
    2. find the closes trucks from (latitude, logitude) given by user
       Max Heap approach is used.

    """

    def __init__(self, latitude, longitude, num_trucks, logger):
        self.latitude = latitude
        self.longitude = longitude
        self.num_trucks = num_trucks
        self.logger = logger
        self.truck_data = FoodTruckData(logger)

    def import_csv(self, filepath):
        # check if the file exist, and load CSV
        self.truck_data.load_csv(filepath)
        return self.truck_data.trucks

    def find_trucks(self, filepath):
        trucks = self.import_csv(filepath)
        self.logger.info(f"Finding {self.num_trucks} closest trucks from ({self.latitude}, {self.longitude})")
        closest = self.get_closest(trucks)
        self.logger.info(f"{self.num_trucks} closest trucks: {closest}")
        return closest

    def get_closest(self, trucks):
        closest = []
        for idx, truck in enumerate(trucks):
            distance = (float(truck["Latitude"]) - float(self.latitude))**2 + (float(truck["Longitude"]) - float(self.longitude))**2
            heapq.heappush(closest, (-distance, idx))
            if len(closest) > self.num_trucks :
                heapq.heappop(closest)

        return [trucks[idx] for _, idx in closest]
