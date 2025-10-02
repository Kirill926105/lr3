correct_password = "secret123" # задаем правильный пароль
user_password = input("Введите пароль: ") #  ввод пароля от пользователя
if user_password == correct_password: # если пароль совпадает, то доступ разрешен
    print("Доступ разрешен")
else: # иначе, доступ запрещен
        print("Доступ запрещен")
