import csv
with open('fil1.csv')as csvfile:
    d=csv.DictReader(csvfile)
    print('Period       Subject')
    print("____________________")
    for i in d:
        print(i['Period'],i['Subject'])
