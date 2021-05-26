
def biographies():
    """Asks and returns name and age"""
    name = input("Name: ")
    age = ""
    while True:
        age = input("Age: ")
        try:
            age = int(age)
            age = str(age)
            break
        except:
            print("Invalid input. \nTry to write it in numerical form.")

    return name, age