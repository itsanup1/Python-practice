class Car:
    def __init__(self, brand:str, color:str, seats:int):
        self.brand = brand
        self.color = color
        self.seats = seats
        self.turned_on = False
    def reduce_it(self):
        self.seats = self.seats - 1
        return self.seats
        
    def turn_on(self):
        if self.turned_on:
            print(f'The {self.brand} is already turned on')
        else:
            self.turned_on = True
            print(f'The {self.brand} is now turned on')  
   
    def turn_off(self):
        if not self.turned_on:
            print(f'The {self.brand} is already turned off')
        else:
            self.turned_on = False
            print(f'The {self.brand} is now turned off')  
     
    def __str__(self):
         return f'\nCar(brand: {self.brand}, color: {self.color}, seats: {self.seats})'
                      
                                
car1 = Car("Tata","Black",7)   
car2 = Car("BMW", "White", 4)
 
print(car1)
print(car1.brand)
print(car1.seats)
print(car1.color)

print()
print(car2)
print(car2.brand)
print(car2.seats)
print(car2.color)

print(car1.reduce_it())
print()

car1.turn_on()
car1.turn_on()
car1.turn_off()
car1.turn_on()

print()
print(car2)
print(car1)