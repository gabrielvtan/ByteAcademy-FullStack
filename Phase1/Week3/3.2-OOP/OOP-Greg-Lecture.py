
class Person:
    """This is a person"""
    mammal = True
#This is true for every instance of Person class

    def __init__(self, height, weight, __age=0):
#These are only applicable to individuals, with age usually
#starting at 0 unless we pass in a different age
        self.age = __age
        self.height = height
        self.weight = weight

    def birthday(self,__age=1):
        self.age = self.age+__age

    def grow(self, inches):
        self.height += inches

Greg = Person(70, 140)
#Greg is 0 years old

Greg = Person(70, 140, 26)
#Now Greg is 26

new_age = Greg.birthday()
# Sets Greg.age = 1
# Would need to make this function
# return a value to assign to new_age