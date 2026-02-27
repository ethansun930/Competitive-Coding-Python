a = {"a": 5, "b": 10, }

class Person:
    def __init__(self, height: int, weight: int, hair_color: str, metadata: str):
        self.height = height
        self.weight = weight
        self.hair_color = hair_color
        self.METADATA = metadata
        
    def bmi(self):
        if self.weight == 0:
            return 0
        return self.height / self.weight
        
person_a = Person(3, 5, "blue")


print(person_a.bmi())

class Table:
    def __init__(self, length: )


# obj_b = Person(5, 7, "black")

# print(person_b.bmi())

# class :
#     def __init__(self, height: int, weight: int, hair_color: str):
#         self.height = height
#         self.weight = weight
#         self.hair_color = hair_color
        
# obj_a = Person(3, 5, "blue")

# obj_b = Person(5, 7, "black")