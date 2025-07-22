import calendar


cl = calendar.Calendar(firstweekday=0)

def month_calendar(year, month):
    return list(cl.itermonthdates(year, month))
        
        
    

def date_day_cl(year,month):
    for c in list(cl.itermonthdays2(year, month)):
        
        print(c)

if __name__ == "__main__":
    print(list(month_calendar(2025,8)))