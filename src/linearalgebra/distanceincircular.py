import numpy as np

def circleCheck(point, radius):

    x = point[0]
    y = point[1]

    distance = x*x + y*y

    if distance < radius*radius:
        return "Inside circle"
    elif distance > radius*radius:
        return "Outside circle"
    else:
        return "On circle"


print(circleCheck([1, 1], 3))



# Even Simpler Mental Model

# Think like this:

# Step 1 → Square both coordinates
# Step 2 → Add them
# Step 3 → Compare with R²

#  Simple Geometry Intuition

# Distance from origin = √(x² + y²)

# If distance < R → inside
# If distance = R → on boundary
# If distance > R → outside

# We skip square root to make it faster.

# 🔵 What Is This Code Doing?

# It checks:

# 👉 Is a point inside, outside, or exactly on a circle?

# Circle center is assumed to be (0,0).

# Circle equation:

# x₁² + x₂² = R²

# So we just compare:

# x₁² + x₂² with R²

