import re


def find_date(line):
    pattern = r"([A-Za-z][-,A-Za-z. ']+[ ]*)+"
    result = re.findall(pattern,line)

    return result


f = open("names.txt")
for line in f.readlines():
    #print(line)
    result = find_date(line)
    if (len(result)>0):
        print(result)

