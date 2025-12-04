def add_numbers(a, b):
    result = a + b      # unused variable: result
    return a + b        


def greet (name):   # space before parentheses ❌
      print("Hello " + name)  # wrong indentation ❌


def calculate_area(radius): 
    pi = 3.141592653589793238462643383279502884197  # line too long ❌
    area=pi*radius*radius  # missing spaces around '=' ❌
    return area  
