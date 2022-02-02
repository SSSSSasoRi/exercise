class Animal:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def run(self):
        print(f"{self.name} is running.")

    def bark(self):
        print(f"{self.name} is barking.")


class Dog(Animal):
    def __init__(self, name, age, weight):
        super(Dog, self).__init__(name, age, weight)

    def bark(self):
        print(f"{self.name}: Wang!")

    def print_age(self):
        print(self.age)


# dog1 = Dog("wang cai", 2)
# dog1.print_age()


class Cat(Animal):
    def __init__(self, name, age, weight):
        super(Cat, self).__init__(name, age, weight)

    def print_name(self):
        print(self.name)

    def calculate_food(self):
        result = self.weight / self.age
        return result

    def diet(self):
        self.weight -= 1

    def bark(self):
        print(f"{self.name}: Miao!")


# cat1 = Cat("mimi", 2, 5)
# print(cat1.weight)
# cat1.diet()
# print(cat1.weight)
# cat1.diet()
# print(cat1.weight)


def weight_check(cats, th):
    for c in cats:
        if c.weight > th:
            print(f"{c.name} is overweight.")


# cats = [
#     Cat("aaa", 10, 10),
#     Cat("bbb", 2, 2),
#     Cat("ccc", 5, 6),
#     Cat("ddd", 4, 3),
#     Cat("eee", 6, 5),
#     Cat("fff", 1, 2)
# ]
# th = 5
#
# weight_check(cats, th)

dog2 = Dog("wangcai", 3, 4)
cat2 = Cat("paofu", 2, 3)
dog2.bark()
cat2.bark()
