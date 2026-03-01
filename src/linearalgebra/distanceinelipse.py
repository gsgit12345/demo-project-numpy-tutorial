import numpy as np

def finddistanceinellipse(point,a,b):

      x=point[0] #take the oth value in array
      y=point[1] #take ith value in array

      value=(x*x)/(a*a)+(y*y)/(b*b)

      if value <1:
            return "inside ellipse"
      
      elif value>1 :
         return "outside ellipse"
      else:
           return "on boundry of ellipse"
      

print(finddistanceinellipse([1, 1], 3, 2))  #inside ellipse 

print(finddistanceinellipse([1, 1], 3, 2))    #
print(finddistanceinellipse([4, 0], 3, 2))



# a = 3 → ellipse stretches 3 units along x-axis
# b = 2 → ellipse stretches 2 units along y-axis

# So:

# (3,0) is on boundary

# (0,2) is on boundary

# (4,0) is outside
# Ellipse equation:

# x²/a² + y²/b² = 1

# Your code computes:

# value = (x²/a²) + (y²/b²)

# Then:

# value < 1 → Inside

# value = 1 → On boundary

# value > 1 → Outside