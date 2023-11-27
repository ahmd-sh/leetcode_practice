# from operator import mul
# from functools import reduce

nums = [4,1,-1,2,-1,2,3]
l = len(nums)
answer = [1] * l

# Complexity is at least O(n^2)
# for i in range(l):
#    answer[i] = reduce(mul, [nums[x] for x in range(l) if x != i], 1)

right = 1

for i in range(1, l):
    answer[i] = answer[i-1] * nums[i-1]

for i in range(l-1, -1, -1):
    answer[i] = answer[i] * right
    right *= nums[i]

print(answer)