import math
import os
import random
import re
import sys

def plusMinus(arr):
    positive = negative = zero = 0
    
    for x in range(len(arr)):
        if arr[x] > 0:
            positive += 1
        elif arr[x] < 0:
            negative += 1
        else:
            zero += 1
    # return plusMinus

    print("yo soy el negativo" + " " + str(positive/len(arr)))
    print("yo soy el positivo" + " " + str(negative/len(arr)))
    print("yo soy el zero" + " " + str(zero/len(arr)))

print(plusMinus(([-4, 3, -9, 0, 4, 1])))