# Needlessly complex way to solve this string reversal problem

# s = "A man, a plan, a canal: Panama"
s = "race a car"
lowercase = range(97, 123)
uppercase = range(65, 91)
numbers = range(48, 58)

l = len(s)
i, j = 0, l-1

res = True

while i < j:
    while (
        i < j and
        ord(s[i]) not in lowercase and
        ord(s[i]) not in uppercase and
        ord(s[i]) not in numbers
    ):
        i += 1

    while (
        j > i and
        ord(s[j]) not in lowercase and
        ord(s[j]) not in uppercase and
        ord(s[j]) not in numbers
    ):
        j -= 1

    if s[i].lower() != s[j].lower():
        res = False
        break
    i += 1
    j -= 1

print(res)