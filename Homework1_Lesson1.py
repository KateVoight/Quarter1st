# task1
name = input('Как Вас зовут?')
print('Здравствуйте,' + name + '!')

age = input('Сколько Вам лет?')
print(age + ' - пожалуй, это самый замечательный возраст!')

#task2
insert_time = int(input('Здравствуйте! Введите количество секунд цифрами'))

hours = insert_time / 60 / 60
minutes = insert_time / 60 % 60
seconds = insert_time % 60

print(f'Введенное Вами количество секунд составит: Часов: {hours:.0f} Минут: {minutes:.0f} Секунд: {seconds}')

#task3
num = int(input('Введите пожалуйста число от 0 до 100'))

total = (str(num) + (str(num + num)) + (str(num + num + num)))
print('Сумма чисел составит: ' + total)

#task4
insert_num = int(input('Введите пожалуйста число от 10 до 99'))

first_num = insert_num // 10
second_num = insert_num % 10

while first_num > second_num:
    print(first_num)
    break
if first_num < second_num:
    print(second_num)

#task5
#task6