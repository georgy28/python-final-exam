class IceCreamMachine:

    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings

    def scoops(self):
        # YOUR CODE GOES HERE
        output = []
        for ingredient in self.ingredients:
            for topping in self.toppings:
                output.append([ingredient,topping])
        return output
        

machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
print(machine.scoops())
#should print
# [['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]
machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce","orange"])
print(machine.scoops())
# this should print
#[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce'], ['vanilla','orange'], ['chocolate','orange']]
machine = IceCreamMachine(["vanilla", "chocolate"], [])
print(machine.scoops())

machine = IceCreamMachine([], ["chocolate sauce","orange"])
print(machine.scoops())
# the last 2 should print an empty list