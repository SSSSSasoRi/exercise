def bmi(height, weight):
    result = weight / height ** 2
    return result


height = float(input("height:"))
weight = float(input("weight:"))

my_bmi = bmi(height, weight)

print(my_bmi)
