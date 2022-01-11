

# creating a parent class with attributes assigned to it
class User:
    name = 'No Name Provided'
    email = ' '
    password = '1234abcd'
    account_number = 0

# creation of two child classes that have their own attributes
# that don't overlap.
class Employee(User):
    base_pay = 11.00
    department = 'General'

class Customer(User):
    mailing_address = ' '
    mailing_list = True
