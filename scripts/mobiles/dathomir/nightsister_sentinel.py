import sys
from services.spawn import MobileTemplate
from services.spawn import WeaponTemplate
from java.util import Vector

def addTemplate(core):
	mobileTemplate = MobileTemplate()
	
	mobileTemplate.setCreatureName('nightsister_sentinal')
	mobileTemplate.setLevel(80)
	mobileTemplate.setDifficulty(1)
	mobileTemplate.setAttackRange(6)
	mobileTemplate.setAttackSpeed(1.0)
	mobileTemplate.setWeaponType(4)
	mobileTemplate.setMinSpawnDistance(4)
	mobileTemplate.setMaxSpawnDistance(6)
	mobileTemplate.setDeathblow(True)
	mobileTemplate.setSocialGroup('nightsister')
	mobileTemplate.setAssistRange(12)
	mobileTemplate.setRespawnTime(300)
	mobileTemplate.setOptionsBitmask(192)
	
	templates = Vector()
	templates.add('object/mobile/shared_dressed_dathomir_nightsister_sentinal.iff')
	mobileTemplate.setTemplates(templates)
	
	weaponTemplates = Vector()
	weapontemplate = WeaponTemplate('object/weapon/melee/sword/shared_sword_01.iff', 4, 1.0)
	weaponTemplates.add(weapontemplate)
	mobileTemplate.setWeaponTemplateVector(weaponTemplates)
	
	attacks = Vector()
	mobileTemplate.setDefaultAttack('meleehit')
	mobileTemplate.setAttacks(attacks)
	
	lootPoolNames_1 = ['Junk']
	lootPoolChances_1 = [100]
	lootGroupChance_1 = 65
	mobileTemplate.addToLootGroups(lootPoolNames_1,lootPoolChances_1,lootGroupChance_1)
	
	lootPoolNames_2 = ['jedi_relic_1']
	lootPoolChances_2 = [100]
	lootGroupChance_2 = 85
	mobileTemplate.addToLootGroups(lootPoolNames_2,lootPoolChances_2,lootGroupChance_2)
	
	lootPoolNames_4 = ['random_stat_jewelry']
	lootPoolChances_4 = [100]
	lootGroupChance_4 = 8
	mobileTemplate.addToLootGroups(lootPoolNames_4,lootPoolChances_4,lootGroupChance_4)

	lootPoolNames_5 = ['sithholocrons']
	lootPoolChances_5 = [100]
	lootGroupChance_5 = 3
	mobileTemplate.addToLootGroups(lootPoolNames_5,lootPoolChances_5,lootGroupChance_5)
	
	core.spawnService.addMobileTemplate('nightsister_sentinal', mobileTemplate)