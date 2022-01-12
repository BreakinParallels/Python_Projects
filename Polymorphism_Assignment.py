


#Parent Class User
class User:
    name = "Shannon"
    email = "shannon@gmail.com"
    password = "7890shh"

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The password or email is incorrect.")


#Child Class Employee
class FTEmployee(User):
    employee_name = "Mark Jones"
    department_number = "PE401"
    pin_number = "3980"

    def getLoginInfo(self):
        entry_employee_name = input("Enter your name: ")
        entry_department_number = input("Enter your Department Number: ")
        entry_pin_number = input("Enter your pin: ")
        if (entry_employee_name == self.employee_name and entry_department_number == self.department_number and entry_pin_number == self.pin_number):
            print("Welcome back, {}!".format(self.employee_name))
        else:
            print("Your Department Number or pin is incorrect.  Please re-enter.")

class Customer(User):
    customer_email = "Jane@hotmail.com"
    member_id = "444333"
    

#This is the same method in the parent class "User".
#The difference is that, instead of using entry_password, we're using entry_pin.

    def getLoginInfo(self):
        entry_customer_email = input("Enter your email: ")
        entry_member_id = input("Enter your Member ID: ")
        if (entry_customer_email == self.customer_email and entry_member_id == self.member_id):
            print("Welcome back, Member {}!".format(self.member_id))
        else:
            print("Your Email or Member ID is incorrect.")

#The following code invokes the methods inside each class for User and Employee.

customer = User()
customer.getLoginInfo()

employee = FTEmployee()
employee.getLoginInfo()

member = Customer()
member.getLoginInfo()
