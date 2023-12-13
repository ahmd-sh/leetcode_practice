def eval_RPN():
    tokens = ["18"]

    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
    }
    st = []

    for t in tokens:
        if t in ops:
            a = st.pop()
            b = st.pop()
            st.append(int(ops[t](b, a)))
        else:
            st.append(int(t))

    return st[-1]

print(eval_RPN())
