def reverse_num(num:int):
    rev = 0
    while(num!=0):
        rev = num%10 + rev*10
        num = num//10
    return rev


if __name__ == '__main__':
    num = 2134
    result = reverse_num(2134)
    print(result)