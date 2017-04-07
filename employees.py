# Create a class that contains information about employees of a company and define methods to get/set employee name, job title, and start date.

class Employee:

    ''' employee working for company '''

    def __init__(self, name, title, start_date):
         self.name = name
         self.title = title
         self.start_date = start_date

    def get_name(self):
         ''' returns name of employee '''
         return self.name

    def set_name(self, name):
         self.name = name  

    def get_title(self):
         ''' returns title of employee '''
         return self.title

    def set_title(self, title):
         self.title = title  

    def get_start_date(self):
         ''' returns start date of employee '''
         return self.get_start_date  

    def set_start_date(self, start_date):
    
         self.start_date =  start_date   

# Add the remaining methods to fill the requirements above
    
class Company:

    ''' company in which employees work '''

    def __init__(self, name, title, start_date):
         self.name = name
         self.start_date = start_date
         self.employees = set()

    def get_name(self):
    
         ''' returns the name of the company '''
        
         return self.name


# create company
NashvilleSoftwareSchool = Company('NashvilleSoftwareSchool', 'NSS Inc', '2010')

# create employees
steve = Employee('Steve', 'Head Coach', 'January 2015')
gilbert = Employee('Gilbert', 'Instructor', 'January 2017')
meg = Employee('Meg', 'Jr. Instructor', 'January 2017')
  
# assign the employees to the company.
NashvilleSoftwareSchool.employees.add(steve)
NashvilleSoftwareSchool.employees.add(gilbert)
NashvilleSoftwareSchool.employees.add(meg)

