from abc import ABC, abstractmethod


# interface for payment strategy
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: int) -> None:
        pass

    def collectPaymentDetails(self) -> None:
        pass

    def validatePaymentDetails(self) -> None:
        pass


# Payment by Credit Card
class CreditCard:
    def __init__(self, number, date, cvv):
        self.number = number
        self.date = date
        self.cvv = cvv


# Payment by PayPal
class Paypal:
    def __init__(self, email, password):
        self.email = email
        self.password = password


# Concrete strategy for payment by PayPal
class PaymentService:
    def __init__(self):
        self._cost = 0
        self._includeDelivery = False
        self._paymentStrategy = None

    # setter for payment strategy
    def paymentStrategy(self, strategy: PaymentStrategy):
        self._paymentStrategy = strategy
    
    def processOrder(self, cost):
        self._cost = cost
        self._paymentStrategy.collectPaymentDetails() 
        if self._paymentStrategy.validatePaymentDetails():
            self._paymentStrategy.pay(self.getTotal())
        else:
            print("Payment failed")

    def getTotal(self):
        return self._cost + 10 if self._includeDelivery else self._cost


# Concrete strategy for payment by credit card
class PaymentByCreditCard(PaymentStrategy):

    def __init__(self):
        self.card = None

    def collectPaymentDetails(self) -> None:
        self.card = CreditCard("cardNumber", "expiryDate", "cvv")
        print("Payment details collected")

    def pay(self, amount: int) -> None:
        print(f"Payment of {amount} by credit card")

    def validatePaymentDetails(self) -> None:
        print("Validating card information")
        return True
    

# Concrete strategy for payment by PayPal
class PaymentByPaypal(PaymentStrategy):

    def __init__(self):
        self.paypal = None

    def collectPaymentDetails(self) -> None:
        self.paypal = Paypal("email", "password")   
        print("Payment details collected")
    
    def pay(self, amount: int) -> None:
        print(f"Payment of {amount} by PayPal")
    
    def validatePaymentDetails(self) -> None:
        print("Validating PayPal information")
        return True
    
if __name__ == "__main__":
    paymentService = PaymentService()
    paymentService.paymentStrategy(PaymentByCreditCard())
    paymentService.processOrder(100)
    paymentService.paymentStrategy(PaymentByPaypal())
    paymentService.processOrder(200)