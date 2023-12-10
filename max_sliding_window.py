from collections import deque

def max_sliding_window():
    nums = [1,3,3,5,5,3,-3,5,3,6,7]
    k = 3

    res = []
    dq = deque()

    for i in range(len(nums)):
        while dq and dq[0] < i-k+1:
            dq.popleft()

        while dq and nums[dq[-1]] <= nums[i]:
            dq.pop()

        dq.append(i)

        if i >= k-1:
            res.append(nums[dq[0]])

    return res

print(max_sliding_window())
