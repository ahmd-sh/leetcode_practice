def three_sum():
    nums = [-1,0,1,2,-1,-4]

    if len(nums) < 3:
        return []

    res = []
    nums.sort()

    for i, val in enumerate(nums):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        l, r = i+1, len(nums)-1
        while l < r:
            three_sum = val + nums[l] + nums[r]

            if three_sum < 0:
                l += 1
            
            elif three_sum > 0:
                r -= 1
            
            else:
                res.append([val, nums[l], nums[r]])
                l += 1
                r -= 1

                while l < r and nums[l] == nums[l-1]:
                    l += 1

    return res

print(three_sum())
