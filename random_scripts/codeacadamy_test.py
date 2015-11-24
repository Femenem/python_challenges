def cube(number):
    newNumber = number ** number
    print(newNumber)
    return newNumber
def by_three(number):
    if number % 3 == 0:
        cube(number)
    else:
        return False
