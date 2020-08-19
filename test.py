import os
years = []
whaty = 0

def listyears():
    arr = os.listdir('static/Years')
    for line in arr:
        years.append(line)


listyears()
for year in years:
    on = years.index(year)
    year = years[on]
    print(str(year))