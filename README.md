### **Food Truck Service project**

This is a CLI application implemented in python 3.8. 
It will have a location (Lattitude, Longitue) as parameters and return 5 closest food trucks near it.

###### **How to run it**

From command line,  
 % python find_trucks_cli.py -latitude 100 -longitude -30

###### **Program structure**

src\
   ` `--config  : configuration files for logging and data file  
   ` `--model  :  data models  
   ` `--service  : controllers doing business logic  
   ` `--utils  : utilities   
   ` `find_trucks_cli.py  
tests

###### **Data Model**

List was used to contain each truck's data, and dictionary was chosen to fast access O(1) to each field.
Truck class was one option but since there are many unused fields from CSV file, basic dictionary was chosen for simplicity.

###### **Algorithm used to select the closest trucks**

Each truck's distance to the user location was pushed to Max heap
Once size of heap grows than 5, or the number specified from configuration file, 
if the new truck is closer than the top element of the heap, pop an element from the heap 
and push the new one.

Time complexity : O(N log K)  N is the number of trucks and K could be 5 or any number.
Space complexity : O(N)

###### **Logging**
python builtin logging module was used with RotatingFileHandler which will rotate log files based the size from configuration
LoggerFactory class was implemented in case that application was extended with other features.



