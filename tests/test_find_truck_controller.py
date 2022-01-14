import unittest
from controller.find_truck_controller import FindTruckController


class FindTruckControllerTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.trucks = [{'locationid': 7, 'Latitude': '7.0', 'Longitude': '3'},
                       {'locationid': 6, 'Latitude': '6.0', 'Longitude': '3'},
                       {'locationid': 1, 'Latitude': '1.0', 'Longitude': '3.0'},
                       {'locationid': 2, 'Latitude': '2.0', 'Longitude': '3'},
                       {'locationid': 3, 'Latitude': '3.0', 'Longitude': '3'},
                       {'locationid': 4, 'Latitude': '4.0', 'Longitude': '3'},
                       {'locationid': 5, 'Latitude': '5.0', 'Longitude': '3'},
                       ]

    def test_get_closest(self):
        find_truck_service = FindTruckController(None, None, None)
        closest = FindTruckController.get_closest_by_heap(self.trucks, 0, 0, 3)
        locations = [truck.get('locationid') for truck in closest]
        self.assertTrue(1 in locations and 2 in locations and 3 in locations)


if __name__ == '__main__':
    unittest.main()
