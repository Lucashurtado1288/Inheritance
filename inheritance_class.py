# Employee Class (superclass)
class Employee:
    # Initialing attributes of Employee Class
    def __init__(self, name='', number=''):
        self.__name = name
        self.__number = number

    # Methods below are Mutators for the data attributes in Employee superclass
        # controlled way to modify private variables through methods
    def set_name(self, name):
        self.__name = name

    def set_number(self, number):
        self.__number = number

    # Methods below are the Accessors for the data attributes in Employee superclass
    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number





# ProductionWorker Class (subclass of Employee superclass)
class ProductionWorker(Employee):
    # Initializing first two values from Employee superclass and adding Shift and pay rate.
    def __init__(self, name="", number="", shift=1, pay_rate=0.0):      
        super().__init__(name, number)
        self.__shift = shift
        self.__pay_rate = pay_rate
    

    # Mutators
    def set_shift(self,shift):
        self.__shift = shift 

    def set_pay_rate(self,pay_rate):
        self.__pay_rate = pay_rate 

    # Accessors 
    def get_shift(self):
        return self.__shift 

    def get_pay_rate(self):
        return self.__pay_rate 



# Shift Supervisor Class (subclass of Employee superclass)
    # super().__init__(name, number) , newer way to reference the superclass
    # Employee.__init__(self, name, number) , would still work just have to use self each time
class ShiftSupervisor(Employee):
    # Initializing first two values from Employee superclass and adding Salary and bonus.
    def __init__(self, name="", number="", salary=0.0, bonus=0.0):
        super().__init__(name, number)
        self.__salary = salary
        self.__bonus = bonus

    # Methods below are Mutators for the data attributes in subclass ShiftSupervisor
    def set_salary(self, salary):
        self.__salary = salary

    def set_bonus(self, bonus):
        self.__bonus = bonus

    # Methods below are Accessors for the data attributes in subclass ShiftSupervisor
    def get_salary(self):
        return self.__salary

    def get_bonus(self):
        return self.__bonus











