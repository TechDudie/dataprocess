def min(array):
    m = 1000000000
    for i in array:
        if i < m:
            m = i
    return m
def max(array):
    m = 0 - 1000000000
    for i in array:
        if i > m:
            m = i
    return m
def sum(array):
    total = 0
    for i in array:
        total += i
    return total
def mean(array):
    return sum(array) / len(array)
def median(array):
    if len(array) % 2 == 1:
        index = round(len(array) / 2)
        return array[index]
    else:
        return (array[len(a) / 2] + array[len((a / 2) - 1)]) / 2
data = [3,5,7,8,9]
print(min(data))
print(max(data))
print(sum(data))
print(mean(data))
print(median(data))
