def print_n_times(n: int):
    if n<=0:
        return
    print("Recursion Execution")
    print_n_times(n-1)

if __name__ == '__main__':
    print_n_times(3)