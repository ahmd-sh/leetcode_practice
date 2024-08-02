# Time: O(2^target)

def combination_sum(self, candidates: List[int], target: int) -> List[List[int]]:
    res = []

    def dfs(i, cur, target):
        if target == 0:
            res.append(cur.copy())
            return
        if i >= len(candidates) or target <= 0:
            return

        cur.append(candidates[i])
        dfs(i, cur, target - candidates[i])

        cur.pop()
        dfs(i + 1, cur, target)

    dfs(0, [], target)
    return res
