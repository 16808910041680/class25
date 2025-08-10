class fruit:
    def __init__(self, name):
        self.name = name
        print (name + " created.")

    def __del__(self):
        print("destructor called.")
        print (self.name + " destroyed.")
    def create_fruit(self, name):
        return fruit(name)
fruit1 = fruit("Apple")
fruit2 = fruit1.create_fruit("Banana")
