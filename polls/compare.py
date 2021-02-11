import random
def compare(item, target):
    items_class=['common','uncommon','rare','super' 'legendary', 'arcane']
    perc = 0
    if item and target in items_class:
        if items_class.index(target) <= items_class.index(item):
            return "You can't do that!"
        else:
            if items_class.index(target) - items_class.index(item) == 1:
                perc = 50
            elif items_class.index(target) - items_class.index(item) == 2:
                perc = 25
            elif items_class.index(target) - items_class.index(item) == 3:
                perc = 12
            elif items_class.index(target) - items_class.index(item) == 4:
                perc = 6
            elif items_class.index(target) - items_class.index(item) == 5:
                perc = 3
    
    if random.randint(0, 100) <= perc:
        return "Succesfuly!"
    elif random.randint(0, 100) >= perc:
        return "Unluckily!"

if __name__ == "__main__":
    item = str(input("class of item('common','uncommon','rare', 'legendary', 'arcane'): "))
    target = str(input("class of target('common','uncommon','rare', 'legendary', 'arcane'): "))
    print(compare(item, target))