import numpy as np
import cv2
from numpy import random
import os


class OneDimension:
    def __init__(self):
        pass

    # Wolfgram automata rules
    # input rule_set=1...255
    # it's turned into an 8 bit binary number
    # said number is applied as a rule list
    # ex. [1,0,0,1,1,1,0,0]

    def calculateState(self,a, b, c,rule_set):
        binary_string = format(rule_set, 'b').zfill(8)
        rule_list = [int(digit) for digit in binary_string]
        index = 7 - int(f"{a}{b}{c}", 2)  # The '2' specifies that it's a binary number.
        return rule_list[index]

    def generateImage(self,rule_set):
        max_gens = 100
        w = 10
        cells = random.randint(0, 1, size=(max_gens)).tolist()
        cells[len(cells) // 2] = 1

        image = np.full((max_gens * w, max_gens * w), 255, np.uint8)

        thickness = -1

        for nr, i in enumerate(cells):
            image = cv2.rectangle(image, (w * nr, 0), (w * (nr + 1), w), 255 - i * 255, thickness)

        for gen in range(1, max_gens):
            new_cells = cells.copy()

            lens = len(cells)
            for i in range(len(cells)):
                new_cells[i] = self.calculateState(cells[(i - 1) % lens], cells[i], cells[(i + 1) % lens],rule_set)

            for nr, i in enumerate(new_cells):
                image = cv2.rectangle(image, (w * nr, gen * w), (w * (nr + 1), gen * w + w), 255 - i * 255, thickness)
            cells = new_cells.copy()

        # cv2.imshow('image', image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        path = 'Pictures'
        cv2.imwrite(os.path.join(path, f"1D_{rule_set}.png"), image)