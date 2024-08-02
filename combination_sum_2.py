def combination_sum_2(candidates: List[int], target: int) -> List[List[int]]:
    res = []
    candidates.sort()

    def backtrack(i, cur, target):
        if target == 0:
            res.append(cur.copy())
            return
        if i >= len(candidates) or target <= 0:
            return

        cur.append(candidates[i])
        backtrack(i + 1, cur, target - candidates[i])
        cur.pop()

        while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
            i += 1
        backtrack(i + 1, cur, target)

    backtrack(0, [], target)
    return res
