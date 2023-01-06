# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
    
#     *Пример:*
    
#     - 6 -> да
#     - 7 -> да
#     - 1 -> нет


user_input = int(input("Enter day number: "))
if 8> user_input > 5 : 
    print(f'- {user_input} -> yes')
elif 5 >= user_input > 0 :
    print(f'- {user_input} -> no')
else : 
    print('Entered number does not correspond to day of the week, enter number from 1 to 7')    




# #А давайте напишем более полезную программу, которая берет дату, и говорит какой это день недели?

# user_input = str(input("Enter your date in format 'dd.mm.yyyy' : "))
# date_list = user_input.split(".")

# #здесь уже сделали работу за нас с помощью модуля datetime
# def use_datetime(date_list):
#     import datetime
#     user_date = datetime.datetime(int(date_list[2]),int(date_list[1]),int(date_list[0]))
#     print(user_date.strftime("%A"))
# #можно попробовать вручную

# def use_manual(date_list):
#     # Нерешимой проблемой для меня оказалось правильно задать смещение по неделе начала введенного года относительно понедельника. Не знаю, по какой формуле вычислять его, может, подскажете?
#     # Пока сделал ручной ввод дня недели для 1го января, чтобы проверить работу. В 2022-м была суббота, день 6.
#     displacement = int(input("What weekday number was on 1st of january of the entered year?\n"))
#     if int(date_list[2])%4 ==0: leap = 1
#     else : leap = 2
    
#     month_count = int(date_list[1])
#     day_count = int(date_list[0])
#     print(day_count)
#     if 0< month_count <=7:
#         day_num = ((month_count-1)*31 - month_count//2 - leap) + day_count
#     elif 7 < date_list[1] < 12 : 
#         day_num = ((month_count-1)*31 - month_count//2 + 1 - leap )+ day_count
#     else : 
#         return print("month number is not correct")   
#     print(day_num)
    
#     weekday_num = (day_num+displacement-1)%7
#     print(weekday_num) 
#     weekdays = { 
#         1 : 'Monday',
#         2 : 'Tuesday',
#         3 : 'Wednesday',
#         4 : 'Thursday',
#         5 : 'Friday',
#         6 : 'Saturday',
#         7 : 'Sunday'}
#     if weekday_num in weekdays :
#         print('This day is '+weekdays[weekday_num])
#     else :
#         print('Entered number does not correspond to day of the week, enter number from 1 to 7')


# user_input = str(input("Enter your date in format 'dd.mm.yyyy' : "))
# date_list = user_input.split(".")
# use_datetime(date_list)
# # use_manual(date_list)


