# Time: O(2^target)

def combination_sum(self, candidates: List[int], target: int) -> List[List[int]]:
    res = []

    def dfs(i, cur, tot):
        if tot == target:
            res.append(cur.copy())
            return
        if i >= len(candidates) or tot > target:
            return

        cur.append(candidates[i])
        dfs(i, cur, tot + candidates[i])

        cur.pop()
        dfs(i + 1, cur, tot)

    dfs(0, [], 0)
    return res
