### **Food Truck Service project**

This is a CLI application implemented in python 3.8. 
It will have a location (Lattitude, Longitue) as parameters and return K(default 5) closest food trucks near it.

#### **How to run it**

From command line,  
(venv) (base) youngshinkim@youngshins-air src % python find_trucks_cli.py -latitude 37.782143532929 -longitude -122.430449785949
[{'Address': '368 ELM ST',
  'Applicant': 'Anas Goodies Catering',
  'Approved': '07/09/2018 12:00:00 AM',
  'ExpirationDate': '07/15/2019 12:00:00 AM',
  'FacilityType': 'Truck',
  'FoodItems': 'Cold Truck: Sandwiches: Noodles:  Pre-packaged Snacks: Candy: '
               'Desserts Various Beverages',
  'Latitude': '37.7813800275549',
  'Location': '(37.7813800275549, -122.423143845506)',
  'LocationDescription': 'ELM ST: FRANKLIN ST to GOUGH ST (300 - 399)',
...................

#### **Application Architecture**
MVC pattern  :   Model, View, and Controller were separated, and it would be easy to change View or Model in the future without touching controller.  
For example, you can replace CliView with TKView.  Model also can be easily replaced with DBModel.  
Controller <--> Model   
` `|-----> View


#### **Data Model**

List was used to contain each truck's data, and dictionary was chosen fast access to each field. It will take O(1) time.

Todo:
It would be better putting abstraction between models and the controller. 

#### **Algorithm used to select the closest trucks**

Each truck's distance to the user location is pushed to min heap with negative value. 
Once the size of the heap grows more than the number specified from configuration file, 
if the new truck is closer than the top element of the heap, pop an element from the heap 
and push the new one. In this way, it will maintain top K closest trucks in the heap.

Time complexity : O(N log K)  N is the number of trucks and K could be 5 or any number.  
Space complexity : O(N)

Other approach : You can sort by distance and return the first K trucks. it will take O(NlogN) time.  

if the given data set is not big enough ( N > 10000), these two approaches might not have much difference.

#### **Logging**
python builtin logging module was used with RotatingFileHandler which will rotate log files based on the max size.
log configuration came from config file. LoggerFactory implemented to provide one place to set up loggers. 

#### **Todo items**
1. Data validation for CSV file
2. Integration testing (end-to-end testing) for ensuring the new code change did not break the existing functionalities.
3. View can be enhanced to UI or WebUI and showing only selected fields which are useful to users
4. Deployment process (PyInstaller or container like Docker)
5. providing choice of algorithms to select food trucks through strategy pattern. 
6. Assuming the app will be deployed to PROD, I will use Logstash - Elasticsearch - Kibana for searching logs