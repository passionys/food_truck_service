from pprint import pprint
from view.view import View


class CliView(View):
    """
    CliView : simple command line interface view
    """
    def __init__(self, logger):
        self.logger = logger

    def show_result(self, trucks):
        pprint(trucks)
