import threading
import time

def Timer(hours, minutes, secunds):
    if (0 <= hours*60 + minutes*60 + secunds ):
        isTime = True
        while(isTime):
            for secund in range(secunds):
                print(f"Осталось: {hours}:{minutes}:{secunds-secund}")
                time.sleep(1)
            print(f"Осталось: {hours}:{minutes}:0")
            time.sleep(1)
            if minutes != 0:
                secunds = 59
                minutes -= 1
                continue
            elif hours != 0:
                minutes = 59
                secunds = 59
                hours -= 1
            else:
                isTime = False
                print("Время вышло!")
    else:
        print("Wrong input!")

def Stopwatch(hours, minutes, secunds):
    allTimeInSecunds = hours * 60 + minutes * 60 + secunds
    if (0 <= allTimeInSecunds):
        isTime = True
        while (isTime):
            hoursLeft = 0
            minutesLeft = 0
            secundLeft = 0
            for i in range(allTimeInSecunds):
                print(f"Прошло: {hoursLeft}:{minutesLeft}:{secundLeft}\tиз {hours}:{minutes}:{secunds}")
                time.sleep(1)
                secundLeft += 1

                if secundLeft >= 60:
                    if minutesLeft >= 60:
                        hoursLeft += 1
                    else:
                        minutesLeft += 1
                        secundLeft = 0
                if i >= allTimeInSecunds - 1:
                    isTime = False
                    print("Время вышло!")
    else:
        print("Wrong input!")


#================================================== MAIN ==================================================
if __name__ == "__main__":
    hours = int(input("Введите сколько часов ждать: "))
    minutes = int(input("Введите сколько минут ждать: "))
    secunds = int(input("Введите сколько секунд ждать: "))

    timer = threading.Thread(target=Timer, args=(hours, minutes, secunds))
    stopwatch = threading.Thread(target=Stopwatch, args=(hours, minutes, secunds))

    choise = int(input("=> Включить таймер - нажмите '1'   |   Включить секундомер - нажмите '2'\nВаш выбор: "))
    if choise == 1:
        timer.start()
    elif choise == 2:
        stopwatch.start()
    else:
        print("Wrong input!")