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
# def time_check():
#     '''
#     '''
#     start = int(input('Enter the time at which the meeting needs to be started:'))
#     end = int(input('Enter the time at which the meeting needs to be ended:'))
#     if (start < end):
#         if (7 <= start < 22) and (7 < end <= 22):
#             return True
#         else:
#             print('The meeting or discussion can only be done between 7 and 22.')
#     else:
#         print('Invalid input! Try Again')
def ending_program(continue_loop):
    
    # Again asks the user whether he/she wants to print something else or not by typing 'Y' or 'END', accordingly.    
    if continue_loop != "Y" or continue_loop != "END":
        print("Please make sure that the input is either Y or END")
        return True
        
    # Let the code continue, if the user enters 'Y'
    if continue_loop == 'Y':          
        return True
    # Let the code break from the while loop, if the user enters 'END'
    elif continue_loop == 'END':          
        return False
    
        
        
def is_valid_time(start, end):
    '''
    '''
    print('Please, enter the starting and ending time of the meeting or discussion from 7 to 22.\n')
    # validInt = False
    # while not validInt:
    #     time_check()
    #     continue_loop = str(input("If you want to continue, then type 'Y' otherwise type 'END':"))          # Again asks the user whether he/she wants to print something else or not by typing 'Y' or 'END', accordingly.
    #     if continue_loop == 'Y' or continue_loop == 'y':          # Let the code continue, if the user enters 'Y'
    #         continue
    #     elif continue_loop == 'END' or continue_loop == 'end':          # Let the code break from the while loop, if the user enters 'END'
    #         break
    #     else:
    #         print("Enter a valid input out of these('Y, END') ")
    #         continue_loop = str(input("If you want to continue, then type 'Y' otherwise type 'END':"))
    
    if (start < end):
        if (7 <= start < 22) and (7 < end <= 22):
            return True
        else:
            print('The meeting or discussion can only be done between 7 and 22.')
    else:
        print('Invalid input! Meeting cannot end before starting')
        return False


def is_leap_year(year):
    '''
    

    Parameters
    ----------
    year : TYPE: int
        The year paramether will be checked whether it is every 4. For instance,
        if the year is 2026, it will return (True), if it is 2027,
        it will return (False)

    Returns True or False depending on the user input
    -------

    '''
    if year % 400 == 0:
        return True;
    
    if year % 100 == 0:
        return False;
    
    if year % 4 == 0:
        return True;
    
    return False;
    
            
def days_in_month(month, year):
    '''
    Parameters
    ----------
    month : TYPE: int
        Depending of the month that the user inputs, the maximum number of days
        will be either 30, 28, 29, or 31
    year : TYPE: int
        If it is a leap year 29 will be the maximum number of days for February,
        otherwise the maximum number of days available will be 28
    Returns
    -------
    TYPE
        Returns an int of respective number of days in a particular month

    '''
    # Checks if the month is either 4,6,9 or 11
    if month in (4,6,9,11):
        return 30;
    
    # Checks if the month is 2
    elif month == 2:
        if is_leap_year(year):
            return 28
        else:
            return 29;
        
    # If the month is not 4,6,9,11 or 2, the maximum amount of days will be 31
    else:
        return 31;
    
# def validating_input():
#     while True:

        
    
def is_valid_date(days_str, month_str, year_str):
    '''
    Returns
    -------
    days : TYPE: int
    month : TYPE: int
    TYPE
        
    Returns either True if the user input is valid, otherwise it will return False,
    and the user will have to input a valid date.
    '''
    print("Please input a valid date in a (25/9/2025) date format");
        
    if not (days_str and month_str and year_str):
        print("days, month or year cannot be empty");
        return False
        
    days = int(days_str);
    month = int(month_str);
    year = int(year_str);
        
    # If year is (not) between 2025 and 10000 it will prompt an error
    if not (2025 <= year < 10000):
        print("Year must be between 2025 and 10000");
        return False
    
    # If month is (not) between 1 and 12 it will prompt an error        
    if not (1 <= month <= 12):
        print("Month has to be between 1 and 12");
        return False
        
    respective_day = days_in_month(month, year)
        
    # If days is not between 1 and respective_day it will prompt an error    
    if not (1 <= days <= respective_day):
        print("Day must be ", respective_day, "for month ", month);
        return False
        
    return True
    
def is_subject(subject_str):
    if len(subject_str) >= 1 and len(subject_str) <= 30:
        return True
    else:
        return False

def add_record():
    
    # validation_func = is_valid_date(days_str, month_str, year_str)
    meeting_list = []
    
    
    while True:
        date_str = input("Please input a valid date in a (23/9/2025) format or END to finish: ").strip()
        
        if date_str.upper() == "END":
            break
        
        is_date = date_str.split("/")
        
        if len(is_date) != 3:
            print("Invalid date format. Please use DD/MM/YYYY format.")
            continue
        
        
        start = int(input('Enter the time at which the meeting needs to be started: '))
        end = int(input('Enter the time at which the meeting needs to be ended: '))
        subject = input("Please enter the subject that you wish to store: ").strip()
        
        
        
        
        day = is_date[0]
        month = is_date[1]
        year = is_date[2]
        
        # print(day)
        index = 0
            
        # Validating date input
        if not is_valid_date(day, month, year):
            continue
        
        # Validating time input
        if not is_valid_time(start, end):
            continue
        
        # Validating subject input
        if not is_subject(subject):
            print("Subject must be between 1 and 30 characters")
            continue
        
        # apointment_list = f"{day}/{month}/{year};{subject};{start}{end}"
        
        # A list of the apointment formatted accordingly
        appointment_data = [f"{day}/{month}/{year}", subject, start, end]
        
        
        meeting_list.append(appointment_data)
        
        print("\nAppointment added")
        # After the appointment is added the following print statement,
        # will display it to the user
        print("{:<18}\t{:<18}\t{:<18}\t{:<18}".format(
            appointment_data[0], 
            appointment_data[1],  
            appointment_data[2],  
            appointment_data[3],  
        ))
        
    print("{:<18}\t{:<18}\t{:<18}\t{:<18}".format("Date", "Subject",  "Start", "End"))
    print("{:<18}\t{:<18}\t{:<18}\t{:<18}".format("----","-------","-----","-----"))
    
    # We will loop through each appointment added to the list and display all the appointments
    # Note: This has to be the show_records() function
    for item in meeting_list:
            
        print("{:<18}\t{:<18}\t{:<18}\t{:<18}".format(
               item[0],  # date
               item[1],  # subject
               item[2],  # start
               item[3],  # end
           ))
add_record()