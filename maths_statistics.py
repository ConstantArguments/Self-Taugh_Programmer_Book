import math
import statistics
import random

nums = []
for i in range (1, 11):
    nums.append(random.randint(1, 100))
nums.sort()

print(f"numbers: {nums}")
mean = statistics.mean(nums)
med = statistics.median(nums)
mode = statistics.mode(nums)

print(f"\nmean of numbers = {mean}")
print(f"median of numbers = {med}")
print(f"mode of numbers = {mode}")

 
parendicular = nums[2]
base = nums[6]
hypot = math.hypot(parendicular, base)

print(f"\nIf parendicular is {parendicular}, and base is {base}, ")
print(f"the hypotenuse is {hypot}")
