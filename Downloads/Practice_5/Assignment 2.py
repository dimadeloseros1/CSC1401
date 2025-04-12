#     while True:
#         if month == 4 or month == 6 or month == 9 or month == 11:
#             if days >= 1 and days <= 30:
#                 return days;
#             else:
#                 print("Please make sure that the days are between 1 and 30")
            
# def date_31(month, days):
#     while True:
#         if month == 4 or month == 6 or month == 9 or month == 11:
#             if days >= 1 and days <= 30:
#                 return days;
        
# def date_28(month, days):
#     while True:
#         if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
#             if days >= 1 and days <= 31:
#                 return days

# def date_29(month, days):
#     while True:    
#         if month == 2:
#             if days >= 1 and days <= 28:
#                 return days

def is_leap_year(year):
    if year % 400 == 0:
        return True
    
    if year % 100 == 0:
        return False
    
    if year % 4 == 0:
        return True
    
    return False
    
            
def days_in_month(month, year):
    if month in (4,6,9,11):
        return 30
    
    elif month == 2:
        return 29 if is_leap_year(year) else 28
    
    else:
        return 31
    
def is_valid_date():
    print("Please input a valid date in a (25/9/2025) date format")
    
    while True:
        
        days_str = input("Please input a valid day in a month: ").strip()
        month_str = input("Please input a valid month in a year: ").strip()
        year_str = input("Please input a valid year: ").strip()
        
        if not (days_str and month_str and year_str):
            print("days, month, year cannot be empty")
            continue
        
        days = int(days_str)
        month = int(month_str)
        year = int(year_str)
        
        
        if not (2025 <= year < 10000):
            print("Year must be between 2025 and 10000")
            continue
            
        if not (1 <= month <= 12):
            print("Month has to be between 1 and 12")
            continue
        
        respective_day = days_in_month(month, year)
        
        if not (1 <= days <= respective_day):
            print("Day must be ", respective_day, "for month ", month)
            continue
        
        return (days, month, year)
    
print(is_valid_date())