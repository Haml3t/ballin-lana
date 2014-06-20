from attributes import VGR, END, VIT, ATN, STR, DEX, ADP, INT, FTH



def equipLoad(VIT):
	baseEquip = 38.5
	equip = baseEquip + equipBonus(VIT)
	return equip

def equipBonus(VIT):
	if VIT >= 0 and VIT <= 29:
		bonus = 1.5*VIT
	elif VIT >= 30 and VIT <= 49:
		bonus = equipBonus(29) + (VIT-29)
	elif VIT >= 50 and VIT <= 69:
		bonus = equipBonus(49) + 0.5*(VIT-49)
	else:
		bonus = equipBonus(69) + .5*(2*(.25*(VIT-69))-2)
	return bonus

print 'Equip Load = ' + str(equipLoad(VIT))

def HP(VGR, END, VIT, ATN, STR, DEX, ADP, INT, FTH):
	baseHP = 500
	HP = baseHP + VGRHPGain(VGR) + lowHPGain(END) + lowHPGain(VIT) + lowHPGain(ATN) + lowHPGain(STR) + lowHPGain(DEX) + lowHPGain(ADP) + lowHPGain(INT) + lowHPGain(FTH)
	return HP

def VGRHPGain(VGR):
	if VGR >= 0 and VGR <= 20:
		bonus = 30*VGR
	elif VGR >= 21 and VGR <= 50:
		bonus = VGRHPGain(20) + 20*(VGR-20)
	else:
		bonus = VGRHPGain(50) + 5*(VGR-50)
	return bonus
	
def lowHPGain(attribute):
	if attribute >= 0 and attribute <= 20:
		bonus = 2*attribute
	elif attribute >= 21 and attribute <= 50:
		bonus = lowHPGain(20) + (attribute-20)
	else:
		bonus = lowHPGain(50)
	return bonus
	
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
	
