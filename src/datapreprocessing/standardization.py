import numpy as np

def standardize_column(column):

    column_array=np.array(column,dtype=float)

    # Standardization Formula:
    # z = (x - mean) / standard_deviation


    mean=np.mean(column_array)

    std=np.std(column_array)

    standardized_data = (column_array - mean) / std

    return standardized_data

heights = [76, 75, 72, 82, 69, 74, 75, 71, 75]

standardized_heights = standardize_column(heights)

print(standardized_heights)
