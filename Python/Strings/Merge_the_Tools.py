def merge_the_tools(string, k):
    # your code goes here    
    for i in range(0, len(string), k):
        # print(string[i:i+k])
        tmp = string[i:i+k]
        while(tmp):
            print(tmp[0], end="")
            tmp = "".join(tmp.split(tmp[0]))
        print("")
    
    """
    for i in range(0, len(string), k):
        tmp = string[i:i+k]
        uni = []
        for j in tmp:
            if (j not in uni):
                uni.append(j)
        print("".join(uni))
    """

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
