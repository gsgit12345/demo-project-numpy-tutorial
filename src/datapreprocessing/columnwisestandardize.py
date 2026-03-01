import numpy as np

def columnwiseStandardise(matrix):

    matrix_array = np.array(matrix, dtype=float)

    # Standardization Formula:
    # z = (x - μ) / σ
    # where:
    # μ = mean of column
    # σ = standard deviation of column

    mean = np.mean(matrix_array, axis=0)   # column-wise mean
    std = np.std(matrix_array, axis=0)     # column-wise std deviation

    standardized_matrix = (matrix_array - mean) / std

    return standardized_matrix


X = [
    [76, 225],
    [75, 195],
    [72, 180],
    [82, 231]

]

print(columnwiseStandardise(X))