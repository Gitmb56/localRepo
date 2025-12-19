def bark(self):
    print("Bhow Bhow")
Dog = type(
    "Dog",                   # class name
    (),                      #parent classes
    {
        "legs":4,
        "bark":bark
    }
)

d = Dog()
print(d.legs)
d.bark()