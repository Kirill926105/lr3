# Ввод даты
day = int(input("Введите день: "))
month = int(input("Введите месяц: "))

# Проверка даты
if month < 1 or month > 12:
    print("Ошибка: месяц должен быть от 1 до 12")
elif day < 1 or day > 31:
    print("Ошибка: день должен быть от 1 до 31")
else:
    # Проверка дней в месяце
    if (month == 2 and day > 28) or ((month == 4 or month == 6 or month == 9 or month == 11) and day > 30):
        print("Ошибка: в этом месяце нет столько дней")
    else:
        # Определение сезона
        if (month == 3) or (month == 4) or (month == 5):
            season = "Весна"
        elif (month == 6) or (month == 7) or (month == 8):
            season = "Лето"
        elif (month == 9) or (month == 10) or (month == 11) or (month == 11):
            season = "Осень"
        else:
            season = "Зима"
        
        print(f"Дата {day}.{month} относится к времени года: {season}")