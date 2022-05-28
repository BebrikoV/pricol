class Client:
    def __init__(self,name,balans,Creditbalans,passport):
        self.__name = name
        self.__balansOwnFunds = balans
        self.__balansCreditFunds = Creditbalans
        self.__passport = passport
    def balansOwnFunds(self, money):
        self.balansOwnFunds =+ money
    def balansCreditFunds(self, money):
        self.balansCreditFunds =+ money
    #def printProtectedData(self):
     #   print(self._name,self._balansOwnFunds,self._balansCreditFunds,self._passport)
    def __printPrivateData(self):
        print(self.__name,self.__balansOwnFunds,self.__balansCreditFunds,self.__passport)
account1 = Client("Bebra",1000,300,674560)
account1._Client__printPrivateData()
# account1.printProtectedData()
# print(account1.__name)
# print(account1.__balansOwnFunds)
# print(account1.__balansCreditFunds)
# print(account1.__passport)
