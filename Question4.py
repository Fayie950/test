# Dog class
class Dog:
    def make_sound(self):
        return "Woof!"

# Cat class
class Cat:
    def make_sound(self):
        return "Meow!"

# Function using polymorphism
def process_sound(sound_object):
    return sound_object.make_sound()

# Testing the function
dog = Dog()
cat = Cat()

print(process_sound(dog))  # Output: Woof!
print(process_sound(cat))  # Output: Meow!