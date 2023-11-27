nums = [0,0,0,3,7,2,5,8,4,6,0,1]

if not nums:
    return 0

ns = set(nums)
longest_seq = 0

for n in ns:
    if n - 1 not in ns:
        current_num = n
        current_seq = 1

        while current_num + 1 in ns:
            current_num += 1
            current_seq += 1

        longest_seq = max(longest_seq, current_seq)

print(longest_seq)