import inline as inline
import matplotlib.pyplot as plt

2.3 / 1
# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# for g in range(c, d + 1):
#     print('\t' + str(g), end='')
# print(end='\n')
# for i in range(a, b + 1):
#     print(str(i) + '\t', end='')
#     for j in range(c, d + 1):
#         print(str(i * j), end='\t')
#     print(end='\n')

2.3 / 2
# a, b, z, count = int(input()), int(input()), 0, 0
# for i in range(a, b + 1):
#     if i % 3 == 0:
#         count += 1
#         z += i
# print(z / count)

2.4 / 2
# s = input()
# ln = len(s)
# cnt = 1
# for i in range(ln):
#     if i == (ln - 1):
#         print(s[i] + str(cnt), end='')
#     else:
#         if s[i] == s[i + 1]:
#             cnt = cnt + 1
#         else:
#             print(s[i] + str(cnt), end='')
#             cnt = 1

2.5 / 1
# z, cnt = input().split(), 0
# for i in z:
#     cnt += int(i)
# print(cnt)

2.5 / 2
# x = input().split()
# if len(x) > 1:  # создаю новый список
#     y = [int(x[i - 1]) + int(x[i + 1]) for i in range(-1, len(x) - 1)]
#     for i in range(1, len(y)):
#         print(y[i], end=' ')  # вывожу значения со второго до последнего
#     print(y[0])  # вывожу первое значение
# else:
#     print(x[0])
# ##########################################################################
# numbers = [int(i) for i in input().split()]
# if len(numbers) == 1:
#     print(numbers[0])
# else:
#     for i in range(len(numbers)):
#         print(numbers[i - 1] + numbers[(i + 1) % len(numbers)], end=" ")

2.5 / 3
# a, b = [int(i) for i in input().split()], []
# a.sort()
# for i in range(0, len(a) - 1):
#     if a[i] == a[i - 1]:
#         if a[i] not in b:
#             b.append(a[i])
# print(*b)
#
# a, c = [str(i) for i in input().split()], []
# for i in a:
#     if i not in c and a.count(i) > 1:
#         c.append(i)
#         print(i, end=' ')

2.6
# сапер
# n, m, k = (int(i) for i in input().split())  # чтение размеров поля и числа мин
# a = [[0 for j in range(m)] for i in range(n)]  # заполнение поля нулями
# for i in range(k):
#     row, col = (int(i) - 1 for i in input().split())
#     a[row][col] = -1  # расставляем мины
# for i in range(n):
#     for j in range(m):
#         if a[i][j] == 0:  # в этой клетке мины нет, поэтому считаем число мин вокруг
#             for di in range(-1, 2):
#                 for dj in range(-1, 2):
#                     ai = i + di
#                     aj = j + dj
#                     # (ai, aj)
#                     if 0 <= ai < n and 0 <= aj < m and a[ai][aj] == -1:
#                         a[i][j] += 1
# # вывод результата
# for i in range(n):
#     for j in range(m):
#         if a[i][j] == -1:
#             print('*', end='')
#         elif a[i][j] == 0:
#             print('.', end='')
#         else:
#             print(a[i][j], end='')
#     print()

2.6 / 1
# sum_a, summa_kv = 0, 0
# while True:
#     a = int(input())
#     sum_a += a
#     summa_kv += a**2
#     if sum_a == 0:
#         break
# print(summa_kv)

2.6 / 2
# n = int(input())
# a = []
# for i in range(1, n + 1):
#     c = min(i, n)
#     n = n - c
#     a += [i] * c
#     if n <= 0:
#         break
# print(*a)
###############################
# n = int(input())
# result = [i for i in range(1, n + 1) for __ in range(i)][:n]
# [print(i, end=" ") for i in result]
###############################
# n, v = int(input()), []
# for i in range(1, n + 1):
#     v += [str(i)] * i
# print(" ".join(v[:n]))
###############################
# numbers, list1 = int(input()), []
# for i in range(1, numbers+1):
#     list1.extend([i] * i)
# print(*list1[:numbers])

2.6 / 3
# lst = [int(i) for i in input().split()]
# x = int(input())
# if x in lst:
#     for i in range(len(lst)):
#         if lst[i] == x:
#             print(i, end=' ')
# else:
#     print('Отсутствует')
###############################
# l, n = [int(i) for i in input().split()], int(input())
# print(*[x for x in range(len(l)) if l[x] == n] if n in l else ["Отсутствует"])
###############################
# lst = [int(i) for i in input().split()]
# x, s = int(input()), []
# for i in range(0, len(lst)):
#     if x in lst:
#         if lst[i] == x:
#             s.append(i)
#     else:
#         s = ['Отсутствует']
# print(*s)

2.6 / 4
# s = []
# while True:
#     a = input().split()
#     if 'end' not in a:
#         s.append(a)
#     else:
#         break
# for i in range(len(s)):
#     for j in range(len(s[i])):
#         a = int(s[i - 1][j])
#         if i == len(s) - 1:
#             b = int(s[0][j])
#         else:
#             b = int(s[i + 1][j])
#         c = int(s[i][j - 1])
#         if j == len(s[i]) - 1:
#             d = int(s[i][0])
#         else:
#             d = int(s[i][j + 1])
#         res = a + b + c + d
#         print(res, end=' ')
#     print()
###############################
# c = []
# while True:
#     a = [i for i in input().split()]
#     if a == ['end']:
#         break
#     c.append(a)
# n, m = len(c), len(c[0])
# for i in range(n):
#     for j in range(m):
#         x = int(c[i][j-1]) + int(c[i][j+1-m]) + int(c[i-1][j]) + int(c[i+1-n][j])
#         print(x, end=' ')
#     print()

2.6 / 5
# ############################## МОЙ КОД НО ТОЛЬКО ДЛЯ 5-КИ
# n = int(input())
# matrix = [[0 for x in range(n)] for i in range(n)]
# for j in range(n):
#     for i in range(j + 1):
#         matrix[0][j] += 1
# for i in range(1, n):
#     for j in range(i + 5):
#         matrix[i][4] += 1
# for j in range(n-1):
#     for i in range(j - 14, -1):
#         matrix[4][j] += 1
# for i in range(1, n-1):
#     for j in range(i - 18, -1):
#         matrix[i][0] += 1
# for j in range(1, n-1):
#     for i in range(j + 16):
#         matrix[1][j] += 1
# for i in range(2, n-1):
#     for j in range(i + 18):
#         matrix[i][3] += 1
# for j in range(1, n-2):
#     for i in range(j - 25, -1):
#         matrix[3][j] += 1
# for j in range(1, n-2):
#     for i in range(j + 23):
#         matrix[2][j] += 1
#
# for i in range(n):
#     for j in range(n):
#         print(matrix[i][j], end=' ')
#     print()
# ############################## КОД В РЕШЕНИЯХ, САМЫЙ ПОНЯТНЫЙ
# n = int(input())
# t = [[0] * n for i in range(n)]
# i, j = 0, 0
# for k in range(1, n * n + 1):
#     t[i][j] = k
#     if k == n * n:
#         break
#     if i <= j + 1 and i + j < n - 1:
#         j += 1
#     elif i < j and i + j >= n - 1:
#         i += 1
#     elif i >= j and i + j > n - 1:
#         j -= 1
#     elif i > j + 1 and i + j <= n - 1:
#         i -= 1
# for i in range(n):
#     print(*t[i])
# ############################## 5*5 за 181 шаг
# n = int(input())
# # Создаем нулевую квадратную матрицу заданной размерности
# a = [[0 for i in range(n)] for j in range(n)]
# # Определяем внутренние счетчики для цикла
# i = 0  # строки
# j = 0  # столбцы
# x = 1  # текущее значение для заполнения ячейки
# k = 0  # порядковый номер контура
# while x <= n * n:
#     a[i][j] = x  # заполняем ячейку текущим значением
#     if i != j:  # Только если мы сейчас не на диагонали!
#         # Сумма зеркально расположенных элементов одинакова для текущего контура.
#         # Она равна нижнему правому значению в контуре, умноженному на 2.
#         # Так что на каждом шаге цикла мы заполняем зеркальный элемент матрицы,
#         # просто вычитая текущее x из этой суммы ;)
#         a[j][i] = (a[k][k] + (n - k * 2) * 2) * 2 - 4 - x
#     if j != n - k - 1:
#         # если еще не уперлись в правую границу контура, двигаемся вправо
#         j += 1
#     elif i != n - k - 1:
#         # если еще не уперлись в нижнюю границу контура, двигаемся вниз
#         i += 1
#     elif x != n * n:
#         # Если вправо и вниз уже нельзя, значит мы закончили обход текущего контура!
#         # Только не забываем проверить, что x не равен n*n, а то будет бо-бо.
#         k += 1  # переходим к следующему контуру
#         i = j = k  # обход следующего контура начнем с координат [k,k]
#         x = a[k][k - 1]  # текущее значение равно наибольшему в старом контуре
#     x += 1  # Ну, и не забываем прибавлять единичку в конце цикла, какое бы условие ни сработало.
# # Выводим на печать
# for i in a:
#     print(*i)
# ############################## 5*5 за 179  шагов
# def spiral(x, y, n):
#     if x >= y:
#         if x < n - y - 1:
#             return y * (4 * n - 4 * y - 1) + x + 1
#         else:
#             return x * (4 * n - 4 * x - 5) + 2 * n + y - 1
#     else:
#         if y > n - x - 1:
#             return y * (4 * n - 4 * y - 3) + 2 * n - x - 1
#         else:
#             return x * (4 * n - 4 * x - 7) + 4 * n - y - 3
# def print_spiral(n):
#     print("\n".join(["".join(["{0:4d}".format(spiral(x, y, n)) for x in range(n)]) for y in range(n)]))
#     # print("")
# print_spiral(int(input()))
# ############################## 5*5 за 216 шагов
# def get_matrix(n):
#     matrix = [[None] * n for _ in range(n)]
#     m = 1
#     x = y = cnt = 0
#     start_y, end_y = 1, n - 1
#     start_x, end_x = 0, n - 1
#     while start_x * m <= end_x * m or start_y * m <= end_y * m:
#         for x in range(start_x, end_x + 1 * m, m):
#             cnt += 1
#             matrix[y][x] = cnt
#         for y in range(start_y, end_y + 1 * m, m):
#             cnt += 1
#             matrix[y][x] = cnt
#         start_x, end_x = end_x - m, start_x
#         start_y, end_y = end_y - m, start_y
#         m *= -1
#     return matrix
# if __name__ == '__main__':
#     print('\n'.join(map(lambda r: ' '.join(map(lambda c: '%2d' % c, r)), get_matrix(int(input())))))
# ############################## 5*5 за 161 шаг
# # Создаётся функция, которая и будет всё делать
#     def zm(n):
#         # Переменной dx присваивается значение 1
#         # Переменной dy присваивается значение 0
#         # Обычно dx и dy - это некие приращения для переменных x и y
#         dx, dy = 1, 0
#         # Переменным x и y присваивается значение 0
#         x, y = 0, 0
#         # Создаётся список списков
#         # Это матрица n*n
#         # Пока все её элементы - пустые (None)
#         arr = [[None] * n for _ in range(n)]
#         # Выполняется перебор
#         # Для переменной i последовательно перебираем значения от 1 до (n-квадрат + 1)
#         for i in range(1, n**2+1):
#             # Элементу матрицы с координатами x и y присваивается значение i
#             # Эта строчка будет присваивать последовательные натуральные числа
#             # тем ячейкам, которые перебирает код чуть ниже
#             arr[x][y] = i
#             # Создаются временные переменные nx и ny
#             # в которых вычисляются новые значения для x и y
#             # для этого к старым значенииям прибавляются приращения
#             nx, ny = x+dx, y+dy
#             # Если всё нормально, и индекс не выскочил за пределы матрицы
#             # или не наткнулся на уже занятую ячейку
#             if 0 <= nx < n and 0 <= ny < n and not arr[nx][ny]:
#                 # то эти значения и оставляются
#                 x, y = nx, ny
#             else:
#                 # а если индекс выскочил за границу матрицы
#                 # или наткнулся на уже занятую ячейку
#                 # то разворачиваемся на 90 градусов
#                 # путем замены приращения по x и y друг на друга
#                 # а минус нужен, чтобы он не ходил только вправо или вниз,
#                 # а чередовал с движениями вверх или влево.
#                 # Так и получается спираль
#                 dx, dy = -dy, dx
#                 # и используем уже это изменённое движение для новых значений x и y
#                 x, y = x+dx, y+dy
#         # После того, как перебрали все элементы,
#         # печатаем то, что получилось
#         for x in list(zip(*arr)):
#             print(*x)
#     # А здесь вся вышеописанная функция
#     # вызывается с аргументом, который вводит пользователь с клавиатуры
#     zm(int(input()))
# ##############################
3.1 / 1
# def f(x):
#     if x <= -2:
#         return 1 - (x + 2) ** 2
#     elif x > -2 and x <= 2:
#         return -(x / 2)
#     else:
#         return (x - 2) ** 2 + 1

3.1 / 2
# def modify_list(lst):
#     i = 0
#     while i != len(lst):
#         if lst[i] % 2 == 1:
#             lst.pop(i)
#         else:
#             lst[i] //= 2
#             i += 1
#     return lst
########################
# def modify_list(l):
#     for i in range(len(l) - 1, -1, -1):
#         if l[i] % 2 == 0:
#             l[i] //= 2
#         else:
#             l.pop(i)
########################
# def modify_list(l):
#     l[:] = [i//2 for i in l if not i % 2]
########################
# def modify_list(l):
#     i = 0
#     while i < len(l):
#         if l[i] % 2 != 0:
#             del (l[i])
#         else:
#             l[i] = l[i] // 2
#             i += 1
########################

3.2 / 1
# def update_dictionary(d, key, value):
#     if key in d:
#         d[key] += [value]
#     elif 2 * key in d:
#         d[key * 2] += [value]
#     else:
#         d[key * 2] = [value]
# d = {}
# # print(update_dictionary(d, 1, -1))  # None
# # print(d)  # {2: [-1]}
# # update_dictionary(d, 2, -2)
# # print(d)  # {2: [-1, -2]}
# # update_dictionary(d, 3, -3)
# # print(d)  # {2: [-1, -2, -3]}

3.2 / 2
# n = input().lower().split()
# d = dict()
# for i in n:
#     z = n.count(i)
#     d.setdefault(i,z)
# for key, value in d.items():
#     print(key, value)
########################
# s = input().lower().split()
# for i in set(s):
#     print(i, s.count(i))

3.2 / 3
# s = {}
# for i in range(int(input())):
#     x = int(input())
#     if x not in s:
#         s[x] = f(x)
#     print(s[x])
########################
# x = [int(input()) for i in range(int(input()))]
# b = {x: f(x) for x in set(x)}
# print(*[b[i] for i in x], sep='\n')

3.3
# Чтение из файла
# a = open('hello.txt', 'r')
# # s1 = a.readline()
# # s2 = a.readline().strip()
# a.close()

# with open('hello.txt') as a:
#     for line in a:
#         line = line.strip()
#         print(line)
########################
# Запись в файл
# fil = open('hello.txt', 'w')
# fil.write('Some text\n')
# fil.write(str(25))
# fil.close()

# with open('hello.txt', 'w') as fil:
#     fil.write('Some text\n')
#     fil.write(str(25))

3.4 / 1
######################## РАБОТАЕТ
# with open('dataset_3363_2.txt', 'r') as inf:
#     a = inf.readline()
# b = []
# for i in range(len(a)):
#     if a[i].lower() in 'qwertyuiopasdfghjklzxcvbnm':
#         b += a[i]
#         a = a[:i] + "!" + a[i + 1:]
# c = a.split('!')[1:]
# for i in range(len(b)):
#     print(b[i] * int(c[i]), end="")
######################## РАБОТАЕТ
# with open('dataset_3363_2.txt') as inf:
#     a = inf.readline().strip()
#     a = list(a)
#     g = ''
#     z = ''
#     k = 0
#     q = 0
#     for i in a:
#         if i.isdigit() == False:
#             g = i
#             k = 0
#         else:
#             if k != 0:
#                 k = str(k)
#                 k += i
#                 print(k)
#                 z = z + (g * (int(k) - 1))
#             else:
#                 i = int(i)
#                 z = z + (g * i)
#                 k = i
# with open('dataset_3363_2.txt', 'w') as ouf:
#     ouf.write(z)
######################## РАБОТАЕТ
# with open('dataset_3363_2.txt', 'r') as inf:
#     s1 = inf.readline()
# import re
#
# g = re.findall(r'\d+', s1)
# f = [i for i in s1 if i.isalpha()]
# h = "".join([int(i) * j for i, j in zip(g, f)])
# with open('dataset_3363_2.txt', 'w') as inf:
#     inf.write(h)
######################## РАБОТАЕТ
# import re
# with open('dataset_3363_2 (1).txt', 'r+') as f:
#     a = re.split(r"(\d+)", f.readline())[:-1]
#     result = ''.join([y * int(x) for x, y in zip(a[1::2], a[::2])])
#     print(result)
#     f.seek(0)
#     f.write(result)
########################
# with open('dataset_3363_2.txt', 'r') as f:
#     s = f.readline().strip()
# i = 0
# while i < len(s):
#     j = i + 1
#     while j < len(s) and s[j].isdigit():
#         j += 1
#     print(s[i] * int(s[i+1:j]), end='')
#     i = j
######################## ОТЛИЧНОЕ РЕШЕНИЕ!!!
# s, d = input(), []
# for i in s:
#     if not i.isdigit():
#         d.append(i)
#     else:
#         d[-1] += i
# print(*[i[0]*int(i[1:]) for i in d], sep='')
# ########################

3.4 / 2
# text = open("dataset_3363_3.txt", 'r')
# s = text.read().replace('\n', ' ').lower().split()
# text.close()
# print(max(s, key=s.count), max(map(s.count, s)))
########################
# with open('dataset_3363_3.txt', 'r') as f:
#     s = f.read().lower().strip().split()
# w = max(s, key=s.count)
# print(w, s.count(w))

3.4 / 3
# with open('dataset_3363_4.txt', 'r') as f:
#     s = f.read().lower().strip().split()
#     dl = len(s)
#     o_summa0, o_summa1, o_summa2 = 0, 0, 0
#     for cnt in s:
#         cnt = cnt.strip().split(';')
#         del cnt[0]
#         summa = (int(cnt[0]) + int(cnt[1])+int(cnt[2])) / 3
#         print(summa)
#         o_summa0 += int(cnt[0]) / dl
#         o_summa1 += int(cnt[1]) / dl
#         o_summa2 += int(cnt[2]) / dl
#     print(o_summa0, o_summa1, o_summa2)
########################
# s = [0, 0, 0]
# n = 0
# with open('dataset_3363_4.txt') as f:
#     for line in f:
#         m = list(map(int, line.strip().split(';')[1:]))
#         print(sum(m)/3)
#         for i in 0, 1, 2:
#             s[i] += m[i]
#             n += 1
#     print(s[0]/n, s[1]/n, s[2]/n)

# 3.5 / 2
# import sys
# sys.argv = 'python3 my_solution.py arg1 arg2'
# print(sys.argv[1:])

3.6 / 1
# import requests
# with open('dataset_3378_2 (1).txt', 'r') as f:
#     s = f.read().strip()
#     r = requests.get(s)
#     print(len(r.text.splitlines()))  # можно обьединить и получится
#     # print(len(requests.get(f.read().strip()).text.splitlines()))

3.6 / 2
# import requests
# p = requests.get('https://stepic.org/media/attachments/course67/3.6.3/699991.txt')
# while True:
#     if not p.text.startswith('We'):
#         p = requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + p.text)
#         print(p.text)
#         continue
#     else:
#         print(p)
#         break
##########################################
# import requests
# url, name = 'https://stepic.org/media/attachments/course67/3.6.3/', '699991.txt'
# while name[:2] != 'We':
#     name = requests.get(url + name).text
# print(name)
##########################################
# import requests
# p = requests.get('https://stepic.org/media/attachments/course67/3.6.3/699991.txt')
# while not p.text.startswith('We'):
#     p = requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + p.text)
# print(p.text)

3.7 / 1
# n = int(input())
# teams = {}
# for i in range(n):
#     team1, goal1, team2, goal2 = input().split(';')
#
#     if team1 not in teams:
#         teams[team1] = {'plays': 0, 'wins': 0, 'draws': 0, 'loses': 0, 'score': 0}
#
#     if team2 not in teams:
#         teams[team2] = {'plays': 0, 'wins': 0, 'draws': 0, 'loses': 0, 'score': 0}
#
#     if goal1 > goal2:  # team1 wins
#         teams[team1]['wins'] += 1
#         teams[team1]['score'] += 3
#
#         teams[team2]['loses'] += 1
#         teams[team2]['score'] += 0
#
#     elif goal2 > goal1:  # team2 wins
#         teams[team1]['loses'] += 1
#         teams[team1]['score'] += 0
#
#         teams[team2]['wins'] += 1
#         teams[team2]['score'] += 3
#
#     elif goal1 == goal2:  # draw
#         teams[team1]['draws'] += 1
#         teams[team1]['score'] += 1
#
#         teams[team2]['draws'] += 1
#         teams[team2]['score'] += 1
#
#     teams[team1]['plays'] += 1
#     teams[team2]['plays'] += 1
#
# for team in teams:
#     values_order = ['plays', 'wins', 'draws', 'loses', 'score']
#     print("{}:{}".format(str(team), ' '.join([str(teams[team][key]) for key in values_order])))
#########################################
# def command(c, res):
#     if not c in dct: dct[c] = [0, 0, 0, 0, 0]
#     dct[c] = [dct[c][0] + 1,
#                 dct[c][1] + 1 if res == 3 else dct[c][1],
#                 dct[c][2] + 1 if res == 1 else dct[c][2],
#                 dct[c][3] + 1 if res == 0 else dct[c][3],
#                 dct[c][4] + res,]
# dct = {}
# for i in range(int(input())):
#     c1, g1, c2, g2 = input().split(';')
#     command(c1, 3 if g1 > g2 else 1 if g1 == g2 else 0)
#     command(c2, 3 if g2 > g1 else 1 if g1 == g2 else 0)
# for c in dct:
#     print('{}:{} {} {} {} {}'.format(c, *dct[c]))
3.7 / 2
# a, b, c, d, s1, s2 = input(), input(), input(), input(), [], []
# code = dict(zip(a, b))
# decode = dict(zip(b, a))
# for i in c:
#     s1.append(code[i])
# print(*s1, sep='')
# s2 = [decode[i] for i in d]
# print(*s2, sep='')
#########################################
# a, b, c, d = input(), input(), input(), input()
# print(''.join([b[a.find(x)] for x in c]))
# print(''.join([a[b.find(x)] for x in d]))
#########################################
# a, b, c, d = input(), input(), input(), input()
# print(*[dict(zip(a, b))[i] for i in c], sep='')
# print(''.join([dict(zip(b, a))[i] for i in d]))

3.7 / 3
# words, not_in = [input().lower() for _ in range(int(input()))], []
# for _ in range(int(input())):
#     txt = input().lower().split()
#     for i in txt:
#         if i not in words and i not in not_in:
#             not_in.append(i)
#             # print(i)
# print('\n'.join(not_in))
##########################################
# words = {input().lower() for _ in range(int(input()))}
# txt = set('\n'.join(input().lower() for _ in range(int(input()))).split())
# print('\n'.join(txt - words))
##########################################
# # формируем множество известных слов на основании построчного ввода
# dic = {input().lower() for _ in range(int(input()))}
# # заводим пустое множество для приема текста
# wrd = set()
# # т.к. текст построчно подается, а также в каждой строке несколько слов,
# # то каждую строку превращаем во множество и добавляем в единое множество wrd
# for _ in range(int(input())):
#     wrd |= {i.lower() for i in input().split()}
# # на вывод отправляем результат вычитания словарного множества dic
# # из текстового множества wrd; впереди ставим *, чтобы раскрыть поэлементно
# print(*(wrd-dic), sep="\n")

3.7 / 4
# x, y = 0, 0
# for i in range(int(input())):
#     d = input().split()
#     direction, steps = d[0], int(d[1])
#     if direction == 'север':
#         y += steps
#     elif direction == 'юг':
#         y -= steps
#     elif direction == 'восток':
#         x += steps
#     else:
#         # direction == 'запад':
#         x -= steps
# print(x, y)
# ##########################################
# x, y = 0, 0
# for i in range(int(input())):
#     s = input().split()
#     x += int(s[1]) * ((s[0] == 'восток') - (s[0] == 'запад'))
#     y += int(s[1]) * ((s[0] == 'север') - (s[0] == 'юг'))
# print(x, y)
##########################################
# data = {'север': 0, 'юг': 0, 'запад': 0, 'восток': 0}
# for key, value in [input().split() for _ in range(int(input()))]:
#     data[key] += int(value)
# print(data['восток'] - data['запад'], data['север'] - data['юг'])
##########################################
# d = {'север': 0, 'запад': 0, 'юг': 0, 'восток': 0}
# for i in range(int(input())):
#     x = input().split()
#     d[x[0]] += int(x[1])
# print(d['восток'] - d['запад'], d['север'] - d['юг'])
##########################################

3.7 / 5
# with open('dataset_3380_5.txt', 'r') as f, open('out.txt', 'w') as g:
#     s = []
#     v = 0
#     for line in f:
#         s += line.split()
#         v += 1
#
#     t = [0] * 11
#     t2 = [0] * 11
#     k = 0
#     for i in range(2, v * 3, 3):
#         k = int(s[i - 2])
#         if 1 <= k <= 11:
#             t[k - 1] += int(s[i])
#             t2[k - 1] += 1
#
#     for i in range(0, 11):
#         value = [i + 1, ' ', t[i] / t2[i], '\n']
#         for x in value:
#             g.write(str(x))
# ##########################################
# with open("dataset_3380_5.txt", "r") as f:
#     a = {str(i): [] for i in range(1, 12)}
#     [a[i[0]].append(int(i[2])) for i in map(lambda x: x.split('\t'), f.read().split('\n')) if i[0]]
#     [print(i, sum(a[i]) / len(a[i]) if len(a[i]) > 0 else '-') for i in map(str, range(1, 12))]
##########################################
# with open('dataset_3380_5.txt', 'r') as f:
# # s = f.read().strip()
# # # clas, fam, height = s.strip()
# # print(s)
# # d = dict(s)
# # print(d)
# for line in f:
#     # print(line)
#     string = line.rstrip().split('\t')
#     print(string)

# with open("dataset_3380_5.txt", "r") as f:
##########################################
# aa = {}
# with open('dataset_3380_5.txt', 'r') as f_inp:
#     for data in f_inp.read().splitlines():
#         class_, name, growth = data.split()
#         aa.setdefault(int(class_), []).append(int(growth))
# # print(aa)
# for key in range(1, 11 + 1):
#     if key in aa:
#         data = aa[key]
#         # print(data)
#         growth = sum(data) / len(data)
#     else:
#         growth = '-'
#     print(key, growth)  # или запись в файл
##########################################

3.8
# БИБЛИОТЕКА numpy
# from numpy import *
#
# # создание одномерного массива из списка целых чисел
# a = array([2, 3, 4])
# print(a)
# print()
#
# # создание 3х-мерного массива из 3х последовательностей чисел
# b = array([(2, 3, 4), (2, 4.9, 4), (2, 3, 8.5)])
# e = b.ndim  # размерность массива (одномерный, двумерный итд)
# f = b.shape  # размеры массива (число строк, столбцов итд)
# print(b)  # все числа имеют один тип - число с плавающей точкой
# print(e, f)
# print()
#
# # 3, 2 помещаются в дополнительные скобки, чтобы представлять из себя один объект - пару чисел
# z = zeros((3, 2))
# print(z)
# print()
#
# # функция arange аналогична функции range, но возвращает массив
# k = arange(10, 30, 5)
# print(k)
# print()
#
# # генерирует 12 чисел на отрезке от 0 до 4 с равным шагом
# m = linspace(0, 4, 12)
# print(m)
# print()
#
# n = arange(15).reshape(5, 3)
# print(n)
# print()
#
# a = array([10, 20, 30])
# b = arange(3)
# print(a, b, sep='\n')
# print(a + b, a - b, sep='\n')  # арифметические операции на массивах выполняются поэлементно
# print()
#
# print(a ** 2)
# print(2 * sin(a))
# print(a < 20)

3.9 / 1


# БИБЛИОТЕКА numpy

# import numpy as a
# import matplotlib.pyplot as b
# from pylab import show

# x = a.linspace(0, 5, 10)
# y = x ** 2
# print(x)
# print(y)

# СОЗДАНИЕ ФИГУРЫ
# b.figure()
# b.plot(x, y, 'r')
# b.xlabel('x')
# b.ylabel('y')
# b.title('title')
# b.show()
# или можно написать так
# fig = plt.figure()
# axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
# axes.plot(x, y, 'g')
# axes.set_xlabel('x')
# axes.set_ylabel('y')
# axes.set_title('title')
# show()


# 1 график, 2 фигуры
# fig = plt.figure()
# axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
# axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])
# main figure
# axes1.plot(x, y, 'g')
# axes1.set_xlabel('x')
# axes1.set_ylabel('y')
# axes1.set_title('title')
# insert figure
# axes2.plot(x, y, 'y')
# axes2.set_xlabel('x')
# axes2.set_ylabel('y')
# axes2.set_title('insert title')
# show()


# 2 графика 1|1
# fig, axes = plt.subplots(nrows=1, ncols=2)
# for ax in axes:
#     ax.plot(x, y, 'y')
#     ax.set_xlabel('x')
#     ax.set_ylabel('y')
#     ax.set_title('title')
# fig.tight_layout()  #чтобы элементы не пересекались
# show()


# указать размер фигуры
# fig, axes = plt.subplots(figsize=(12, 3))
# axes.plot(x, y, 'grey')
# axes.set_xlabel('x')
# axes.set_ylabel('y')
# axes.set_title('title')
# show()


# 1 график, 3 фигуры
# from pylab import *
# x, y, z, a = [], [], [], []
# for i in range(2000):
#     x.append(i / 1000)
#     y.append((i / 1000) ** 0.5)
#     z.append((i / 1000) ** (1 / 3))
#     a.append((i / 1000) ** (1 / 20))
# figure()
# plot(x, y, 'r')
# plot(x, z, 'b')
# plot(x, a, 'g')
# show()


#  1 график, 2 фигуры + легенды
# fig, axes = plt.subplots()
# axes.plot(x, x ** 2, label='y = x**2')
# axes.plot(x, x ** 3, label='y = x**3')
# axes.legend(loc=2)
# axes.set_xlabel('x')
# axes.set_ylabel('y')
# axes.set_title('title')
# show()


# построение гистограм
# from pylab import show
# from numpy.random import randn
# n = randn(10000)
# fig, axes = plt.subplots(1, 2, figsize=(12, 4))
# axes[0].hist(n)
# axes[0].set_title('Default histogram')
# axes[0].set_xlim((min(n), max(n)))
#
# axes[1].hist(n, cumulative=True, bins=50)
# axes[1].set_title('Cumulative default histogram')
# axes[1].set_xlim((min(n), max(n)))
# show()


