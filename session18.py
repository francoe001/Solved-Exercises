# -*- coding: utf-8 -*-

#Exercise 1
#Create a Polyhedron class, and two classes Triangle and Circle that inherit from it.
#Make Triangle and Circle have an area method that return their respective areas

import math

class Polygon:
    
    def area(self):
        pass
    
class Triangle(Polygon):
    
    def __init__(self, base, height):
        
        self.base = base
        self.height = height
    
    def area(self):
        return self.base * self.height / 2
        
        
class Circle(Polygon):
    
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return math.pi * self.radius ** 2
    

shapes = [
        Circle(2),
        Triangle(2,3),
        Circle(4)
        ]

for shape in shapes:
    print(shape.area())



#%%


#Exercise 1
#Change your ecommerce example so:
#You create a class Product from which the classes Item and Service will inherit
    
class Product:
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
   
class Item(Product):
    pass
           
class Service(Product):
    pass
    

class Tier:
    
    def __init__(self, name):
        self.name = name
        
    def discount(self, item):
        """
        returns the price...
        """
        if self.name == "gold":
            return 0.95 * item.price
        elif self.name == "silver":
            if isinstance(item, Item):
                return 0.98 * item.price
            else:
                return item.price
        else:
            return item.price
            
cart = [
        Item("guitar", 1000),
        Item("pick box", 5),
        Service("Insurance", 5),
        Service("Insurance", 5)
        ]

normal_tier = Tier("normal")
silver_tier = Tier("silver")
gold_tier = Tier("gold")


def checkout(shopping_cart, tier=normal_tier): 
    if  shopping_cart == []:
        print("go back shopping!")
        return None
        
    total = 0
    
    services_in_cart = set()
    
    for item in shopping_cart:
        
        if isinstance(item, Service):
            if item.name in services_in_cart:
                continue            
            else:
                services_in_cart.add(item.name)
            
        total += tier.discount(item)
    
    return total















