nums = [5, 15, 25, 35, 45]

lowest = min(nums)
highest = max(nums)

normalized_list = list(map(lambda n: (n - lowest) / (highest - lowest), nums))

print(normalized_list)