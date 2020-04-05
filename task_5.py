from datetime import datetime, timedelta
import random
import string

# current date plus one day
current_date = datetime.today() + timedelta(days=1)
# converts to str format
str_current_date = current_date.strftime("%d-%m-%y %H:%M")
print("Current date and time:", str_current_date)

# converts date and time from string format to datetime object
str_date_time = '2020-02-03 09:18:36.000'
str_date_time = datetime.strptime(str_date_time, "%Y-%m-%d %H:%M:%S.%f")
print("Day:", str_date_time.strftime("%d"))
print("Month:", str_date_time.strftime("%m"))
print("Year:", str_date_time.year)
print("Hours:", str_date_time.hour)
print("Minutes:", str_date_time.minute)

# generates 3 random numbers which are divisible by 5
nums = [random.randrange(100, 999, 5) for i in range(3)]
print("Generated number is divisible by 5:")
print(nums)

# generates string from 10 random characters
characters = string.printable
generated_string = ''.join(random.choice(characters) for i in range(10))
print("Generated_string:", generated_string)

# Generates 10 lottery tickets
tickets = [random.randrange(1000000000, 10000000000) for i in range(100)]
# selects 2 winning tickets
for i in range(2):
    print("Winner №{}:".format(i + 1), random.choice(tickets))

# Exception Handling
try:
    file = open("file.txt", 'r')
except FileNotFoundError:
    print("Oops...file not found!")
else:
    print("I'm working, when there is no exception ")
finally:
    print("I'm always working")