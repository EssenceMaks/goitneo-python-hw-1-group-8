from datetime import datetime  # Импортируем необходимые библиотеки

def get_users_from_file(filename):         # Функция для чтения пользователей из файла и преобразования их в список словарей
    users = []                             # Создаем пустой список для хранения пользователей
    with open(filename, 'r') as file:      # Открываем файл на чтение
        for line in file:                  # Проходим по каждой строке файла                     
            name, birthday_str = line.strip().split(', ')          # Разделяем строку по запятой и преобразуем в список, содержащий имя и дату рождения
            birthday = datetime.strptime(birthday_str, '%Y-%m-%d') # Преобразуем строку даты рождения в объект datetime и добавляем в список пользователей
            users.append({"name": name, "birthday": birthday})     
    return users                                                   # Возвращаем список пользователей

def get_birthdays_per_week(users):         # Функция для определения и вывода дней рождений пользователей на текущей неделе
    today = datetime.now().date()          
    birthdays_this_week = {'Monday': [], 'Tuesday': [], 'Wednesday': [],      # Создаем словарь для хранения именниников 
                           'Thursday': [], 'Friday': [], 'Saturday': [], 'Sunday': []}  
    
    for user in users:                                           # Проходим по каждому пользователю из списка
        name = user["name"]                                      # Получаем имя пользователя
        birthday = user["birthday"].date()                       # Получаем дату рождения пользователя  
        birthday_this_year = birthday.replace(year=today.year)   # Устанавливаем текущий год для даты рождения
        
        if birthday_this_year < today:                           # Если день рождения уже прошел в текущем году, устанавливаем его на следующий год
            birthday_this_year = birthday.replace(year=today.year + 1)
        
        delta_days = (birthday_this_year - today).days           # Вычисляем разницу в днях между текущей датой и днем рождения
        birthday_weekday = birthday_this_year.strftime('%A')     # Получаем название дня недели для дня рождения
        
        
        if 0 <= delta_days < 7:                                  # Если день рождения находится в пределах текущей недели или был вчера               
            if birthday_weekday in ['Saturday', 'Sunday']:       # Если день рождения выпадает на ЭТУ субботу или воскресенье
                if 'Next Monday' not in birthdays_this_week:
                    birthdays_this_week['Next Monday'] = []
                birthdays_this_week['Next Monday'].append(name + f' (from {birthday_weekday})') # Выводи имя в ГРЯДУЩИЙ понедельник
            else:
                birthdays_this_week[birthday_weekday].append(name)
        
        
        elif delta_days == 7:           # Если день рождения выпадает на ЭТУ субботу или воскресенье
            if 'Next Monday' not in birthdays_this_week:
                birthdays_this_week['Next Monday'] = []
            birthdays_this_week['Next Monday'].append(name + f' (will be on {birthday_weekday})') # Выводи имя в будущий понедельник
    
    for day, names in birthdays_this_week.items():  # Выводим список именниников на текущей неделе
        if names:
            print(f"{day}: {', '.join(names)}")

filename = 'users.txt'                  # Имя файла с данными о пользователях
users = get_users_from_file(filename)   # Получаем список пользователей из файла

get_birthdays_per_week(users)