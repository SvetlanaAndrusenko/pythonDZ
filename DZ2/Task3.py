# Task3 Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

month = int(input('Enter the number of month:'))

month_list = ['winter','spring','summer','autumn']

month_dict = {'winter':[12,1,2],'spring': [3,4,5], 'summer': [6,7,8], 'autumn': [9,10,11]}

print(month_list)
print(month_dict)

# Программа через список
if (month == 12 or month == 1 or month == 2):
    print(f'{month} - {month_list[0]}')
else:
    if (month == 3 or month == 4 or month == 5):
        print(f'{month} - {month_list[1]}')
    else:
        if (month == 6 or month == 7 or month == 8):
            print(f'{month} - {month_list[2]}')
        else:
            if (month == 9 or month == 10 or month == 11):
                print(f'{month} - {month_list[3]}')
            else:
                print('Enter the right number from 1 to 12')

# Программа через словарь
for key, value in month_dict.items():
    if month in value:
        print(f'{month} - {key}')




