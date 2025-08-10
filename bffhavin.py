class Randomclass:
    def __init__(self):
        self.string = "Hello, World!"
        print(self.string)
    def change_string(self, new_string):
        self.string = new_string
    def __str__(self):
        return self.string
    def uppercase(self):
        stuff.uppercase_string = lambda: stuff.string.upper()
        print(stuff.uppercase_string())
stuff = Randomclass()
stuff.change_string("Goodbye, World!")
print(stuff.string)
stuff.uppercase()
#This is a random comment


