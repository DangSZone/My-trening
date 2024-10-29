from time import sleep


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class UrTube:
    users = None
    videos = []
    current_user = None

    def register(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age
        if UrTube.users is None:
            UrTube.users = []
            UrTube.users.append(User(nickname, hash(password), age))
            UrTube.log_in(self, nickname, password)
            print(f'{nickname}, успешно зарегистрирован')
        else:
            for a in UrTube.users:
                if nickname != a.nickname:
                    UrTube.users.append(User(nickname, hash(password), age))
                    UrTube.log_in(self, nickname, password)
                    print(f'{nickname}, успешно зарегистрирован')
                    break
                else:
                    print(f"Пользователь {nickname} уже существует")
                    break

    def log_in(self, nickname, password):
        self.nickname = nickname.lower
        password =hash(password)
        for i in UrTube.users:
            if i.nickname == nickname and  i.password == hash(password):
                UrTube.current_user = i
                break
            else:
                continue

    def log_out(self, nickname):
        self.nickname = nickname
        if UrTube.current_user.nickname == nickname:
            UrTube.current_user = None
        else:
            print('Недоступно')

    def add(self, *args):
        for i in args:
            if not any(v.title == i.title for v in self.videos):
                self.videos.append(i)

    def get_videos(self, name):
        list_ = []
        self.name = name
        for t_ in UrTube.videos:
            dict_ = t_.__dict__
            tit_ = str(dict_['title']).lower()
            if name.lower() in tit_:
                list_.append(dict_['title'])
        return list_

    def watch_video(self, name):
        time = []
        self.name = name
        for a in UrTube.videos:
            if name != a.title:
                continue
            else:
                if UrTube.current_user == None:
                    print('Пожалуйста войдите в аккаунт')
                    break
                elif a.adult_mode == True and UrTube.current_user.age >= 18:
                    sleep(a.duration)
                    for sec in range(a.duration+1):
                        time.append(sec)
                    print(f'{time} Конец видео.')
                else:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    break



ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')











