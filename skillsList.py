import random
import discord
from discord.ext.commands import Bot
bot = Bot(command_prefix='!') 
TOKEN = 'ODU4MDMxMjI3Mjk3NzI2NTA0.YNYN2g.Y7NiBR--GboIfHKX1IiW-ZWJCLY'

def multipleAttack(user, target):
    attackCount = 1
    if user.spd > target.spd:
        multipleAttackChance = user.spd - target.spd
        while multipleAttackChance > 1:
            multipleAttackCheck = random.randint(1, 100)
            if multipleAttackChance >= multipleAttackCheck:
                attackCount += 1
            else:
                break
            multipleAttackChance /= 2
    return attackCount

def crit(user, target):
    critMultiplier = 1
    if user.skl > target.luk:
        critChance = user.skl - target.luk
        while critChance > 1:
            critCheck = random.randint(1, 100)
            if critChance >= critCheck:
                critMultiplier += 0.5
            else:
                break
            critChance /= 2
    return critMultiplier

def miss(user, target):
    miss = False
    if user.skl < target.luk:
        missChance = (target.luk * 2) - (user.skl * 2)
        missCheck = random.randint(1, 100)
        if missChance >= missCheck:
            miss = True
    return miss

class Skill:
    def __init__(self, type, cooldown, name):
        self.type = type
        self.cooldown = 0
        self.maxCooldown = cooldown
        self.name = name

class BasicAttack (Skill):
    def __init__(self, name):
        super().__init__(0, 0, name)
    
    async def skill(self, user, target, party):
        channel = bot.get_channel(858035586564751390)
        critMod = crit(user, target)
        atkCount = multipleAttack(user, target)
        atkDmg = max(round((user.atk * 2 * critMod) - target.dfn),0)
        await channel.send(f"{user.name} used {self.name}!")
        if critMod != 1:
            await channel.send(f" x{critMod} Critical!")
        if atkCount != 1:
            await channel.send(f" {user.name} attacked {atkCount} times!")
        for i in range(atkCount):
            if miss(user, target) == False:
                target.hp -= atkDmg
                await channel.send(f" {target.name} took {atkDmg} damage!")
            else:
                await channel.send(f" {target.name} dodged...")
        self.cooldown = self.maxCooldown

class AbyssNova (Skill):
    def __init__(self):
        super().__init__(1, 3, "Abyss Nova")
    
    async def skill(self, user, target, party):
        channel = bot.get_channel(858035586564751390)
        target.atkChange1 += user.mag
        target.magChange1 += user.mag
        target.resChange1 -= user.mag
        await channel.send(f'{user.name} used Abyss Nova!')
        await channel.send (f' {target.name} gained {user.mag} ATK!')
        await channel.send (f' {target.name} gained {user.mag} MAG!')
        await channel.send (f' {target.name} lost {min(user.mag,target.res)} RES...')
        self.cooldown = self.maxCooldown

class RekindlingOfDeadAshes (Skill):
    def __init__(self):
        super().__init__(3, 3, "Rekindling of Dead Ashes")
    
    async def skill(self, user, target, party):
        channel = bot.get_channel(858035586564751390)
        preHp = target.hp
        if target.hp == 0:
            target.hp = min(target.hp + (user.mag * 2), target.maxHp)
        else:
            target.hp = min(target.hp + user.mag, target.maxHp)
        healed = target.hp - preHp
        await channel.send(f"{user.name} used Rekindling Of Dead Ashes!")
        await channel.send(f" {target.name} recovered {healed} HP!")
        self.cooldown = self.maxCooldown

class Supersonic (Skill):
    def __init__(self):
        super().__init__(2, 3, "Supersonic")
    
    async def skill(self, user, target, party):
        channel = bot.get_channel(858035586564751390)
        target.atkChange1 -= user.atk
        await channel.send(f'{user.name} uses Supersonic on {target.name}!')
        await channel.send(f' {target.name} lost {min(user.atk, target.atk)} ATK...')
        self.cooldown = self.maxCooldown

class QuickAttack (Skill):
    def __init__(self):
        super().__init__(0, 2, "Quick Attack")
    
    async def skill(self, user, target, party):
        channel = bot.get_channel(858035586564751390)
        user.spd *= 2
        critMod = crit(user, target)
        atkCount = multipleAttack(user, target)
        atkDmg = max(round((user.atk * 2 * critMod) - target.dfn),0)
        await channel.send(f"{user.name} used {self.name}!")
        if critMod != 1:
            await channel.send(f" x{critMod} Critical!")
        if atkCount != 1:
            await channel.send(f" {user.name} attacked {atkCount} times!")
        for i in range(atkCount):
            if miss(user, target) == False:
                target.hp -= atkDmg
                await channel.send(f" {target.name} took {atkDmg} damage!")
            else:
                await channel.send(f" {target.name} dodged...")
        self.cooldown = self.maxCooldown

class Sludge (Skill):
    def __init__(self):
        super().__init__(4, 3, "Sludge")

    async def skill(self, user, target, party):
        channel = bot.get_channel(858035586564751390)
        critMod = crit(user, target)
        atkCount = multipleAttack(user, target)
        await channel.send(f"{user.name} used {self.name}!")
        if critMod != 1:
            await channel.send(f" x{critMod} Critical!")
        if atkCount != 1:
            await channel.send(f" {user.name} attacked {atkCount} times!")
        for x in party:
            atkDmg = max(round((user.mag * 2 * critMod) - x.res),0)
            for i in range(atkCount):
                if miss(user, x) == False:
                    x.hp -= atkDmg
                    await channel.send(f" {x.name} took {atkDmg} damage!")
                else:
                    await channel.send(f" {x.name} dodged...")
        self.cooldown = self.maxCooldown

