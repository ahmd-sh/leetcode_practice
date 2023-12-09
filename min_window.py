from collections import Counter

def min_window():
    s = "ADOBECODEBANC"
    t = "ABC"

    if t == "": return ""

    cntr_t = Counter(t)
    wndw = {}

    curr,req = 0,len(cntr_t)
    res,res_len = [-1, -1],float("infinity")
    l = 0
    for r in range(len(s)):
        chr = s[r]
        wndw[chr] = 1 + wndw.get(chr, 0)

        if chr in cntr_t and wndw[chr] == cntr_t[chr]:
            curr += 1

        while curr == req:
            if (r-l+1) < res_len:
                res = [l, r]
                res_len = r-l+1

            wndw[s[l]] -= 1
            if s[l] in cntr_t and wndw[s[l]] < cntr_t[s[l]]:
                curr -= 1
            l += 1

    l,r = res
    return s[l:r+1] if res_len != float("infinity") else ""

print(min_window())
