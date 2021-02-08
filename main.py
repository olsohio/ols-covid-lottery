import csv
from random import randint

group_size = 5  # Change this to match your group size
allEntries = []

with open('confidential_entries/entries.csv', 'r') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		allEntries.append(row)

results = []
while len(allEntries) > 0:
	randomEntry = randint(0, len(allEntries) - 1)
	thisResult = allEntries[randomEntry]
	results.append(thisResult)
	allEntries.remove(thisResult)



group_count = 0 # Dont change this
with open('confidential_results/results.csv', 'w+', newline='') as csvfile:
	fieldnames = ["Entry","Email Address","Name:","Slot","Group"]
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()

	for eachResult in results:
		index = results.index(eachResult)
		eachResult["Slot"] = index

		if index % group_size == 0:
			group_count += 1
			eachResult["Group"] = group_count

		else:
			eachResult["Group"] = group_count

		writer.writerow(dict(eachResult))

with open('public_results/results_public.csv', 'w+', newline='') as outfile:
	writer = csv.writer(outfile,delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	for eachResult in results:
		eachResult = dict(eachResult)
		print(f"Reference Number: {eachResult['Entry']} assigned to Slot {eachResult['Slot']} Group {eachResult['Group']} ")
		slot = f"Slot {index}"
		writer.writerow([f"Reference Number {eachResult['Entry']}", f"Slot {eachResult['Slot']}" , f"Group {eachResult['Group']}"])