from PersonModule import Person

class Employee(Person): # inheriting from Person Class
    
    def __init__(self, name=None, age=16, employee_id=-1, salary=10000, job_position=None, hours_req=0): 
        if not (age >= 16): 
            raise ValueError("Invalid Age")
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary
        self.job_position = job_position
        self.hours = hours_req

    def setHours(self, hours_working): # setters
        if hours_working > 0:
            self.hours = hours_working
        else: 
            raise ValueError("Invalid hours")
    
    def getHours(self): # getters
        return self.hours
    
    def doWork(self, *args) -> None: # Overload
        if len(args) != 0:
            for ele in args: 
                if type(ele) == str:
                    print("Doing work with tool", ele)
                if type(ele) == int: 
                    print("Silly rabit trix are for kids", ele)
            return
        
        print("Doing Work")
        return
            

John = Employee("John", 28, 123, 10000, "CEO", 40)
Jai = Employee("Jai", 19, 1234, 10, "Janitor", 20)
Jai.doWork("Mop", 2, "Toolbox")



