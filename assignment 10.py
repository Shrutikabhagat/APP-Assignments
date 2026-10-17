import numpy as np

# Temperatures recorded for 10 days
temp = np.array([32, 34, 31, 30, 33, 35, 36, 34, 32, 31])

# First 3 days
print("First 3 days:", temp[:3])

# Day 5 to Day 8
print("Day 5 to Day 8:", temp[4:8])

# Average, maximum, minimum and total
print("Average temperature:", np.mean(temp))
print("Maximum temperature:", np.max(temp))
print("Minimum temperature:", np.min(temp))
print("Total temperature:", np.sum(temp))

# Increase every temperature by 2°C using broadcasting
temp = temp + 2

# Modified array
print("Modified temperatures:", temp)
