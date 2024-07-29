# Time: O(n * 2^n)

def subsets_with_dup(nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()

    def backtrack(i, subset):
        if i == len(nums):
            res.append(subset.copy())
            return

        # With nums[i]
        subset.append(nums[i])
        backtrack(i + 1, subset)
        subset.pop()

        # Exclude nums[i]
        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        backtrack(i + 1, subset)

    backtrack(0, [])
    return res
