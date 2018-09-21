def print_line(ch, num, col):
    # print(ch, num)
    line = [chr(ord(ch)+i) for i in range(num)]
    line = line[-1:0:-1] + line[:]
    print("-".join(line).center(col, "-"))

def print_rangoli(size):
    # your code goes here
    low, col = (size*2-1, size*2-1 + size*2-1-1) # alphabet:x, interval:x-1
    # print("low=%d col=%d" % (low, col))
    for i in range(1, low+1):
        if(i<size):
            print_line(chr(ord('a')+(size-i)), i, col)
        elif(i==size):
            print_line('a', i, col)
        else:
            print_line(chr(ord('a')+(i-size)), 2*size-i, col)
   
"""
def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase
    L = []
    for i in range(size):
        s = "-".join(alpha[i:size])
        # print(s)
        L.append((s[::-1]+s[1:]).center(4*size-3, "-"))
        # print((s[::-1]+s[1:]).center(4*size-3, "-"))        
    print('\n'.join(L[:0:-1]+L))
"""

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
