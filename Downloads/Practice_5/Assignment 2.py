
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
    
def show_records(appointment_list):
    '''
    Parameters
    ----------
    appointment_list : TYPE: list
        This function loops through the appointment_list paramether,
        and returns all the records which the user has input through.

    Returns
    -------
    A list of all the records which the user has input.

    '''
    for item in appointment_list:
            
        print("{:<18}\t{:<18}\t{:<18}\t{:<18}".format(
               item[0],  # date
               item[1],  # subject
               item[2],  # start
               item[3],  # end
           ))

def is_concurrent_appointment(input_appointment, appointment_list):
    '''
        This function is in-charge of checking wether there is a conflict between
        the date and time values in any of the list appointments and the current
        user appointment

    Parameters
    ----------
    input_appointment : TYPE
        string list
    appointment_list : TYPE
        string list

    Returns
    -------
    bool
        True if there is an overalp, False otherwise

    '''
    date = input_appointment[0]
    input_start_time = input_appointment[2]
    input_end_time = input_appointment[3]
    
    for appointment in appointment_list:
        list_date = appointment[0]
        list_start_time = appointment[2]
        list_end_time = appointment[3]
        
        # Check for an existing appointment stored in the list and compares it,
        # with the one that user just input
        if date == list_date:
            # if both of the dates above match, the following conditional statement will check,
            # whether the a list (end time) is less than (input start time), and
            # whether the (input end time) is greater than (list start time)
            
            if (input_start_time < list_end_time and input_end_time > list_start_time):
                return True
            
    return False
       
    
def add_record():
    
    # validation_func = is_valid_date(days_str, month_str, year_str)
    appointment_list = []
    
    # date = date_func()
    # date_func()    
    
    while True:
        
        # is_date = date
        date_str = input("Please input a valid date in a (23/9/2025) format or END to finish: ").strip()
        if date_str.upper() == "END":
            break
            
        is_date = date_str.split("/")
            
        if len(is_date) != 3:
            print("Invalid date format. Please try again")
            continue
        
        start = int(input('Enter the time at which the meeting needs to be started: '))
        end = int(input('Enter the time at which the meeting needs to be ended: '))
        subject = input("Please enter the subject that you wish to store: ").strip()
        
        
        day = is_date[0]
        month = is_date[1]
        year = is_date[2]
        
        # print(day)
        # index = 0
            
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
        
        if is_concurrent_appointment(appointment_data, appointment_list):
            print("Please make sure that the appointment is not held at the same time as the previous appointment")
            continue
        
        appointment_list.append(appointment_data)
            
        
        
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
    
    
    
    # We will loop through each appointment added to the list 
    # and display all the appointments via the show_records() function
    show_records(appointment_list)
    
add_record()