import csv
import json


def convert(fileLoc):
    #Read file
    f = open(fileLoc,"r")

    csvReader = csv.reader(f, delimiter=',')

    lineNo = -1
    headers = ""
    arr = []
    for row in csvReader:
        lineNo += 1
        if lineNo == 0:
            headers = row
        else:
            tempDict = {}
            for x in range(len(headers)):
                tempDict[headers[x]] = row[x]
            arr.append(tempDict)
    f.close()

    #write file
    writer = open("newFile.json","w+")
    writer.write(json.dumps(arr))
    writer.close()


if __name__ == "__main__":
    convert("GDP by Country 1999-2022.csv")
