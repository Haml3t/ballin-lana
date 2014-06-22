from attributes import VGR, END, VIT, ATN, STR, DEX, ADP, INT, FTH

class Performance_Calculator(object):
	def __init__(self, vit):
		self.vit = vit

	def get_equip_load(self):
		base_equip = 38.5
		return base_equip + self.get_equip_bonus()

	def get_equip_bonus(self, v):
		if v < 0:
			return None
		elif v <= 29:
			return 1.5 * v
		elif v <= 49:
			return self.get_equip_bonus(29) + (v-29)
		elif v <= 69:
			return self.get_equip_bonus(49) + 0.5*(v-49)
		else:
			return self.get_equip_bonus(69) + 0.5*(2*(0.25*(v-69))-2)

	def get_hp(self):
		base_hp = 500
		return base_hp +
				self.vgr_hp_gain(self.vgr) +
				self.low_hp_gain(self.end) +
				self.low_hp_gain(self.vit) +
				self.low_hp_gain(self.atn) +
				self.low_hp_gain(self.str) +
				self.low_hp_gain(self.dex) +
				self.low_hp_gain(self.adp) +
				self.low_hp_gain(self.int) +
				self.low_hp_gain(self.fth)

	def vgr_hp_gain(self, v):
		if v < 0:
			return None
		elif v <= 20:
			return 30 * v
		elif v < 50:
			return vgr_hp_gain(20) + 20*(v-20)
		else:
			return vgr_hp_gain(50) + 5*(v-50)

	def low_hp_gain(self, attribute):
		if attribute < 0:
			return None
		elif attribute <= 20:
			return 2 * attribute
		elif attribute <= 50:
			return self.low_hp_gain(20) + (attribute-20)
		else:
			return self.low_hp_gain(50)

	def get_stamina(self):
		pass

	
print 'HP = ' + str(HP(VGR, END, VIT, ATN, STR, DEX, ADP, INT, FTH))

def stamina(END):
	baseStamina = 80
	stamina = baseStamina + staminaBonus(END)
	return stamina

def staminaBonus(END):
	if END >= 0 and END <= 20:
		bonus = 2*END
		return bonus
	else:
		bonus = staminaBonus(20) + (END - 20)
		return bonus

print 'Stamina = ' + str(stamina(END))

def magicBNS(INT):
	
