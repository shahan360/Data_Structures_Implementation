class Cookie: # This is a class to represent a cookie
    def __init__(self, color): # This is the constructor to initialize the object
        self.color = color

    def get_color(self): # This is a method to get the color of the cookie
        return self.color

    def set_color(self, color): # This is a method to set the color of the cookie
        self.color = color     


cookie_one = Cookie("red") # Creating an instance of the Cookie class
print(cookie_one.color) # Calling the color attribute of the instance
cookie_two = Cookie("blue")
print(cookie_two.color)
cookie_three = Cookie("green")
print(cookie_three.color)

print(cookie_one.get_color()) # Calling the get_color method of the instance
print(cookie_two.get_color())
print(cookie_three.get_color())

print(cookie_one.set_color("yellow")) # Calling the set_color method of the instance
print(cookie_one.get_color()) # Calling the get_color method of the instance