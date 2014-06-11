import csv
mainHead = {}
def kludgeDict(values,header):
	headPiece = {}
	for i in range(len(header)):
		headPiece[header[i]] = values[i]
	return headPiece
with open('Dark Souls 2 Armor - Head.csv', 'r') as armorCsv:
	armorReader = csv.reader(armorCsv, dialect='excel')
	isFirstRow = True
	for row in armorReader:
		if isFirstRow:
			header = row
			isFirstRow = False
		else:
			mainHead[row[0]] = kludgeDict(row,header)
print mainHead['Vengarl\'s Helm']
