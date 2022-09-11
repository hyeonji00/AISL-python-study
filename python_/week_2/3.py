import math
import os
import random
import re
import sys

def minMaxSum(arr):
	arr.sort()

	min_arr = arr[:4]
	max_arr = arr[1:]

	print(sum(min_arr), sum(max_arr))

if __name__ == "__main__":
	arr = list(map(int, input().rstrip().split()))

	minMaxSum(arr)
