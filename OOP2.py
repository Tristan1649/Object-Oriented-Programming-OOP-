from time import sleep
class Ak47:
    def __init__(self, title, numbe_bullet) -> None:
        self.title = title
        self.bullet = numbe_bullet
        self.numbe_bullet = numbe_bullet
    
    def gun(self):
        if self.bullet == 0:
            print('No bullets!')
        for i in range(1,self.bullet+1):
            print(i, 'Shot -->')
            self.bullet -= 1
            sleep(0.05)
            if i % 3 == 0:
                sleep(1)
    
    def change_mag(self):
        self.bullet = self.numbe_bullet
s1 = Ak47('Ak14', 26)
class Soldier:
    def __init__(self, name, rank, weapon, mag) -> None:
        self.name = name
        self.rank = rank 
        self.weapon = weapon
        self.mag = mag
    
    def atak(self):
        while self.mag != 0:
            print('Ready to fire!')
            self.weapon.gun()
            print('I am reloading!!! Cover me!')
            self.weapon.change_mag()
            sleep(3)
            self.mag -= 1
s = Soldier('Trooper', 'sergant', s1, 3) 
s.atak()