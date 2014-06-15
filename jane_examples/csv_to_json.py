import csv, json
import re
from config import HEAD_ARMOR_CSV, HEAD_ARMOR_JSON, string_header_values

# Returns a dictionary of the properties of an item
# Input: row - a list of properties in the order defined by global header
def get_item_properties(row):
	item_properties = {}
	global header
	for i, p in enumerate(header):
		if row[i] and i > 0:														# not in the 'Name' column
			if p in string_header_values:
				item_properties[p] = row[i]
			else:
				item_properties[p] = float(row[i])
	return item_properties

# Takes a csv and outputs a dictionary
# Input: the name of the armor CSV file to use
def csv_to_json(csv_filename):
	with open(csv_filename, 'r') as armor_csv:
		armor_reader = csv.reader(armor_csv)
		global header
		header = armor_reader.next()												# get first row

		armor_dict = {}
		for row in armor_reader:
			armor_name = row[0]

			if re.match(r'.+\+\d+.*',armor_name):									# ignores entries not of the form 'any text+(number)'
				pieces = armor_name.split('+')
				armor_name = pieces[0]
				digits = [num for num in pieces[1].split() if num.isdigit()]		# list of all groups of digits in string
				plus_value = int(digits[0])											# first number in string

				if armor_name in armor_dict:										# if the name is already in the dictionary
					if plus_value > armor_dict[armor_name]["Plus_Value"]:			# update if necessary
						armor_dict[armor_name] = get_item_properties(row)
						armor_dict[armor_name]["Plus_Value"] = plus_value
				else:																# otherwise, put it in
					armor_dict[armor_name] = get_item_properties(row)
					armor_dict[armor_name]["Plus_Value"] = plus_value

	return armor_dict


# Dump data into JSON file

armor_dict = csv_to_json(HEAD_ARMOR_CSV)

with open(HEAD_ARMOR_JSON, 'w') as armor_json:
	json.dump(armor_dict, armor_json)