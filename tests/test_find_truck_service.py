import unittest
from service.find_truck_service import FindTruckService


class FindTruckServiceTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.trucks = [{'locationid': 1, 'Latitude': '1.0', 'Longitude': '3.0'},
                       {'locationid': 2, 'Latitude': '2.0', 'Longitude': '3'},
                       {'locationid': 3, 'Latitude': '3.0', 'Longitude': '3'},
                       {'locationid': 4, 'Latitude': '4.0', 'Longitude': '3'},
                       {'locationid': 5, 'Latitude': '5.0', 'Longitude': '3'},
                       {'locationid': 6, 'Latitude': '6.0', 'Longitude': '3'},
                       {'locationid': 7, 'Latitude': '7.0', 'Longitude': '3'}]

    def test_get_closest(self):
        find_truck_service = FindTruckService(0, 0, 3, None)
        closest = find_truck_service.get_closest(self.trucks)
        locations = [truck.get('locationid') for truck in closest]
        self.assertTrue(1 in locations and 2 in locations and 3 in locations)


if __name__ == '__main__':
    unittest.main()
