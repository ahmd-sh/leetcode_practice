def three_sum():
    nums = [-1,0,1,2,-1,-4]

    l = len(nums)
    if l < 3:
        return []

    res = []
    nums.sort()

    for i, val in enumerate(nums):
        if i > 0 and val == nums[i-1]:
            continue

        j, k = i+1, l-1
        while j < k:
            ts = val + nums[j] + nums[k]
            if ts > 0:
                k -= 1
            elif ts < 0:
                j += 1
            else:
                res.append([val, nums[j], nums[k]])
                j += 1
                while nums[j] == nums[j-1] and j < k:
                    j += 1

    return res

print(three_sum())