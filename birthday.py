name = input('What is your name? ')
birthday_month = input('What month were you born? ')
print(f'Hello, {name}!')

# if birthday_month.lower() == 'august':
#     print('Happy birthday month!')

print(f'There are {len(name)} letters in your name')

from datetime import date

now = date.today()
current_month = now.month # If it's august this will be 8

current_month = now.strftime('%B')

if birthday_month.lower() == current_month.lower():
    print('Happy birthday month!')