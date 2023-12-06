def len_of_longest_substring():
    s = "abcabcbb"
    uniques = set()
    max_length = 0
    l = 0

    for r in range(len(s)):
        while s[r] in uniques:
            uniques.remove(s[l])
            l += 1
        uniques.add(s[r])
        max_length = max(max_length, len(uniques))

    return max_length

print(len_of_longest_substring())
