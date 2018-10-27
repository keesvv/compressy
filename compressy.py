#!/usr/bin/env python3
import sys
import os.path
from colored import fg, bg, attr
from terminaltables import SingleTable

# Total benefit
totalBenefit = 0

class TableFormat:
    def getFormat(filename, content, contentCompressed, benefit):
        return [os.path.basename(filename),
            "%s bytes" % len(content),
            "%s bytes" % len(contentCompressed),
            "%s %s %s bytes" % (bg("white") + fg("black"), benefit, attr(0))]

    def getTotalFormat(totalBenefit):
        return ["%sTotal%s" % (attr(1), attr(0)),
            "", "", "%s %s %s bytes" % (bg("blue") + fg("white"), totalBenefit, attr(0))]

class Compression:
    def compressFile(file):
        # Validate file path
        if os.path.isfile(file) != True:
            print(fg("red") + "Error: file %s does not exist." % file + attr(0))
            return

        content = open(file, "rb").read()
        contentCompressed = compress.compress(content)
        benefit = len(content) - len(contentCompressed)

        tableData.append(TableFormat.getFormat(
            file, content, contentCompressed, benefit))

        global totalBenefit
        totalBenefit = totalBenefit + benefit

        # Write to file
        with compress.open(file + "." + ext, "w") as out:
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

# User preference of compression algorithm
if files[0] == "--gzip":
    files.pop(0)
    ext = "gz"
    import gzip as compress
elif files[0] == "--bzip":
    files.pop(0)
    ext = "bz2"
    import bz2 as compress
else:
    ext = "xz"
    import lzma as compress

print("Compressing %i file%s..."
    % (len(files), "s" if len(files) > 1 else ""))

for file in files:
    Compression.compressFile(file)

tableData.append(TableFormat.getTotalFormat(totalBenefit))

table = SingleTable(tableData, "%sResults%s" % (fg("yellow"), attr(0)))
print("\n" + table.table + "\n")
