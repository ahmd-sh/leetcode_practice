def is_valid_parentheses():
    s = "[({})]"

    hm = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    if s and s[0] in hm:
        return False

    st = []
    for c in s:
        if c in hm:
            if st and st[-1] == hm[c]:
                st.pop()
            else:
                return False
        else:
            st.append(c)

    return len(st) == 0

print(is_valid_parentheses())
