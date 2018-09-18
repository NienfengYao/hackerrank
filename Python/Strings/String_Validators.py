if __name__ == '__main__':
    s = input()
    """
    print(sum([1 if i.isalnum() else 0 for i in s]) > 0)
    print(sum([1 if i.isalpha() else 0 for i in s]) > 0)
    print(sum([1 if i.isdigit() else 0 for i in s]) > 0)
    print(sum([1 if i.islower() else 0 for i in s]) > 0)
    print(sum([1 if i.isupper() else 0 for i in s]) > 0)
    """

    for test in ('isalnum', 'isalpha', 'isdigit', 'islower', 'isupper'):
        print(any(eval("c." + test + "()") for c in s))
