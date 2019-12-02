
def  overseerSystem(**kwargs):
    for k,v in kwargs.items():
        if k == 'temperature':
            temp = kwargs.get('temperature')
            if temp > 500:
                print('Warning: temperature is', temp)
        elif k == 'CO2level':
            co2 = kwargs.get('CO2level')
            if co2 > 0.15:
                print('Warning: CO2level is', co2)
        elif k == 'miscError':
            print ('Misc error #' + str(v))
        else:
            pass       
               

def main():
    Message1 = {'temperature': 550}
    Message2 = {'temperature': 475}
    Message3 = {'temperature':450, 'miscError': 404}
    Message4 = {'CO2level': 0.18}
    Message5 = {'CO2level': 0.2, 'miscError': 418}
    overseerSystem(**Message1)
    overseerSystem(**Message2)
    overseerSystem(**Message3)
    overseerSystem(**Message4)
    overseerSystem(**Message5)
if __name__=='__main__':
    main() 


class BritCoins:
    
    __coinValues = {"pound":240, "shilling":12, "penny":1}
    
    def __init__(self,**kwargs):
        self.totalPennies = 0
        for k,v in kwargs.items():
            if k == 'pound':
                self.totalPennies += self.__coinValues.get('pound')*v
            elif k == 'shilling':
                self.totalPennies += self.__coinValues.get('shilling')*v
            else:
                self.totalPennies += self.__coinValues.get('penny')*v

    def __add__(self, other):

        return BritCoins(**{'penny': self.totalPennies + other.totalPennies})

        
    def __sub__(self, other):
        return BritCoins(**{'penny': self.totalPennies - other.totalPennies}) 
        
    def __str__(self):
        self.calPennies =self.totalPennies
        po = self.calPennies // 240
        sh = (self.calPennies - po*240) // 12
        pe = self.calPennies - po*240 - sh*12
        return str(po)+' pounds '+str(sh)+' shillings '+str(pe)+' pennies'
        
c1 = BritCoins(pound = 4, shilling = 24, penny = 3)
print(str(c1))
c2 = BritCoins(pound = 3, shilling = 4, penny = 5)
print(str(c2))
c3 = c1 + c2
print(str(c3))
c4 = c1 - c2
print(str(c4))
