import random
w = "you can't get 0 or smaller"
print(w)
head = 5
for card in range(0,25):
    print('your main num is {}'.format(head))
    meaning1 = random.randint(-6, 6)
    meaning2 = random.randint(-6, 6)
    string = "{} or {}?: ".format(meaning1, meaning2)
    inp = int(input(string))
    if inp == meaning1:
        head = head + meaning1
        if card == 24:
            print("You won!")
    elif inp == meaning2:
        head = head + meaning2
        if card == 24:
            print("You won!")
    elif head <= 0:
        print('You failed!')
        break
    else:
        print('Wrong choice!! Programm breaks...')
        break