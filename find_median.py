# Author: Aubrey Floyd
# GitHub username: aubreyfloyd2
# Date: 2/13/2023
# Description: Function that takes as a parameter a list of numbers and returns the statistical
#              median of those numbers.

def find_median(some_nums):
    """Returns statistical median of list of numbers."""
    n = len(some_nums)
    nums_sorted = sorted(some_nums)  # sort the list
    if len(some_nums) % 2 == 0: # check if even
        median = ((nums_sorted[n//2-1]) + (nums_sorted[n//2])) / 2.0
    else: # else if odd
        median = nums_sorted[n//2]
    return median

# some_nums = [13,7,-3,82,4,9]
# print(find_median(some_nums))