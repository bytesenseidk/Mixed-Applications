class MyBMI(type):
    def __call__(cls, *args, **kwargs):
        height, weight = args
        print(f"With a height of {height}m. and weight {weight}kg.")
        print("Your Body Mass Index is: ")
        return type.__call__(cls, *args, **kwargs)


class BMI(metaclass=MyBMI):
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
    
    
    def formula(self):
        return round(self.weight / (self.height**2), 1)
        

    def __str__(self):
        return str(self.formula())


if __name__ == "__main__":
    print(BMI(1.78, 90))
    

