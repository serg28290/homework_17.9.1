try:
    listing = list(map(int, input("Введите числа через пробел: ").split()))
except Exception:
    listing = list(map(int, input("Введите числа через пробел: ").split()))
try:
    number = int(input("Введите число: "))
except Exception:
    number = int(input("Введите число: "))


def sorting():
    return sorted(listing)


def binary_search(lst, item):
    left = 0
    right = len(sorting()) - 1
    res = False

    while left <= right and not res:
        middle = (left + right) // 2
        element = lst[middle]
        if element == item:
            res = True
        if element > item:
            right = middle - 1
        else:
            left = middle + 1
    return res


result = binary_search(sorting(), number)
if result:
    print("Элемент найден!")
else:
    print("Элемент не найден.")
