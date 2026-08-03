import logging
from characters import Character

logger = logging.getLogger(__name__)

class Battle():
    def __init__(self,attacker,target):
        self.attacker = attacker
        self.target = target

    def start(self):
        while self.attacker.is_alive() and self.target.is_alive():
            self.attacker.attack_enemy(self.target)
            logger.info(f"{self.attacker} damaged enemy")
            if not self.target.is_alive():
                logger.info(f"{self.attacker} wins the battle")
            self.target.attack_enemy(self.attacker)
            logger.info(f"{self.target} damaged attacker")
            if not self.attacker.is_alive():
                logger.info(f"{self.target} wins the battle")