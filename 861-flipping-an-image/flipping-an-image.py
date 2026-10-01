import numpy as np

class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        mat = np.array(image)
        result = 1 - np.fliplr(mat)
        return result.tolist()