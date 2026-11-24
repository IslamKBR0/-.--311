# # ctrl + / почти во всех ide раскоментирует выделенную область на всякий напомню
#
# # № 1
# import matplotlib.pyplot as plt
# from sklearn.linear_model import  LinearRegression
# import numpy as np

# fahrenheit = [[-88.6], [-29.2], [32.0], [93.2], [129.2], [152.6], [212.0]]
# kelvin = [[206.15], [239.15], [273.15], [307.15], [327.15], [340.15], [373.15]]
#
# lr = LinearRegression()
# lr.fit(fahrenheit, kelvin)
# lr.predict([[256], [123]])
# lr.coef_
# lr.intercept_
# fahrenheit_test = [[-50], [10], [30], [70], [100], [150], [200]]
# kelvin_test = lr.predict(fahrenheit_test)
#
# x_range = np.arange(-100, 220)
# y_range = (x_range + 459.67) / 1.8
#
# plt.figure(figsize=(15, 8), dpi=280)
# plt.plot(x_range, y_range, label='уравнениие', linewidth='1')
# plt.scatter(fahrenheit, kelvin, label='входные данные', color='green')
# plt.scatter(fahrenheit_test, kelvin_test, label='предсказуеммое значение', color='blue')
# plt.xlabel('Фаренгейт')
# plt.ylabel('Кельвин')
# plt.legend(fontsize='6')
# plt.grid(True)
# plt.show()
#
# # № 3
# import matplotlib.pyplot as plt
#
# games = [
#     'CS2',
#     'Dota 2',
#     'PUBG',
#     'Phantom Blade',
#     'Bongo Cat',
#     'Apex Legends',
#     'Call of Duty',
#     'Wallpaper Engine',
#     'Team Fortress 2',
#     'Slay the Spire 2'
# ]
#
# middle_online = [
#     788648,
#     555659,
#     451038,
#     292762,
#     170593,
#     128713,
#     104364,
#     94643,
#     90202,
#     82496
# ]
#
# #plt.bar(games, middle_online)
# #plt.pie(middle_online, labels=games)
# #plt.barh(games, middle_online)
#
# plt.xticks(rotation=22.5)
# plt.title('10 самых популярных игр')
# plt.xlabel('Игры')
# plt.ylabel('Средний онлайн')
#
# plt.show()
#
# # № 4
# from math import factorial, pi, nan, e, gcd
# print(e, pi, nan, factorial(10), gcd(10, 64), sep='\n', end='')
#
#
#
#
#
#
#
#
# # № 1 из заданий повышенной сложности, сидел минут 40 делал,
# # нарисовал какую то фигню отдаленно схожего на кота
# # это можно было намного красивее и лаконичнее сделать но
# # я сделал это просто в лоб и наговнокодил вообщем
import matplotlib.pyplot as plt

x = [0, 15, 25, 40, 20, 0]
y = [20, 33, 33, 20, 0, 20]

x1 = [10, 11, 12, 13, 14, 15]
y1 = [25, 26, 27, 28, 29, 30]

x2 = [25, 26, 27, 28, 29, 30]
y2 = [30, 29, 28, 27, 26, 25]

x3 = [7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5]
y3 = [27.5, 29, 30.5, 32, 33.5, 35, 33.5, 32, 30.5]

x4 = [32.5, 32, 31.5, 31, 30.5, 30, 29.5, 29, 28.5]
y4 = [27.5, 29, 30.5, 32, 33.5, 35, 33.5, 32, 30.5]

x5 = [15, 25]
y5 = [10, 10]

x6 = [16.5, 17, 17.5, 18, 18.5]
y6 = [10, 9, 8, 9, 10]

x7 = [21.5, 22, 22.5, 23, 23.5]
y7 = [10, 9, 8, 9, 10]

x8 = [15, 15.1]
y8 = [22.5, 22.4]

x9 = [25, 24.9]
y9 = [22.5, 22.4]

x10 = [15.04, 15.05]
y10 = [22.45, 22.46]

x11 = [24.95, 24.96]
y11 = [22.45, 22.46]

x12 = [18, 20, 22, 18]
y12 = [19, 17, 19, 19]

plt.figure(facecolor='white')
plt.gca().set_facecolor('orange')

plt.plot(x5, y5, linewidth='5', color='black')
plt.plot(x4, y4, linewidth='5', color='black')
plt.plot(x, y, linewidth='5', color='black')
plt.plot(x3, y3, linewidth='5', color='black')
plt.plot(x1, y1, linewidth='10', color='black')
plt.plot(x2, y2, linewidth='10', color='black')
plt.plot(x6, y6, linewidth='5', color='white')
plt.plot(x7, y7, linewidth='5', color='white')
plt.plot(x8, y8, linewidth='20', color='white')
plt.plot(x9, y9, linewidth='20', color='white')
plt.plot(x10, y10, linewidth='5', color='black')
plt.plot(x11, y11, linewidth='5', color='black')
plt.plot(x12, y12, linewidth='5', color='black')

plt.show()