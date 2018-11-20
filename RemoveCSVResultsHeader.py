import csv
import os

os.makedirs('headerRemoved', exist_ok=True) # Creates an export directory for processed files


# Loop through every file in current working directory.
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue # skip if not a csv file

    print("Removing header from " + csvFilename + "...")

    # Read the CSV file in, skip over rows until headings are found, identified by 'Test Results...'
    csvRows = []
    foundHeadings = False
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        for field in row:
            if field == "Test Results...":
                foundHeadings = True
        if not foundHeadings: # if foundHeadings is still false
            continue # skip row
        csvRows.append(row)
    csvFileObj.close()

    # Write out the CSV file
    csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w', newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()
