
import openpyxl


days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
DAYTH = ['Sunday', 'Monday', 'Tuesday', 'Wendesday', 'Thursday', 'Friday', 'Saterday']


def list_sum(anylist):
    '''  '''
    list_sum = 0
    for each in anylist:
        list_sum += each
    return list_sum
    
def isleap(year):
    """Return True for leap years, False for non-leap years."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def adjust_date(month_v, date):
    '''  '''
    if month_v in Small_month:
        if date > 30:
            month_v += 1
            date -= 30
    elif month_v in Big_month:
        if date > 31:
            month_v += 1
            date -= 31
    else:
        if isleap(year):
            if date > 29:
                month_v += 1
                date -= 29            
        else:
            if date > 28:
                month_v += 1
                date -= 28
    return month_v, date


def adjust_mon(month_n):
    '''  '''
    global year
    if month_n > 12:
        year += 1
        month_n = 1
    return month_n


'''
def adjust_year(month_n):
    '''  '''
    if month_n > 12:
        year += 1
    return year
'''


def main():
    '''  '''
    global year, month, date_monday, date_sunday
    entry_string = input('Please input the YearMonthDate:')
    year = int(entry_string[:4])
    month = int(entry_string[4:6])
    date = int(entry_string[6:8])
##    year_num = year - 2017
##    month_num = month - 1
    date_num = date - 1
    days_of_year = []
    days_of_month = []
    sum_days = 0
    for each_year in range(2017, year):
        if isleap(each_year):
            days_of_year.append(366)
        else:
            days_of_year.append( 365)
    for each_month in range(1, month):
        days_of_month = days_in_month[1:month]
        if isleap(year):
            days_of_month[1] += 1   # Feb has 29 days.
    sum_days = list_sum(days_of_year) +  list_sum(days_of_month) + date_num
    dayth = sum_days % 7
    print(entry_string, ' is ', DAYTH[dayth])
    return DAYTH[dayth]



if __name__ == '__main__':
    '''  '''
    print('---Begin--------')
    print('----20170101 is Sunday.----')
    date_monday = 4
    month = 9
    Big_month = [10, 12, 1, 3, 5, 7, 8]
    Small_month = [9, 11, 4, 6]
    Feb = [2]
    main()
    print('---End--------')
