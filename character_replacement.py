def character_replacement():
    s = "AABABBA"
    k = 2

    hm = {}
    l, max_f = 0, 0

    for r in range(len(s)):
        hm[s[r]] = 1 + hm.get(s[r], 0)
        max_f = max(max_f, hm[s[r]])

        if (r-l+1) - max_f > k:
            hm[s[l]] -= 1
            l += 1

    return r-l+1

print(character_replacement())
