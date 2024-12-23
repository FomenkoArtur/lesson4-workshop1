if __name__ == "__main__":
    n = int(input("Введите количество элементов в массиве: "))
    numbers = []
    for _ in range(n):
        num = float(input("Введите элемент массива: "))
        numbers.append(num)
    print("Максимум в массиве:", find_max(numbers))
