# Time: O(n * 2^n)

def subsets(self, nums: List[int]) -> List[List[int]]:
    res = []
    subset = []

    def dfs(i):
        if i >= len(nums):
            res.append(subset.copy())
            return

        # Include nums[i] in the subset
        subset.append(nums[i])
        dfs(i + 1)

        # Exclude nums[i] in the subset
        subset.pop()
        dfs(i + 1)

    dfs(0)
    return res
