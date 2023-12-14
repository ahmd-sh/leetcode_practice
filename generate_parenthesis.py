def generate_parenthesis():
    n = 3

    st = []
    res = []

    def bt(open, closed):
        if open == closed == n:
            res.append(''.join(st))
            return

        if open < n:
            st.append("(")
            bt(open+1, closed)
            st.pop()

        if closed < open:
            st.append(")")
            bt(open, closed+1)
            st.pop()

    bt(0,0)
    return res

print(generate_parenthesis())
