import json
import csv

def main():
    # Open the csv file
    infile = open('EC.csv', 'r')
    
    #Create a list to store the data
    items = []    
    #Set the field names (headers)
    headers = ["Low SES, Low Arts","Low SES, High Arts",
               "Overall Sample","High SES, Low Arts","High SES, High Arts"]
    
    
    # Create a CSV reader
    reader = csv.DictReader(infile, fieldnames=headers)

    # Put the data into the list of items
    for row in reader:
        items.append(row)

    
    # Create and output file and write the data to it
    with open('data.json', 'w') as outfile:
        json.dump(items, outfile)


if __name__ == '__main__':
    main()