from collections import Counter

def check_inclusion():
    s1 = "ab"
    s2 = "eidbaooo"

    cntr, sl_w, matched = Counter(s1), len(s1), 0   

    for i in range(len(s2)):
        if s2[i] in cntr: 
            cntr[s2[i]] -= 1
            if cntr[s2[i]] == 0:
                matched += 1
        if i >= sl_w and s2[i-sl_w] in cntr: 
            if cntr[s2[i-sl_w]] == 0:
                matched -= 1
            cntr[s2[i-sl_w]] += 1

        if matched == len(cntr):
            return True

    return False

print(check_inclusion())
