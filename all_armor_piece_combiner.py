import json
from pprint import pprint

#imports jsons into dicts
json_data = open('armor_head.json')
headDict = json.load(json_data)
json_data.close()

json_data = open('armor_arms.json')
armsDict = json.load(json_data)
json_data.close()

json_data = open('armor_chest.json')
chestDict = json.load(json_data)
json_data.close()

json_data = open('armor_legs.json')
legsDict = json.load(json_data)
json_data.close()

def combination(headPiece, armsPiece, chestPiece, legsPiece, ID):
	pieces = [headPiece, armsPiece, chestPiece, legsPiece]
	setName = []
	armorSet = {'head': headPiece, 'arms': armsPiece, 'chest': chestPiece, 'legs': legsPiece, 'ID': ID, 'name': setName, 'totalPerformance': {}}
	sumList = ['Curse', 'Poison', 'Effect', 'Prerequisite', 'Dark', 'Phys', 'Fire', 'Poise', 'Scaling', 'Mag', 'Bleed', 'Light', 'Sls', 'Str', 'Total Defense', 'Weight', 'Petrify']
	for h in headPiece:
		if h == 'Name':
			for p in pieces:
				setName.append(p[h])
		if h in sumList:
			if not isinstance(headPiece[h], basestring):
				armorSet['totalPerformance'][h] = 0
			else:
				armorSet['totalPerformance'][h] = ""
			for p in pieces:
				if h in p:
					armorSet['totalPerformance'][h] = armorSet['totalPerformance'][h] + p[h]
	return armorSet
"""	
def allCombinations(headDict, armsDict, chestDict, legsDict):
	ID = 0
	for h in headDict:
		for a in armsDict:
			for c in chestDict:
				for l in legsDict:
					ID += 1
					amorSet = combination(h, a, c, l, ID)
					
"""

print len(headDict)
print len(armsDict)
print len(chestDict)
print len(legsDict)
print len(headDict)*len(armsDict)*len(chestDict)*len(legsDict)
testHead = headDict['Ironclad Helm']
testArms = armsDict['Ironclad Gauntlets']
testChest = chestDict['Ironclad Armor']
testLegs = legsDict['Ironclad Leggings']

testCombo = combination(testHead, testArms, testChest, testLegs, 000000)
print 'Head = '
print testCombo['head']
print 'Full Set = ' + str(testCombo['name'])
print testCombo['totalPerformance']


