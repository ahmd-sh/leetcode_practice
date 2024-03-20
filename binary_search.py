def search():
    nums = [-1,0,3,5,9,12]
    target = 9

    # Recursive
    # def bs(nums, target, l, u):
    #     if l > u:
    #         return -1

    #     mid = l + ((u-l)//2)
    #     if target == nums[mid]:
    #         return mid
    #     elif target < nums[mid]:
    #         return bs(nums, target, l, mid-1)
    #     else:
    #         return bs(nums, target, mid+1, u)

    # return bs(nums, target, 0, len(nums)-1)

    # Iterative
    l, r = 0, len(nums) - 1

    while l <= r:
        m = l + (r - l) // 2
        if target > nums[m]:
            l = m + 1
        elif target < nums[m]:
            r = m - 1
        else:
            return m

    return -1

print(search())
