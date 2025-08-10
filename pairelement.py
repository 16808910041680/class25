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
    def sum_elements_median(self):
        sum1 = sum(self.dict1)
        sum2 = sum(self.dict2)
        sum1 /= len(self.dict1)
        sum2 /= len(self.dict2)
        sum1 = sum1 + 30
        sum2 = sum2 + 30
        match1 = 0
        sum1 - self.dict1 == match1
        print (sum1, match1, "Matches up to the last element in dict1.")

element1 = pair_element({10,20,30,40,50,60,70}, {30,40,50,60,70,80,90})
pair_element.pair_elements(element1)
pair_element.sum_elements(element1)
pair_element.sum_elements_median(element1)





