from datetime import datetime

def get_days_from_today(date):
    """
    Обчислює кількість днів між заданою датою і поточною датою.
    
    :return: ціле число, яке вказує на кількість днів від заданої дати до поточної
    """
    try:
        # Перетворення рядка дати у об'єкт datetime
        target_date = datetime.strptime(date, '%Y-%m-%d')
        
        # Отримання поточної дати
        current_date = datetime.today()
        
        # Розрахунок різниці між датами
        delta = (current_date - target_date).days
        
        return delta
    except ValueError:
        # Обробка помилки, якщо формат дати неправильний
        print("Неправильний формат дати. Використовуйте 'РРРР-ММ-ДД'.")
        return None

# Приклад використання
result = get_days_from_today("2025-01-15")
if result is not None:
    print(f"Кількість днів від заданої дати до сьогодні: {result}")

# Додаткові тести
print(get_days_from_today("2025-01-19"))  # Від'ємне число, якщо сьогодні 18 січня 2025 року
print(get_days_from_today("2022-01-15"))  # Позитивне число, якщо сьогодні 18 січня 2025 року
print(get_days_from_today("2021-01-18"))  # Має повернути 0, якщо сьогодні 18 січня 2025 року
print(get_days_from_today("invalid-date"))  # Має вивести повідомлення про помилку