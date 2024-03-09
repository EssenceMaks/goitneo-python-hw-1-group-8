from datetime import datetime

def get_users_from_file(filename):
    users = []
    with open(filename, 'r') as file:
        for line in file:
            name, birthday_str = line.strip().split(', ')
            birthday = datetime.strptime(birthday_str, '%Y-%m-%d')
            users.append({"name": name, "birthday": birthday})
    return users

def get_birthdays_per_week(users):
    from collections import defaultdict
    
    today = datetime.now().date()
    birthdays_this_week = defaultdict(list)
    
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)
        
        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)
        
        delta_days = (birthday_this_year - today).days
        birthday_weekday = birthday_this_year.strftime('%A')
        
        # Перевіряємо, чи належить день народження до поточного місяця
        if birthday_this_year.month == today.month:
            if 0 <= delta_days < 7:
                birthdays_this_week[birthday_weekday].append(name)
    
    for day, names in birthdays_this_week.items():
        if names:
            print(f"{day}: {', '.join(names)}")

# Зчитуємо користувачів з файлу
filename = 'users.txt'
users = get_users_from_file(filename)

# Викликаємо функцію для обробки даних про користувачів
get_birthdays_per_week(users)