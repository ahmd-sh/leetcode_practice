nums = [2, 7, 11, 15]
target = 9

hashmap = {}

for i, val in enumerate(nums):
    needed = target - val
    res = hashmap.get(needed, -1)
    if res != -1:
        final = [i, res]
    hashmap[val] = i

print(final)
