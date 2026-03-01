import numpy as np

v_arr=np.array([3,4],dtype=float)

magnitude = np.linalg.norm(v_arr) # 9+16=25-5

print(magnitude)

unit_vector = v_arr / magnitude

print("Unit vector:", unit_vector)
print("Magnitude:", np.linalg.norm(unit_vector))