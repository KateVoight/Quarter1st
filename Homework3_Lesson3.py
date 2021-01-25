# task 1

numb1 = int(input('Введите первое число'))
numb2 = int(input('Введите второе число'))
my_total = numb1 / numb2
print(round(my_total))

def my_div(numb1, numb2):
    try:
        numb_1, numb_2 = float(numb_1), float(numb_2)
        answer = my_total
        return 'error', 'Ошибка числа'
    except ZeroDivisionError:
        return 'Делить на ноль нельзя!'
    return my_total

my_div(input(), input())

# СДЕЛАЛА ПО АНАЛОГИИ С РАЗБОРОМ. НЕ ПОНИМАЮ откуда у Вас берется половина кода и для чего !


# task 2

my_quest = input('Введите ваши: имя, фамилию, год рождения, город проживания, email и телефон.')

def personal_info(**kwargs):
    return kwargs

print(personal_info(
    name=input('Введите Ваше имя: '),
    surname=input('Введите Вашу фамилию: '),
    bday=input('Введите дату Вашего рожлдения: '),
    city=input('Из какого Вы города? '),
    email=input('Адрес электронной почты: '),
    phone=input('Ваш контактный телефон? '),
))

# task 3

numb1 = int(input('Введите первое число'))
numb2 = int(input('Введите второе число'))
numb3 = int(input('Введите третье число'))
# my_total = numb1 / numb2
# print(round(my_total))

def my_func(numb_1, numb_2, numb_3):
    my_list = [numb_1, numb_2, numb_3]
    try:
        my_list.pop(my_list.index(min(my_list)))
        return sum(my_list)


print(my_func(1, 2, 3))

# ВЫПОЛНЕНО ПО АНАЛОГИИ. РАСЧЕТ НЕПРАВИЛЬНЫЙ ДАЕТ!!!!! НЕ ПОНИМАЮ.............

# task 4

х = int(input('Введите целое число'))
y = int(input('Введите целое отрицательное число'))

def my_func(x, y):
    try:
        answer = x ** y
    except TypeError:
        return 'Введите целое значение'
    return answer


print(my_func(10, -4))

# ????????...................