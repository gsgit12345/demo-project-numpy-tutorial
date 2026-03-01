def sphere_check(point, radius):

    x = point[0]
    y = point[1]
    z = point[2]

    # Compute x² + y² + z²
    distance_squared = x*x + y*y + z*z

    # Compare with R²
    if distance_squared < radius*radius:
        return "Inside sphere"
    elif distance_squared == radius*radius:
        return "On sphere"
    else:
        return "Outside sphere"


print(sphere_check([1, 2, 1], 5))




# 1️⃣ Take x, y, z from the point
# 2️⃣ Compute:

# x² + y² + z²

# 3️⃣ Compare it with:

# R²

# That’s it.

# 🔵 Why This Works

# Sphere equation is:

# x² + y² + z² = R²

# If:

# Less than R² → inside

# Equal to R² → on boundary

# Greater than R² → outside

# 🔵 Example

# For:

# point = [1, 2, 1]
# radius = 5

# Compute:

# 1² + 2² + 1²
# = 1 + 4 + 1
# = 6

# R² = 25

# Since:

# 6 < 25

# Output:

# "Inside sphere"