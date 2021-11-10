# Создать список из трех любых элементов.
myspisok = [1, 'text', 2.56]

# Создать словарь из трех пар ключ-значение.
mysl = {1: 'RUSSIA', 2: 'FRANCE', 3: 'GERMANY'}
# print(mysl[3])

# Создать множество из трех элементов.
myr = {1, 2, 3}

# Из списка получить элементо с индексом 1
print('-' * 10)
print(myspisok[1])

# Напиать условие if с двумя блоками elif и блоком else.
print('-' * 10)
if myspisok[2] == 'text':
    print('2:text')
elif mysl[2] == 'RUSSIA':
    print('RUSSIA')
elif mysl[3] == 'FRANCE':
    print('FRANCE')
else:
    print('none')

# Написать цикл while.
print('-' * 10)
i = 0
while i in range(5):
    print(i)
    if i == 4:
        print('break')
        break
    i += 1

# Создать список из трех элементов и распечать его элементы с помощью цикла for
print('-' * 10)
spisok2 = [1, 'text', 2.56]
i = 0
for i in range(len(spisok2)):
    print(spisok2[i])

# распечатать числа от 0 до 5
print('-' * 10)
i = 0
for i in range(6):
    print(i)

# создать строку 'TEST', если в ней есть буква 'E', напечатать 'pass'
print('-' * 10)

s = 'TEST'
if s.find('E') != -1:
    print('pass')

# Запросить данные у пользователя и распечатать их используя форматированную строку.
print('-' * 10)
s = input('enter text: ')
o = f'User enter this text {s}'
print(o)

# Распечатать содержимое файла.
print('-' * 10)
with open('task02.txt', encoding='utf8') as myfile:
    for line in myfile:
        line = line.replace('\n', '')
        print(line)

# Создать функцию, которая принимает два аргумента, вернуть сумму двух аргументов.
print('-' * 10)


def myfunc(arg1, arg2):
    """
    :param arg1: - первый аргумент
    :param arg2: -второй аргумент
    :return:
    """
    return arg1 + arg2


print(myfunc(1, 2))
print(myfunc('str1', 'str2'))

# Создать функцию которая принимает любое количество параметров, распечаатать эти параметры.
print('-' * 10)

def myfunc2(*args):
    print(*args)

myfunc2(1,2,3,4,'text')