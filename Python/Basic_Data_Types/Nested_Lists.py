if __name__ == '__main__':
    recs = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        recs.append([name, score])
 
    sec_lowest_grade = sorted(set([i[1]for i in recs]))[1]
    # print(sec_lowest_grade)
    names = []
    for i in recs:
        if i[1] == sec_lowest_grade:
            names.append(i[0])
    print("\n".join(sorted(names)))
