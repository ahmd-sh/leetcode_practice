# Time: O(n! * n^2)
# Space: O(n! * n)

def permute(self, nums: List[int]) -> List[List[int]]:
    # Iterative
    perms = [[]]
    for n in nums:
        new_perms = []
        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, n)
                new_perms.append(p_copy)
        perms = new_perms
    return perms

    # Recursive
    if len(nums) == 0:
        return [[]]
    res = []
    perms = self.permute(nums[1:])
    for p in perms:
        for i in range(len(p) + 1):
            p_copy = p.copy()
            p_copy.insert(i, nums[0])
            res.append(p_copy)
    return res
