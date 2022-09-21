import math
import os
import random
import re
import sys

def minMaxSum(arr):
	sorted_arr = sorted(arr)

	min_arr = sorted_arr[:4]
	max_arr = sorted_arr[1:]

	print(sum(min_arr), sum(max_arr))

if __name__ == "__main__":
	arr = list(map(int, input().rstrip().split()))

	minMaxSum(arr)
