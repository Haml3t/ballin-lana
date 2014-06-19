import csv, json
import re
from config import ARMOR_CSV, ARMOR_JSON, string_header_values

mainArmor = {}
def makePieceDict(values):
	global header
	armorPiece = {}
	for i in range(len(header)):
		if values[i] and i > 0:			
			if header[i] in string_header_values:
				armorPiece[header[i]] = values[i]
				
			else:
				armorPiece[header[i]] = float(values[i])
	return armorPiece

with open(ARMOR_CSV, 'r') as armorCsv:
	global header
	armorReader = csv.reader(armorCsv, dialect='excel')
	isFirstRow = True
	for row in armorReader:
		if isFirstRow:
			header = row
			isFirstRow = False
		
		armorName = row[0]
		if re.match('.+\+\d+.*',armorName):
			pieceStrings = armorName.split('+')
			armorName = pieceStrings[0]
			numbers = []
			for num in pieceStrings[1].split():
				if num.isdigit():
					numbers.append(num)
			reinforcement = int(numbers[0])
			
			if armorName in mainArmor:
				if reinforcement > mainArmor[armorName]["Reinforcement Value"]:
					mainArmor[armorName] = makePieceDict(row)
					mainArmor[armorName]["Reinforcement Value"] = reinforcement
			else:
				mainArmor[armorName] = makePieceDict(row)
				mainArmor[armorName]["Reinforcement Value"] = reinforcement	
			

with open(ARMOR_JSON, 'w') as fp:
	json.dump(mainArmor,fp)
