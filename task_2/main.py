x = float(input("Введите число x:")) # вводим число x
y = float(input("Введите число y:")) # вводим число y
print(y) if x > y else (print(x) if y > x else print("x=y")) # выводим число y, если x > y, иначе выводим  x, если y > x, иначе x=y