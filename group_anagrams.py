from collections import defaultdict

strs = ["eat","tea","tan","ate","nat","bat"]
res = defaultdict(list)

for s in strs:
    sorted_s = ''.join(sorted(s))
    res[sorted_s].append(s)

print(res.values())