def sum_recursion(num : int):
    if num == 0:
        return 0
    return num + sum_recursion(num-1)

if __name__ == '__main__':
    print(sum_recursion(5))