import csv, json
from random import randint

allEntries = []

with open('entries.csv', 'r') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		allEntries.append(row)


results = []
while len(allEntries) > 0:
	randomEntry = randint(0, len(allEntries) - 1)
	thisResult = allEntries[randomEntry]
	print(allEntries[randomEntry]["Entry"])
	results.append(thisResult)
	allEntries.remove(thisResult)

with open('results.csv', 'w+', newline='') as csvfile:
	fieldnames = ["Timestamp","Entry","Email Address","Name:"]
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	for eachResult in results:
		writer.writerow(dict(eachResult))

with open('results_public.csv', 'w+', newline='') as outfile:
	writer = csv.writer(outfile,delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	print("******")
	for eachResult in results:
		eachResult = dict(eachResult)
		print(eachResult['Entry'])
		writer.writerow([eachResult['Entry']])