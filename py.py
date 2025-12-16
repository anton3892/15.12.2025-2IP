import random

# Создание поля для пользователя и компьютера
player = [['~', '~', '~'], ['~', '~', '~'], ['~', '~', '~']]
computer = [['~', '~', '~'], ['~', '~', '~'], ['~', '~', '~']]

# random.randint - генерирует случайное число от 0 до 2
player[random.randint(0, 2)][random.randint(0, 2)] = 'S'
while True:
    x, y = random.randint(0, 2), random.randint(0, 2)
    if player[x][y] != 'S':
        player[x][y] = 'S'
        break

computer[random.randint(0, 2)][random.randint(0, 2)] = 'S'
while True:
    x, y = random.randint(0, 2), random.randint(0, 2)
    if computer[x][y]!='S':
        computer[x][y]='S'
        break

print("Морской бой!")
print("S - ваш корабль, X - подбитый корабль, ~ - вода")

shots = 0
#Счетчик выстрелов

while True:
    print(f"Выстрел №{shots + 1}")
    print("Ваши корабли:")
    for row in player:
        print(' '.join(row))
    while True:
        try:
            x = int(input("\nСтрока: "))
            y = int(input("Столбец: "))

            if x<0 or x>2 or y<0 or y>2:
                print("Только 0, 1 или 2!")
                continue
            break
        except:
            print("Ошибка! Введите числа")
# join() собирает элементы списка в одну строку, разделяя их указанным символом
# or - Для проверки истены
# continue - Пропусти остаток текущего цикла и перейди к следующей итерации

    shots += 1

    if computer[x][y]=='S':
        print("Попал! Корабль противника потоплен!")
        computer[x][y]='X'
    elif computer[x][y]=='X':
        print("Вы уже потопили корабль здесь!")
    elif computer[x][y]=='O':
        print("Вы уже стреляли сюда и промахнулись!")
    else:
        print("Мимо!")
        computer[x][y]='O'

    if all(cell!='S' for row in computer for cell in row):
        print(f"Вы выиграли за {shots} выстрелов!")
        print("Все корабли противника потоплены!")
        break
# for row in computer - берем каждую строку из поля компьютера
# for cell in row - берем каждую клетку в текущей строке
# cell != 'S' - проверяем, НЕ равен ли символ в клетке 'S'

    print("\nКомпьютер ходит: ")
    while True:
        cx, cy = random.randint(0, 2), random.randint(0, 2)
        if player[cx][cy] not in ['X', 'O']:
            break
    if player[cx][cy] == 'S':
        print(f"Противник попал в ({cx},{cy})!")
        player[cx][cy] = 'X'
    else:
        print(f"Противник промахнулся")
        player[cx][cy] = 'O'
    if all(cell != 'S' for row in player for cell in row):
        print("Компьютер выиграл! Все ваши корабли потоплены!")
        break
# player[cx][cy] - смотрим, что находится в клетке (cx, cy) на поле игрока
# not in - проверяет, НЕТ ли значения в списке