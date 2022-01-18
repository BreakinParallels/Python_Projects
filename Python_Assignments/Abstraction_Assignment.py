


from abc import ABC, abstractmethod
class tv(ABC):
    def creditLimit(self, amount):
        print("Your credit card purchase is: ",amount)
#this function is telling us to pass in an agrument,
#but we won't tell you how or what kind
#of data it will be.
    @abstractmethod
    def payment(self, amount):
        pass


class CreditCardPayment(tv):
#here we've defined how to implement the payment function
#from its parent paySlip class.
    def payment(self, amount):
        print('Your purchase amount of {} exceeded your $1000 limit '.format(amount))


obj = CreditCardPayment()
obj.creditLimit("$3000")
obj.payment("$2000")


    
