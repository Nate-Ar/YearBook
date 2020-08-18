import os
ylist = []


def listyears():
    arr = os.listdir('static/Years')
    for line in arr:
        ylist.append(line)


listyears()
print(ylist)