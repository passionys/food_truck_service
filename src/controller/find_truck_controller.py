from model.food_truck_model import FoodTruckModel
import heapq


class FindTruckController:
    """
    FindTruckService:
    find the K closest trucks from (latitude, longitude) given by user
    Max Heap approach was used.

    """

    def __init__(self, model, view, logger):
        self.model = model
        self.view = view
        self.logger = logger

    def find_trucks(self, latitude, longitude, num_trucks):
        self.logger.info(f"Finding {num_trucks} closest trucks from ({latitude}, {longitude})")
        closest = self.get_closest(self.model.trucks, latitude, longitude, num_trucks)
        self.logger.info(f"{num_trucks} closest trucks: {closest}")
        self.view.show_result(closest)

    def get_closest(self, trucks, latitude, longitude, num_trucks):
        closest = []
        for idx, truck in enumerate(trucks):
            distance = (float(truck["Latitude"]) - latitude)**2 + (float(truck["Longitude"]) - longitude)**2
            heapq.heappush(closest, (-distance, idx))
            if len(closest) > num_trucks :
                heapq.heappop(closest)

        return [trucks[idx] for _, idx in closest]
