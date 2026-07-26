from abc import ABC
from config.stats import CHARACTER_STATS

class Character(ABC):
    def __init__(self, hero,max_health,current_health,attack,defense,max_mana,current_mana):
        self.hero_type = hero
        self.max_health = max_health
        self.current_health = current_health
        self.attack = attack
        self.defense = defense
        self.max_mana = max_mana
        self.current_mana = current_mana

    def attack_enemy(self,target):
        damage = max(1,self.attack - target.defense)
        return damage

    def take_damage(self,damage):
        rem_health = self.current_health - damage
        self.current_health = max(0,rem_health)
        return self.current_health
    
    def is_alive(self):
        if self.current_health <= 0:
            return False
        return True

    
class Warrior(Character):
    def __init__(self):
        stats = CHARACTER_STATS['Warrior']
        super().__init__(
            hero="warrior",
            max_health=stats["health"],
            current_health=stats["health"],
            attack=stats["attack"],
            defense=stats["defense"],
            max_mana=stats["mana"],
            current_mana=stats["mana"])

class Mage(Character):
    def __init__(self):
        stats = CHARACTER_STATS["Mage"]
        super().__init__(
            hero="Mage",
            max_health=stats["health"],
            current_health=stats["health"],
            attack=stats["attack"],
            defense=stats["defense"],
            max_mana=stats["mana"],
            current_mana=stats["mana"])

class Archer(Character):
    def __init__(self):
        stats = CHARACTER_STATS["Archer"]
        super().__init__(
            hero="Archer",
            max_health=stats["health"],
            current_health=stats["health"],
            attack=stats["attack"],
            defense=stats["defense"],
            max_mana=stats["mana"],
            current_mana=stats["mana"])

warrior1 = Warrior()
mage1 = Mage()

damage = warrior1.attack_enemy(mage1)
print(warrior1.attack_enemy(mage1))
print(mage1.take_damage(damage))
print(mage1.is_alive())
print(warrior1.attack_enemy(mage1))
print(mage1.is_alive())
print(warrior1.attack_enemy(mage1))
print(mage1.is_alive())
print(warrior1.attack_enemy(mage1))
print(mage1.is_alive())
print(warrior1.attack_enemy(mage1))
print(mage1.is_alive())
print(warrior1.attack_enemy(mage1))
print(mage1.is_alive())