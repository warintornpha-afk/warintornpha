""" 
Create a class hierarchy:

    Base class Vehicle with attributes: brand, model, year
    Derived class Car with additional attribute: number_of_doors
    Implement a method get_info() in both classes

"""
<<<<<<< HEAD

class Vahicle:
     def __init__(self , brand, model, year):
          self.brand = brand
          self.model = model
          self.year = year

     def get__into(self):
          return f"Vehie=cle into :\nBrand:{self.brand}, model:{self.model}, Year:{self.year} "
          


class Car(Vahicle):
     def __init__(self, brand, model, year, number_of_doors):
          super().__init__(brand, model, year)
          self.number-number_of_doors = number_of_doors
Vahicle = Vahicle("Toyota" , "Yaris" , "2025")
print(Vahiclea.get_into())

car =  car ("Honda","City"<"2020"< "5")
print(car.get_into())
=======
>>>>>>> upstream/main
