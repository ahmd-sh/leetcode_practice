def search_rotated():
    nums = [4,5,6,7,0,1,2]
    target = 2

    l, r = 0, len(nums)-1
    while l <= r:
        mid = (l + r) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] >= nums[l]:
            if nums[mid] < target or nums[l] > target:
                l = mid + 1
            else:
                r = mid - 1
        else:
            if nums[mid] > target or nums[r] < target:
                r = mid - 1
            else:
                l = mid + 1

    return -1

print(search_rotated())
