# # Faster runtime on LC than O(log n) solution
# def find_min():
#     nums = [3,4,5,1,2]
#     return min(nums)

def find_min():
    nums = [3,4,5,1,2]

    l, r = 0, len(nums)-1 
    curr_min = float("inf")

    while l < r:
        mid = (l + r) // 2
        curr_min = min(curr_min, nums[mid])

        if nums[mid] > nums[r]:
            l = mid + 1
        else:
            r = mid - 1

    return min(curr_min, nums[l])

print(find_min())
