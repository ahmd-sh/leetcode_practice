def two_sum():
    numbers = [5,25,75]
    target = 100

    i, j = 0, len(numbers) - 1
    while i < j:
        current_sum = numbers[i] + numbers[j]
        if current_sum == target:
            return [i+1, j+1]
        if current_sum > target:
            j -= 1
        if current_sum < target:
            i += 1

print(two_sum())