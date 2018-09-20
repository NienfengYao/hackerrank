import textwrap

def wrap(string, max_width):
    """
    # solution 1
    new_str = [string[i-max_width:i] for i in range(max_width, len(string), max_width)]
    if (len(string) % max_width != 0):
        # print(int((len(string)/max_width))*max_width)
        new_str.append(string[int((len(string)/max_width))*max_width:])
    return "\n".join(new_str)
    """
    
    """
    # solution 2: better than solution 1
    return "\n".join([string[i:i+max_width] for i in range(0, len(string), max_width)])
    """
    
    # Using textwrap module
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
