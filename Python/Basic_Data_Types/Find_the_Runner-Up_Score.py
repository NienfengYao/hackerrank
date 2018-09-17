if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    """
    # set() for unique and sort it
    print(sorted(set(arr))[-2])
    """
    
    # avoid set and sort, came up with this
    arr = list(arr)
    z = max(arr)
    while max(arr) == z:
        arr.remove(z)
    print(max(arr))
