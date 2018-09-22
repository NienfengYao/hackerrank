def minion_game(string):
    # your code goes here
    """
        Key: find the rule
        
        The count_i of all substring that beginning at position i is
            len(string) - i
            
        Ex: string = BANANA
            B at position 0, count_0 = 6-0 = 6
            N at position 2, count_2 = 6-2 = 4
            N at position 4, count_4 = 2
            => Stuart = 12
            
            A at position 1, count_1 = 5
            A at position 3, count_3 = 3
            A at position 5, count_5 = 1
            => Kevin = 9
    """
    kevin, stuart = 0, 0
    len_s = len(string)
    for i in range(len_s):
        if s[i] in "AEIOU":
            kevin += len_s - i
        else:
            stuart += len_s -i
            
    if (kevin > stuart):
        print("Kevin", kevin)
    elif (kevin < stuart):
        print("Stuart", stuart)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
