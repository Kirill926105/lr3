day = int(input("Введите день месяца:")) # ввод данных
month = int(input("Введите месяц: "))
if month in (3, 4, 5): # определение времени года
    print("Весна")
elif month in (6, 7, 8):
        print("Лето")
elif month in (9, 10, 11):
        print("Осень")
else:
        print("Зима")