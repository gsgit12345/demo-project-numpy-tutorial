import numpy as np

def minmaxcolumnNormalization(column):

    column_array = np.array(column, dtype=float)

    # Min-Max Normalization Formula:
    # x' = (x - xmin) / (xmax - xmin)

    xmin = np.min(column_array)
    xmax = np.max(column_array)

    data = (column_array - xmin) / (xmax - xmin)

    return data


heights = [76, 75, 72, 82, 69, 74, 75, 71, 75]

normalized_heights = minmaxcolumnNormalization(heights)

print(normalized_heights)