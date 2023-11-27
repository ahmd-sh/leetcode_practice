nums = [2, 7, 11, 15]
target = 9

hashMap = {}
for i in range(len(nums)):
    needed = target - nums[i]
    res = hashMap.get(needed, -1)
    if res != -1:
        final = [nums[i], res]
    hashMap[nums[i]] = i

print(final)
