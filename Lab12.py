import re

mydict = {}
regex = r".*\[01/Jul/1995:(([0][0]:[1][2-9])|([0][0]:[2-5][0-9])|([0][1-6]:[0-5][0-9])|([0][7]:([0][0-9])|([1][0-8]))).* (\"POST.*\") 200 .*"
with open('access_log_Jul95', "r") as file:
    data = file.readlines()
    for a in data:
        if (re.match(regex, a)):
            x = re.search(regex, a)
            if x.group(8) in mydict:
                mydict[x.group(8)] = mydict[x.group(8)] + 1
            else:
                mydict[x.group(8)] = 1

    sort_mydict = sorted(mydict.items(), key=lambda x: x[0])
    try:
        print("Top 1 log:", sort_mydict[0][0], "found", sort_mydict[0][1], "times")
        print("Top 2 log:", sort_mydict[1][0], "found", sort_mydict[1][1], "times")
        print("Top 3 log:", sort_mydict[2][0], "found", sort_mydict[2][1], "times")
        print("Top 4 log:", sort_mydict[3][0], "found", sort_mydict[3][1], "times")
        print("Top 5 log:", sort_mydict[4][0], "found", sort_mydict[4][1], "times")
    except IndexError as a:
        print(a)
