import time
import random
w = "you can't get smaller than 0 or bigger than 21"
print(w)
try:
    head = 10
    o = 0
    meaning1 = random.randint(-4, 4)
    meaning2 = random.randint(-4, 4)
    print('your main num is {}'.format(head))
    string = "{} or {}?: ".format(meaning1, meaning2)
    inp = input(string)
    for card in range(1,26):

        if int(inp) == meaning1:
            if head <= 0 or head >= 21:
                print('You failed!')
                break
            if card == 25:
                print("You won!")
            head = head + meaning1
            meaning1 = random.randint(-4, 4)
            
        elif int(inp) == meaning2:
            if head <= 0 or head >= 21:
                print('You failed!')
                break
            head = head + meaning2
            meaning2 = random.randint(-4, 4)
            if card == 25:
                print("You won!")
                break
        
        elif inp != meaning1 and meaning2:
            print("Нужно выбирать из данных чисел!")
            o = o + 1
            if o == 3:
                time.sleep(5)
                print("А я говорил...")
                break
        
        else:
            print('Wrong choice!! Programm breaks...')
            break

        print("position: {}".format(card + 1))
        string = "{} or {}?: ".format(meaning1, meaning2)
        print('your main num is {}'.format(head))
        inp = input(string)
        

except ValueError:
    if type(inp) != int():
        print("Я хотел другое...")
        time.sleep(1)
        print("Я тебя просил отдельное число!")
        time.sleep(1)
        print("А ты мне загогулину суёшь...")
        
    