#%%
#Exercise 1
#Modify your ecommerce example so, instead of returning None when two services of the same 
#type happen on checkout, raises an exception

class Product:
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
class Service:
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
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
            if isinstance(item, Product):
                return 0.98 * item.price
            else:
                return item.price
        else:
            return item.price
            
cart = [
        Product("guitar", 1000),
        Product("pick box", 5),
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
                raise Exception("You have already added the Service")            
            else:
                services_in_cart.add(item.name)
            
        total += tier.discount(item)
    
    return total






#%%

#Exercise 1
#Create a function that reads through a file and prints all the lines in uppercase.
#be sure to control exceptions that may occur here, such as the file not existing


def print_file_uppercase(filename):
    
    try:
        file = open(filename)
    
        for line in file:
            print(line.upper().strip())
    except Exception:
        print("file doesnt exist")
        
print_file_uppercase("data.txt")

#%%
#Exercise 3
#Create a function to copy files.
#The function must receive two names (origin and destination, for example), and copy 
#the contents of origin into destination.
#You'll need to investigate how to write files for this exercise

def copy_file(origin, destination):
    
    try:
        origin_file = open(origin)
        destination_file = open(destination, "w")
        
 #       if len(origin_file) == 0
         
        for line in origin_file:
            destination_file.write(line)
        
        destination_file.close()
    
    except Exception:
        print("something went wrong")
        
        







        