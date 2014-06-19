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
		bonus - equipBonus(69) + .5*(2*(.25*(VIT-69))-2)
	return bonus

print equipLoad(VIT)

def 
