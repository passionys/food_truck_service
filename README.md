### **Food Truck Service project**

This is a CLI application implemented in python 3.8. 
It will have a location (Lattitude, Longitue) as parameters and return K(default 5) closest food trucks near it.

#### **How to run it**

From command line,  
 % python find_trucks_cli.py -latitude 100 -longitude -30  
[{'Address': '2201 VALLEJO ST',
  'Applicant': 'D & T Catering',
  'Approved': '07/11/2018 12:00:00 AM',
  'ExpirationDate': '07/15/2019 12:00:00 AM',
  'FacilityType': 'Truck',
  'FoodItems': 'Cold Truck: Pre-packaged sandwiches: Chicken Bake: Canned '
               'Soup: Chili Dog: Corn Dog: Cup of Noodles: Egg Muffins: '
               'Hamburgers: Cheeseburgers: Hot Dog: Hot sandwiches: '
               'quesadillas: Beverages: Flan: Fruits: Yogurt: Candy: Cookies: '
               'Chips: Donuts: Snacks',
  'Latitude': '0',
  'Location': '(0, 0)',   
...................

#### **Program structure**

src\
   ` `--config  : configuration files for logging and other constants  
   ` `--model  :  data models  
   ` `--service  : controllers doing business logic  
   ` `--utils  : utilities   
   ` `find_trucks_cli.py  
tests  : unit tests  
resources  : CSV file having Food Trucks data

#### **Data Model**

List was used to contain each truck's data, and dictionary was chosen to fast access O(1) to each field.
Truck class was one option but since there are many unused fields from CSV file, basic dictionary was chosen for simplicity.

#### **Algorithm used to select the closest trucks**

Each truck's distance to the user location is pushed to Max heap
Once the size of the heap grows more than the number specified from configuration file, 
if the new truck is closer than the top element of the heap, pop an element from the heap 
and push the new one. In this way, it will maintain top K closest trucks in the heap.

Time complexity : O(N log K)  N is the number of trucks and K could be 5 or any number.  
Space complexity : O(N)

Other approach : You can sort by distance and return the first K trucks. it will take O(NlogN) time.  
Considering N could be large compared to K, I chose Max Heap approach.

#### **Logging**
python builtin logging module was used with RotatingFileHandler which will rotate log files based on the max size.
LoggerFactory class was implemented using Singleton pattern to be threads safe.

#### **Todo items**
1. Data validation for CSV file
2. Displaying results more efficiently instead showing all the fields.  
   We can ask users to add the field names in the config file to show.  
3. How to deploy the application 