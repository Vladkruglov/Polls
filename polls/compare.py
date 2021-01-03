import random
def compare(item, target):
    items_class=['common','uncommon','rare','super' 'legendary', 'arcane']
    perc = 0
    if item and target in items_class:
        if items_class.index(target) <= items_class.index(item):
            return False
        else:
            if items_class.index(target) - items_class.index(item) == 1:
                perc = 75
            elif items_class.index(target) - items_class.index(item) == 2:
                perc = 50
            elif items_class.index(target) - items_class.index(item) == 3:
                perc = 25
            elif items_class.index(target) - items_class.index(item) == 4:
                perc = 12
            elif items_class.index(target) - items_class.index(item) == 5:
                perc = 6
    
    if random.randint(0, 100) <= perc:
        return True
    elif random.randint(0, 100) >= perc:
        return False

if __name__ == "__main__":
    item = str(input("class of item('common','uncommon','rare', 'legendary', 'arcane'): "))
    target = str(input("class of target('common','uncommon','rare', 'legendary', 'arcane'): "))
    print(compare(item, target))