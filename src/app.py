import argparse
from configparser import SafeConfigParser

from service.find_truck_service import FindTruckService
from utils.logger_factory import LoggerFactory
from pprint import pprint

CONFIG_FILE = "config/food_trucks.conf"


def find_food_trucks(args):
    latitude = args.latitude
    longitude = args.longitude
    filepath = args.filepath

    config_parser = SafeConfigParser()
    config_parser.read(CONFIG_FILE)

    food_truck_configs = dict(config_parser.items('log_config'))
    logger = LoggerFactory(CONFIG_FILE).get_logger()
    food_truck_service = FindTruckService(latitude, longitude, food_truck_configs["number_closest_trucks"], logger)
    closest_trucks = food_truck_service.find_trucks(food_truck_configs["csv_file"])

    return closest_trucks

def main():
    parser = argparse.ArgumentParser(prog='find_food_trucks',
                                     description="Find Food Trucks")
    parser.add_argument('-latitude',
                        required=True)
    parser.add_argument('-longitude',
                        required=True)

    args = parser.parse_arg()

    closest_trucks = find_food_trucks(args)
    pprint(closest_trucks)


if __name__ == "__main__":
    main()
