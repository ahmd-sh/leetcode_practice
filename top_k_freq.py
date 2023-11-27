from collections import defaultdict

nums = [4,1,-1,2,-1,2,3]
k = 2
res = []

hm = defaultdict(int)

for num in nums:
    hm[num] += 1

hm_s = sorted(hm.items(), key=lambda x: x[1], reverse=True)[:k]
for i in range(k):
    res.append(hm_s[i][0])

print(res)