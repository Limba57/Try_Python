from main.classInPython.Test import Test

'''

this is a comment
block

'''

# this a single line comment


class Enemy():

    def __init__(self, atkl: int, atkh: int):
        self.atkl = atkl
        self.atkh = atkh

    def get_atk(self):
        print(self.atkl)

    def get_damage_range(self):
        print(self.atkh-self.atkl)


enemy1 = Enemy(60, 80)
enemy1.get_atk()

enemy2 = Enemy(80, 100)
enemy2.get_atk()
enemy2.get_damage_range()

test = Test("Seb")
test.hello()



