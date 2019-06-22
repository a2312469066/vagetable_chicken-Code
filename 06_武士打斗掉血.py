class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5
        self.is_alive = True
    def hurt(self,attack):
        self.health -= attack
        if self.health < 0:
            self.is_alive = False
class Knight(Warrior):
    def __init__(self):
        self.health = 50
        self.attack = 7
        self.is_alive = True

def fight(unit_1, unit_2):
    while unit_1.is_alive == True and unit_2.is_alive == True:

        unit_2.hurt(unit_1.attack)

        if unit_1.is_alive == True and unit_2.is_alive == False:
            return True
        if unit_1.is_alive == False and unit_2.is_alive == True:
            return False

        unit_1.hurt(unit_2.attack)

        if unit_1.is_alive == True and unit_2.is_alive == False:
            return True
        if unit_1.is_alive == False and unit_2.is_alive == True:
            return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    print("Coding complete? Let's try tests!")
