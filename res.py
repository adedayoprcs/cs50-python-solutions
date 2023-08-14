class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.age = cuisine_type


    def status(self):
   
        print(f"{self.name} is now open")

class Restaurant:
   

    first_restaurant = Restaurant('Dominos', 'Chinese cuisine')
    second_restaurant = Restaurant('Enish', 'African cuisine')

    first_restaurant.status()
    second_restaurant.status()

