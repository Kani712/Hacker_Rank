import math
import os
import random
import re
import sys


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))


def hourglass_sum(arr, i, j):
    sum = arr[i][j] + arr[i][j + 1] + arr[i][j + 2]  # top horizontal
    i += 1
    sum += arr[i][j + 1]                            # middle
    i += 1
    sum += arr[i][j] + arr[i][j + 1] + arr[i][j + 2]  # bottom horizontal
    return sum


def max_hourglasses(arr):
    # Given as constraint that the minimum value of A[i][j] can be -9
    max = -9 * 36
    for i in range(0, 4):
        for j in range(0, 4):
            sum = hourglass_sum(arr, i, j)
            # print(sum)
            if sum > max:
                max = sum
    return max


print(max_hourglasses(arr))
