import argparse
from configparser import ConfigParser

from service.find_truck_service import FindTruckService
from utils.logger_factory import LoggerFactory
from model.food_truck_model import FoodTruckModel
from view.cli_view import CliView

CONFIG_FILE = "config/food_trucks.conf"


def find_food_trucks(latitude, longitude):
    config_parser = ConfigParser()
    config_parser.read(CONFIG_FILE)

    food_truck_configs = dict(config_parser.items('food_trucks'))
    logger = LoggerFactory(CONFIG_FILE).get_logger()

    food_truck_service = FindTruckService(FoodTruckModel(food_truck_configs["csv_file"], logger), CliView(), logger)
    food_truck_service.find_trucks(float(latitude), float(longitude), int(food_truck_configs["number_closest_trucks"]))


def main():
    parser = argparse.ArgumentParser(prog='find_food_trucks',
                                     description="Find Food Trucks")
    parser.add_argument('-latitude', required=True)
    parser.add_argument('-longitude', required=True)
    args = parser.parse_args()

    find_food_trucks(args.latitude, args.longitude)


if __name__ == "__main__":
    main()
