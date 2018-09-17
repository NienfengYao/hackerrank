if __name__ == '__main__':
    N = int(input())
    lst = []
    for i in range(N):
        """
        cmd, *args = input().split()
        args = list(map(int, args))
        if cmd == "insert":
            lst.insert(int(args[0]), (args[1]))
        elif cmd == "print":
            print(lst)
        elif cmd == "remove":
            lst.remove(args[0])
        elif cmd == "append":
            lst.append(args[0])
        elif cmd == "sort":
            lst.sort()
        elif cmd == "pop":
            lst.pop()
        elif cmd == "reverse":
            lst.reverse()
        """
            
        # using eval()
        s = input().split()
        cmd = s[0]
        args = s[1:]
        if (cmd != "print"):
            cmd += "(" + ",".join(args) + ")"
            eval("lst." + cmd)
        else:
            print(lst)
