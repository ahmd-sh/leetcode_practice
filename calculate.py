def calculate():
    s = "(1+(4+5+2)-3)+(6+8)"

    num, res = 0, 0
    sign = 1
    stack = []

    for char in s:
        if char.isdigit():
            num = (num * 10) + int(char)

        elif char in "+-":
            res += num * sign
            sign = -1 if char == "-" else 1
            num = 0

        elif char == "(":
            stack.append(res)
            stack.append(sign)
            res = 0
            sign = 1

        elif char == ")":
            res += sign * num
            res *= stack.pop()
            res += stack.pop()
            num = 0

    return res + (num * sign)

print(calculate())
