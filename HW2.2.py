user_input = input ("Введите 5-значное число ")
number = int(user_input)

print(number % 10, number // 10 % 10, number // 100 % 10, number //1000 % 10, number //10000)
