from datetime import date

def fine(act, exp):
    # non expired
    if act <= exp:
        return 0

    # expired
    if(act.year > exp.year):
        return 10000
    
    if(act.month > exp.month):
        return (act.month - exp.month) * 500
        
    if(act.day > exp.day):
        return (act.day - exp.day) * 15

act_day, act_mon, act_year = list(map(int, input().strip().split(' ')))
exp_day, exp_mon, exp_year = list(map(int, input().strip().split(' ')))
act = date(act_year, act_mon, act_day)
exp = date(exp_year, exp_mon, exp_day)
print(fine(act, exp))
