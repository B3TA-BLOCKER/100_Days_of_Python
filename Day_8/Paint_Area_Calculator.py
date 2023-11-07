import math

# Defining a function called paint_calc() so the code below works.
def paint_calc(height, width, cover):
  number_of_can = (height*width)/cover
  final_result = math.ceil(number_of_can)
  print(f"You'll need {final_result} cans of paint.")


test_h = int(input("The Height of the wall : ")) # Height of wall (m)
test_w = int(input("The Width of the Wall : ")) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
