import unittest
from textwrap import dedent
from unittest.mock import mock_open, patch

from model.food_truck_data import FoodTruckData


class FoodTruckDataTestCase(unittest.TestCase):
    DATA = """locationid,Applicant,FacilityType,cnn,LocationDescription,Address,blocklot,block,lot,permit,Status,FoodItems,X,Y,Latitude,Longitude,Schedule,dayshours,NOISent,Approved,Received,PriorPermit,ExpirationDate,Location
751253,Pipo's Grill,Truck,5688000,FOLSOM ST: 14TH ST to 15TH ST (1800 - 1899),1800 FOLSOM ST,3549083,3549,083,16MFF-0010,REQUESTED,Tacos: Burritos: Hot Dogs: and Hamburgers,6007856.719,2107724.046,37.7678524427181,-122.416104892532,http://bsm.sfdpw.org/PermitsTracker/reports/report.aspx?title=schedule&report=rptSchedule&params=permit=16MFF-0010&ExportPDF=1&Filename=16MFF-0010_schedule.pdf,,,,2016-02-04,0,,"(37.7678524427181, -122.416104892532)"
519938,Bob Johnson,Truck,0,,Assessors Block 0733/Lot010,0733010,0733,010,14MFF-0009,EXPIRED,Watermelon,6003818.547,2113011.835,37.782143532929,-122.430449785949,http://bsm.sfdpw.org/PermitsTracker/reports/report.aspx?title=schedule&report=rptSchedule&params=permit=14MFF-0009&ExportPDF=1&Filename=14MFF-0009_schedule.pdf,Mo-Su:10AM-7PM,,02/25/2014 12:00:00 AM,2014-02-25,1,03/15/2015 12:00:00 AM,"(37.782143532929, -122.430449785949)"
735318,Ziaurehman Amini,Push Cart,30727000,MARKET ST: DRUMM ST intersection,5 THE EMBARCADERO,0234017,0234,017,15MFF-0159,REQUESTED,,6013916.72,2117244.027,37.7943310032468,-122.395811053023,http://bsm.sfdpw.org/PermitsTracker/reports/report.aspx?title=schedule&report=rptSchedule&params=permit=15MFF-0159&ExportPDF=1&Filename=15MFF-0159_schedule.pdf,,,,2015-12-31,0,03/15/2016 12:00:00 AM,"(37.7943310032468, -122.395811053023)" """

    @patch("builtins.open", mock_open(read_data=DATA))
    def test_load_CSV(self):
        food_truck_data = FoodTruckData(None)
        trucks = food_truck_data.load_CSV("filepath")
        for truck in trucks:
            print(truck)
        self.assertEqual(len(trucks), 3)


if __name__ == '__main__':
    unittest.main()
