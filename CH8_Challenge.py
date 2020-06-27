"""1. Call a different function from the statistics module.
"""

import statistics
import random

def stats():
    nums = []
    for i in range (1, 101):
        nums.append(random.uniform(0, 100))
    nums.sort()

    print(f"numbers: {nums}")
    medgrpd = statistics.median_grouped(nums)
    medlow = statistics.median_low(nums)
    medhigh = statistics.median_low(nums)

    print(f"\ngrouped median of numbers = {medgrpd}")
    print(f"low median of numbers = {medlow}")
    print(f"high median of numbers = {medhigh}")

stats()

"""2. Create a module named cubed with a function that takes a number as a
    parameter, and returns the number cubed. Import and call the function from
    another module.
"""

import cubed #normally imports at top of file

num = input("\n\nEnter a number: ")
num = float(num)

print(cubed.cuber(num))
