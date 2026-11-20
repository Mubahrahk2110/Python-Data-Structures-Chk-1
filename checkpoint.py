from operator import add


def multiply_items(items):
    result = 1
    for item in items:
        result *= item
    return result


numb = [1, 2, 3, 4, 5]
print(multiply_items(numb))

sample_list = [(2,5), (1,2), (4,4), (2,3), (2,1)]
sample_list.sort(key=lambda x: x[1])
print(sample_list)

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 400, 'b': 500, 'd': 600}

result = {key: add(d1.get(key, 0), d2.get(key, 0)) for key in set(d1) | set(d2)}
print(result)

n = int(input())

squares = {i: i * i for i in range(1, n + 1)}
print(squares)

items = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
sorted_items = sorted(items, key=lambda item: float(item[1]), reverse=True)
print('sorted items:', sorted_items)

numbers = {0, 1, 2, 3, 4}
for number in numbers:
    print(number)

numbers.add(5)
numbers.remove(2)
print(numbers)

# res = lambda x, y: x + y
# print(res(2,3))