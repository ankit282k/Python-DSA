def palindrome(num:int):
    original_num = num
    rev = 0
    while(num!=0):
        rev = num%10 + rev*10
        num = num//10

    if rev == original_num:
        return True
    else:
        return False

if __name__ == '__main__':
    num = 121
    result = palindrome(num)
    print(result)