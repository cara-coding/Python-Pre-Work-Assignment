# # Question 1
# # Write a function to print "hello_USERNAME!" USERNAME is the input of the function.
# #  The first line of the code has been defined as below.

# def hello_name(user_name):
#     print("hello_" + user_name.upper() + "!" )

# hello_name('username')

# # Question 2
# # Write a python function, first_odds that prints the odd numbers from 1-100 
# # and returns nothing


# def first_odds(start,end):

#   for num in range(start, end +1):
#       if num % 2 != 0:
#           print(num)

# # first_odds(0,100) **return


# # Question 3
# # Please write a Python function, max_num_in_list to return the max number of
# #  a given list. 


# def max_num_in_list(a_list):
#     print(max(a_list))

# a_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# max_num_in_list(a_list)

# Question 4
# Write a function to return if the given year is a leap year. A leap year is 
# divisible by 4, but not divisible by 100, unless it is also divisible by 400.
#  The return should be boolean Type (true/false).


# def is_leap_year(a_year):

    

#     if(a_year % 4 == 0) and (a_year % 100 != 0):

#       return True

#     if(a_year % 100 == 0) and (a_year % 400 == 0):
#       type(True)

#     else:
#       return False


# print(is_leap_year(1987))


def is_consecutive(a_list):
    
    return sorted(a_list) ==list(range(min(a_list), max(a_list) +1))
      



print(is_consecutive([8,2,5]))




    

   






















  