from pprint import pprint


class CliView:
    def __init__(self, logger):
        self.logger = logger

    def show_result(self, trucks):
        pprint(trucks)
