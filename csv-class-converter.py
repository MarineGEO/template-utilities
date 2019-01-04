# converts a csv file of vocab or field items into a python class format
import csv
import chardet

# user inputs - path to csv file and the desired class type
csv_file = "/Users/ambell/Documents/MarineGEO-template-workbooks/fish-seines/fields_v0.0.1.csv"
classType = "Field" # "Field or "Vocab"


# grab the encoding of the csv file
with open(csv_file, 'rb') as r:
    encod = chardet.detect(r.read())["encoding"]

# read the csv file as a list
with open(csv_file, 'r', encoding=encod) as f:
    r = csv.reader(f)
    items = list(r)

header = items[0]  # header
items.pop(0) # remove the header from the list of items


# process a single row - converts the items in the list to a string that matches the class object
def singleRow(objType, header, row):

    st_pairs = ""

    for i in range(len(header)):
        if row[i] != "":
            st_pairs = st_pairs + f"{header[i]}='{row[i]}', "

    # remove last two chars from str
    st_pairs = st_pairs[:-2]

    st = f"{objType}({st_pairs}),"

    return st


# loop through all rows in the csv and convert it
def allRows(objType, header, items):
    s = ""
    for i in range(len(items)):
        single = singleRow(objType, header, items[i])
        s = s + single + "\n"
    return s

print(allRows(classType, header, items))