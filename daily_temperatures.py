def daily_temperatures():
    temperatures = [73,74,75,71,69,72,76,73]

    res = [0] * len(temperatures)
    stack = []

    for i in range(len(temperatures)):
        while stack and temperatures[stack[-1]] < temperatures[i]:
            res[stack[-1]] = i - stack[-1]
            stack.pop()
        stack.append(i)

    return res

print(daily_temperatures())
