def max_area():
    height = [1,8,6,2,5,4,8,3,7]
    res = 0
    i, j = 0, len(height)-1
    
    while i < j:
        area = (j - i) * min(height[i], height[j])
        # OR do area calculation in the max fn below
        # for better memory but worse runtime
        res = max(res, area)

        if height[i] < height[j]:
            i += 1
        else:
            j -= 1

    return res

print(max_area())