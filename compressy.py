#!/usr/bin/env python3
import lzma
import sys
import os.path
from colored import fg, bg, attr
from terminaltables import AsciiTable

# Total benefit
totalBenefit = 0

class TableFormat:
    def getFormat(filename, content, contentCompressed, benefit):
        return [filename,
            "%s bytes" % len(content),
            "%s bytes" % len(contentCompressed),
            "%s %s %s bytes" % (bg("white") + fg("black"), benefit, attr(0))]

    def getTotalFormat(totalBenefit):
        return ["%sTotal%s" % (attr(1), attr(0)),
            "", "", "%s %s %s bytes" % (bg("blue") + fg("white"), totalBenefit, attr(0))]

def compressFile(file):
    # Validate file path
    if os.path.isfile(file) != True:
        print(fg("red") + "Error: %s does not exist." % file + attr(0))
        return

    content = open(file, "rb").read()
    contentCompressed = lzma.compress(content)
    benefit = len(content) - len(contentCompressed)

    tableData.append(TableFormat.getFormat(
        file, content, contentCompressed, benefit))

    global totalBenefit
    totalBenefit = totalBenefit + benefit

    # Write to file
    with lzma.open(file + ".xz", "w") as out:
        out.write(content)

def checkArgs():
    # Check if user has entered arguments
    if len(sys.argv) == 1:
        print("Please enter the name of the files to compress.\n" +
            attr(1) + "\tExample: %s %sexample.txt" % (sys.argv[0], fg("green")) + attr(0))
        exit()    

checkArgs()

# Define initial table data
tableData = [
    ["Filename", "Before", "After", "Benefit"]
]

# Determine file paths
files = sys.argv
files.pop(0)

print("Compressing %i file%s..."
    % (len(files), "s" if len(files) > 1 else ""))

for file in files:
    compressFile(file)

tableData.append(TableFormat.getTotalFormat(totalBenefit))

table = AsciiTable(tableData)
print("\n" + table.table + "\n")
