class pair_element: 
    def __init__ (self, dict1, dict2):
        self.dict1 = dict1
        self.dict2 = dict2
        dict1 = {10,20,30,40,50,60,70}
        dict2 = {30,40,50,60,70,80,90}
        print("Pair element created with two dictionaries.")
    def pair_elements(self):
        if self.dict1 == self.dict2:
            print("The dictionaries are equal.")
        else:
            print("The dictionaries are not equal.")
    def sum_elements(self):
        sum1 = sum(self.dict1)
        sum2 = sum(self.dict2)
        print("Sum of elements in dict1:", sum1)
        print("Sum of elements in dict2:", sum2)
element1 = pair_element({10,20,30,40,50,60,70}, {30,40,50,60,70,80,90})
pair_element.pair_elements(element1)
pair_element.sum_elements(element1)



