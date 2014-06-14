import csv
import re
import json

mainHead = {}
def makeHeadPieceDict(values,header):
	headPiece = {}
	for i in range(len(header)):
		if values[i]:
			
			if i == 0:
				plusIndex = values[0].find('+')
				name = values[0][:plusIndex]
				headPiece[header[i]] = name
			else:
				headPiece[header[i]] = values[i]
	return headPiece

with open('Dark Souls 2 Armor - Head.csv', 'r') as armorCsv:
	armorReader = csv.reader(armorCsv, dialect='excel')
	isFirstRow = True
	for row in armorReader:
		if isFirstRow:
			header = row
			isFirstRow = False
		elif re.match('.+\+\d+.*',row[0]):
			"""
			if row[0] in mainHead:
				if row[0] == 'Dingy Hood':
					if row[0] == 21:
						mainHead[row[0]] = makeHeadPieceDict(row,header)
					else
					#skip to next row
				else
				mainHead[row[0]] = makeHeadPieceDict(row,header)
			else
			"""
			plusIndex = row[0].find('+')
			name = row[0][:plusIndex]
			mainHead[name] = makeHeadPieceDict(row,header)

print mainHead['Old Ironclad Helm']


with open('headarmor.json', 'w') as fp:
	json.dump(mainHead,fp)

