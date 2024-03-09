from datetime import datetime, timedelta

def parse_birthdays_file(filename):
    users = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 2:
                name, birthday_str = parts
                birthday = datetime.strptime(birthday_str.strip(), "%Y-%m-%d")
                users.append({"name": name.strip(), "birthday": birthday})
    return users

def get_birthdays_per_week(users):
    today = datetime.today().date()
    # Створюємо словник для зберігання ім'янних списків по днях тижня
    birthdays_per_week = {}
    
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        delta_days = (birthday_this_year - today).days
        
        day_of_week = (today + timedelta(days=delta_days)).strftime('%A')
        if day_of_week in ['Saturday', 'Sunday']:
            day_of_week = 'Monday'
        
        # Якщо день тижня вже є в словнику, додаємо ім'я до списку, інакше створюємо новий список
        if day_of_week in birthdays_per_week:
            birthdays_per_week[day_of_week].append(name)
        else:
            birthdays_per_week[day_of_week] = [name]
    
    return birthdays_per_week

def print_birthdays(birthdays_per_week):
    for day, names in birthdays_per_week.items():
        print(f"{day}: {', '.join(names)}")

# Шлях до текстового файлу з даними
filename = "users.txt"

# Отримуємо дані з файлу
users = parse_birthdays_file(filename)

# Отримуємо список днів народження на наступному тижні
birthdays_per_week = get_birthdays_per_week(users)

# Виводимо результат
print_birthdays(birthdays_per_week)