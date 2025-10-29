import numpy as np
from typing import List 

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        nparray = np.array(matrix)
        transposed_array = nparray.T
        rotated_array = np.fliplr(transposed_array)
        matrix[:] = rotated_array.tolist()
      