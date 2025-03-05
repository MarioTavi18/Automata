import numpy as np
import cv2
from numpy import random
import os


class TwoDimension:
    def __init__(self):
        pass

    def calculateState(self):
        return np.random.uniform(0, 1)  # Correct approach
        #return np.random.choice([0,1],p=[0.2,0.8])

    def generateImage(self):
        w = 10

        height, width = 50 * w, 50 * w
        image = np.ones((height, width), dtype=np.uint8)

        rows = height // w
        cols = width // w
        grid = np.random.choice([0, 255], size=(rows, cols), p=[0.2, 0.8])

        # state initial
        for i in range(rows):
            for j in range(cols):
                image[i * w:(i + 1) * w, j * w:(j + 1) * w] = grid[i][j]

        gen=0
        font = cv2.FONT_HERSHEY_SIMPLEX
        bottomLeftCornerOfText = (10, 30)
        fontScale = 1
        fontColor = (0,0,0)
        thickness = 2

        while True:
            # Recreate generation counter image
            counter_image= np.full([50,320,3],255,np.uint8)
            #counter_image = np.ones((50, 300, 3), np.uint8) * 255
            cv2.putText(counter_image, f'Generation: {gen}', bottomLeftCornerOfText, font, fontScale, fontColor, thickness,cv2.LINE_AA)

            gen +=1
            # Display the images
            cv2.imshow('Random Game of Life Grid', image)
            cv2.imshow('Counter', counter_image)
            for i in range(rows):
                for j in range(cols):
                    image[i*w:(i+1)*w,j*w:(j+1)*w]=self.calculateState()*255

            k = cv2.waitKey(200) & 0xFF
            if k==ord('q'):
                break
        cv2.destroyAllWindows()

        # Optionally save the image