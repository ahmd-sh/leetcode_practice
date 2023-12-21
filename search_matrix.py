def search_matrix():
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 60

    for r in matrix:
        if r[-1] < target:
            continue
        else:
            l, h = 0, len(matrix[0])
            while l <= h:
                m = l + ((h - l) // 2)
                if r[m] > target:
                    h = m - 1
                elif r[m] < target:
                    l = m + 1
                else:
                    return True

    return False

print(search_matrix())
