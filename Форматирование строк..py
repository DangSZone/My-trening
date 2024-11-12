# # Конкотенация - сложение строк
# print('Hello, ' + 'world!')
#
# # При конкотенации строки и другого типа объекта мы получим ошибку.
# # Складывать можно только строки
#
# # Устаревшее форматирование строки с помощью "'s%' %":
# print('Меня зовут %s, мне %d' % ('Денис', 14))
# print('Меня зовут %(name)s, мне %(year)d' % {'name': 'Денис', 'year': 14})
#
# # На смену этому форматированию пришло новое через .format()
# print('Hello, i am {title} {postix} {title}'.format(title='DeeZ',postix= 14))
#
# # Самый новейший это f'{}':
# x = 'Urban'
# print(f'{x * 2} это лучший университет')

team1_name = 'Мастера кода'
team2_name = 'Волшебники данных'
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 10717.6
team2_time = 18015.2
task_total = f'{score_1 + score_2}'
wining_ = 'победа команды:'
challenge_result = f'{wining_} {team1_name}'
task_avg = round((team1_time + team2_time) / (score_1 + score_2), 2)


# Использование %:
print('В команде Мастера кода участников: %s' % team1_num)
print("Итого сегодня в командах участников: %s и %s" % (team1_num, team2_num))

# Использование format():
print("Команда Волшебники данных решила задач: {score_2}!".format(score_2 = 2))
print("Волшебники данных решили задачи за {team2_time} с !".format(team2_time=18015.2))

# Использование f-строк:
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы {challenge_result}')
print(f"Сегодня было решено {score_1 + score_2} задач, в среднем по {task_avg} секунды на задачу!.")



