# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

count = int(input('Введите кол-во монет '))

var = 0
count_0 = 0
count_1 = 0

for i in range(count):
    var = int(input(f'Положение монеты {i}: 0 или 1 ? '))
    if var == 1:
        count_1 += 1
    else:
        count_0 += 1
if count_1 < count_0:
    print(f'Кол-во монет, чтобы перевернуть: {count_1}')
else:
    print(f'Кол-во монет, чтобы перевернуть: {count_0}')
