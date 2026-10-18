class animal:
    pass
class pets(animal):
    pass
class Dog (pets):
    
    @staticmethod
    def brak ():
        print(f"baw baw baw")

a = Dog()
a.brak()