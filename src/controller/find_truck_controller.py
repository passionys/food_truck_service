from model.food_truck_model import FoodTruckModel
import heapq

from view.view import View


class FindTruckController:
    """
    FindTruckController:
    find the K closest trucks from (latitude, longitude) given by user

    """

    def __init__(self, model, view: View, logger):
        self.model = model
        self.view = view
        self.logger = logger

    def find_trucks(self, latitude, longitude, num_trucks) -> None:
        self.logger.info(f"Finding {num_trucks} closest trucks from ({latitude}, {longitude})")
        closest = FindTruckController.closest_trucks_heap(self.model.trucks, latitude, longitude, num_trucks)
        self.logger.info(f"{num_trucks} closest trucks: {closest}")
        self.view.show_result(closest)

    @staticmethod
    def closest_trucks_heap(trucks, latitude, longitude, num_trucks) -> list:
        """
        getting num_trucks closest trucks using max heap approach
        """
        closest = []
        for idx, truck in enumerate(trucks):
            distance = (float(truck["Latitude"]) - latitude) ** 2 + (float(truck["Longitude"]) - longitude) ** 2
            heapq.heappush(closest, (-distance, idx))
            if len(closest) > num_trucks:
                heapq.heappop(closest)

        return [trucks[idx] for _, idx in closest]
