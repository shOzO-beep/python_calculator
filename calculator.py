from time import sleep

while True:
    sleep(1)
    print("1:+")
    print("2:-")
    print("3:/")
    print("4:*")
    print("0:Выход")
    user = int(input("Выбери действие:"))

    try:

        if user == 0:
              print("Закрытие калькулятора")
              sleep(1)
              break

        if user not in (0,1,2,3,4):
              print("Выберите цифру от 0 до 4")
              continue
        print("Введите числа")
        number1 = float(input("Цифра1:"))
        number2 = float(input("Цифра2:"))

        if user == 1:
                result = number1+number2           
        elif user == 2:
                result = number1-number2          
        elif user == 3:
                result = number1/number2          
        elif user == 4:
                result = number1*number2 

        print(result)

    except ValueError:
        print("Нужно писать цифры!")
            
    except ZeroDivisionError:
        print("На ноль делить нельзя!")