import random

class Enemy:
    hp=200
    # instance variable
    def __init__(self,atkl,atkh):
        self.atkl=atkl
        self.atkh=atkh

    def getAtk(self):
        print(self.atkl)

    def get_hp(self):
        print("HP is: ",self.hp)

enemy1=Enemy(100, 120)
enemy1.getAtk()
enemy1.get_hp()

enemy2 = Enemy(40,50)
enemy2.getAtk()
enemy2.get_hp()


'''
playerhp = 250
enemyatkl = 60
enemyatkh = 80


while playerhp > 0:
    dmg = random.randrange(enemyatkl,enemyatkh)
    playerhp=playerhp-dmg

    if playerhp<=30:
        playerhp=30
    
    print("Enemy strikes for", dmg, "points of damage.  Current HP is",playerhp)

    if playerhp==30:
        continue

    print("you have died.")
    break'''