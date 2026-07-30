from characters import Character

class Battle():
    def __init__(self,attacker,target):
        self.attacker = attacker
        self.target = target

    def start(self):
        while self.attacker.is_alive() and self.target.is_alive():
            self.attacker.attack_enemy(self.target)
            if not self.target.is_alive():
                return (f"{self.attacker} wins the battle")
            self.target.attack_enemy(self.attacker)
            if not self.attacker.is_alive():
                return (f"{self.target} wins the battle")