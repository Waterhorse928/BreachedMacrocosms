import random
import charactersMaster
import skillsList

class Rattata(charactersMaster.Character):
    def __init__(self):
        super().__init__(1, 0, 15, 20, 0, 10, 20, 10, 15, 15, True, "Rattata")
        self.skillList.append(skillsList.BasicAttack(0,'Tackle'))
        self.skillList.append(skillsList.QuickAttack(1,"Quick Attack"))

class Zubat(charactersMaster.Character):
    def __init__(self):
        super().__init__(1, 0, 10, 10, 10, 15, 15, 25, 10, 10, True, 'Zubat')
        self.skillList.append(skillsList.BasicAttack(0,'Astonish'))
        self.skillList.append(skillsList.Supersonic(2,"Supersonic"))

class Muk(charactersMaster.Character):
    def __init__(self):
        super().__init__(1, 0, 20, 10, 15, 10, 5, 5, 20, 20, True, 'Muk')
        self.skillList.append(skillsList.BasicAttack(0,'Pound'))
        self.skillList.append(skillsList.Sludge(2,"Sludge"))

class Pirate(charactersMaster.Character):
    def __init__(self, name):
        super().__init__(1, 0, 15, 15, 10, 20, 15, 15, 15, 15, True, name)
        self.skillList.append(skillsList.BasicAttack(0,"Slash"))
        self.skillList.append(skillsList.WatchOut(2,"Watch Out"))
        self.skillList.append(skillsList.Shoot(2,"Shoot"))

class Beowolf(charactersMaster.Character):
    def __init__(self, name):
        super().__init__(1, 0, 15, 15, 15, 15, 15, 15, 15, 15, True, name)
        self.skillList.append(skillsList.BasicAttack(0,"Lunge"))
        self.skillList.append(skillsList.Howl(2,"Howl"))
        self.skillList.append(skillsList.Maul(2,"Maul"))

class AlphaBeowolf(charactersMaster.Character):
    def __init__(self, name):
        super().__init__(3, 0, 30, 30, 15, 20, 20, 15, 15, 10, True, name)
        self.skillList.append(skillsList.BasicAttack(0,"Tear"))
        self.skillList.append(skillsList.Sludge(1, "Piercing Howl"))
        self.skillList.append(skillsList.Savage(3, "Savage"))

class Arbok(charactersMaster.Character):
    def __init__(self, name):
        super().__init__(3, 0, 20, 20, 5, 15, 15, 30, 20, 15, True, name) # Total Stats: 140
        self.skillList.append(skillsList.BasicAttack(0,"Headbutt"))
        self.skillList.append(skillsList.Wrap(2,"Wrap"))
        self.skillList.append(skillsList.Acid(2,"Acid"))
        self.skillList.append(skillsList.PoisonSting(2,"Poison Sting"))

class Wheezing(charactersMaster.Character):
    def __init__(self, name):
        super().__init__(3, 0, 30, 15, 30, 15, 10, 5, 25, 10, True, name) # Total Stats: 140
        self.skillList.append(skillsList.BasicAttack(0,"Tackle"))
        self.skillList.append(skillsList.Smokescreen(2,"Smokescreen"))
        self.skillList.append(skillsList.Sludge(2,"Sludge"))
        self.skillList.append(skillsList.Smog(2,"Smog"))

class Meowth(charactersMaster.Character):
    def __init__(self, name):
        super().__init__(3, 0, 20, 25, 5, 30, 30, 20, 10, 0, True, name) # Total Stats: 140
        self.skillList.append(skillsList.BasicAttack(0,"Scratch"))
        self.skillList.append(skillsList.FurySwipes(2, "Fury Swipes"))
        self.skillList.append(skillsList.Shoot(2, "Bite"))
        self.skillList.append(skillsList.DarkStar(2, "Pep Talk"))

class Wobbuffet(charactersMaster.Character):
    def __init__(self, name):
        super().__init__(4, 0, 50, 0, 0, 0, 10, 10, 40, 35, True, name) # Total Stats: 145
        self.skillList.append(skillsList.BasicAttack(0,"Salute"))
        self.skillList.append(skillsList.ShadowTag(5, "Shadow Tag"))
        self.skillList.append(skillsList.Counter(0, "Counter"))
        self.skillList.append(skillsList.MirrorCoat(0, "Mirror Coat"))
        self.skillList.append(skillsList.Bide(2, "Bide"))

class Mimikyu(charactersMaster.Character):
    def __init__(self, name):
        super().__init__(5, 0, 20, 25, 15, 25, 25, 20, 15, 25, True, name) # Total Stats: 170
        self.skillList.append(skillsList.BasicAttack(0,"Play Rough"))
        self.skillList.append(skillsList.MagicMissile(0,"Shadow Ball"))
        self.skillList.append(skillsList.ShadowClaw(1,"Shadow Claw"))
        self.skillList.append(skillsList.Savage(2,"Wood Hammer"))
        self.skillList.append(skillsList.SnuggleForever(5,"Let's Snuggle Forever"))
    
class Victreebel(charactersMaster.Character):
    def __init__(self, name):
        super().__init__(3, 0, 35, 15, 15, 20, 10, 10, 15, 10, True, name) # Total Stats: 130
        self.skillList.append(skillsList.BasicAttack(0,"Vine Whip"))
        self.skillList.append(skillsList.Shoot(3,"Razor Leaf"))
        self.skillList.append(skillsList.Wrap(3,"Wrap"))
        self.skillList.append(skillsList.SleepPowder(1,"Sleep Powder"))
        self.skillList.append(skillsList.SwordsDance(1,"Swords Dance"))
        self.skillList.append(skillsList.Maul(3,"Double-Edge"))

class Yamask(charactersMaster.Character):
    def __init__(self, name):
        super().__init__(4, 0, 15, 10, 30, 15, 15, 15, 30, 15, True, name) # Total Stats: 145
        self.skillList.append(skillsList.BasicAttack(0,"Astonish"))
        self.skillList.append(skillsList.MagicMissile(0, "Shadow Ball"))
        self.skillList.append(skillsList.Smokescreen(2,"Haze"))
        self.skillList.append(skillsList.NightShade(3,"Night Shade"))
        self.skillList.append(skillsList.Wisp(2,"Will-O-Wisp"))

class Morgan(charactersMaster.Character):
    def __init__(self, name):
        super().__init__(5, 0, 50, 30, 5, 15, 20, 20, 20, 10, True, name) # Total Stats: 170
        self.skillList.append(skillsList.BasicAttack(0,"Chop"))
        self.skillList.append(skillsList.Savage(2,"Overhead Chop"))
        self.skillList.append(skillsList.Cleave(2,"Cleave"))
        self.skillList.append(skillsList.DarkStar(2, "Threaten"))

beowolf1 = {1:Beowolf("Beowolf A"),2:Beowolf("Beowolf B")}
beowolf2 = {1:Beowolf("Beowolf A"),2:Beowolf("Beowolf B"),3:Beowolf("Beowolf C")}
beowolf3 = {1:Beowolf("Beowolf A"),3:Beowolf("Beowolf B"),2:AlphaBeowolf("Alpha Beowolf")}
rocket1 = {1:Rattata(),2:Zubat(),3:Muk()}
rocket2 = {1:Arbok("Arbok"),2:Meowth("Meowth"),3:Wheezing("Wheezing")}
rocket3 = {1:Wobbuffet("Wobbuffet"),2:Mimikyu("Mimikyu"),3:Victreebel("Victreebel"),4:Yamask("Yamask")}
pirate1 = {1:Pirate("Pirate A"),2:Pirate("Pirate B"),3:Pirate("Pirate C")}
pirate2 = {1:Pirate("Pirate A"),2:Pirate("Pirate B"),3:Pirate("Pirate C"),4:Pirate("Pirate D"),5:Pirate("Pirate E")}
pirate3 = {1:Pirate("Pirate A"),2:Pirate("Pirate B"),3:Morgan("Morgan Axe-hand"),4:Pirate("Pirate C"),5:Pirate("Pirate D")}