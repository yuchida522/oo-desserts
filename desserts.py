"""Dessert classes."""


class Cupcake:
    """A cupcake."""

    cache = {}

    def __repr__(self):
        """Human-readable printout for debugging."""
        #cache[key] = value
        return f'<Cupcake name="{self.name}" qty={self.qty}>'

    def __init__ (self, name, flavor, price):
        
        self.name = name
        self.flavor = flavor
        self.price = price
        self.qty = 0
        
        self.cache[name] = self

    def add_stock(self, amount):
        #cupcake.add_stock(5)
        self.qty += amount
        
    def sell(self, amount):
        
        if self.qty == 0:
            print("Sorry, these cupcakes are sold out")
            return
        if self.qty < amount:
            self.qty = 0
            return
        self.qty -= amount    

            
    @staticmethod
    def scale_recipe(ingredients, amount):
        
        new_ingredients = []
        
        for ingredient, qty in ingredients:
            new_amount = (ingredient, qty * amount)
            new_ingredients.append(new_amount)
            
        return new_ingredients

    @classmethod
    def get(cls, name):
        if name in cls.cache:
            return cls.cache[name]
        else:
            print("Sorry, that cupcake doesn't exist")

class Brownie(Cupcake):

    def __init__(self, name, price):
        self.name = name
        self.flavor = 'chocolate'
        self.price = price

if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
