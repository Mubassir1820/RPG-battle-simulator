import logging
logging.basicConfig(level=logging.INFO,format="%(asctime)s - %(levelname)s - %(message)s")

from characters import Character,Warrior,Mage,Archer
from battle import Battle

warrior1 = Warrior()
mage1 = Mage()
archer1 = Archer()

battle = Battle(mage1,archer1)
logging.info(battle.start())