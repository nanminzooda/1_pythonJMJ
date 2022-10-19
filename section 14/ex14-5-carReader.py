import csv

with open('차량관리.csv', 'r', newline='') as file:
    csv_reader = csv.reader(file, delimiter=',', quotechar = '"')
    for line in csv_reader:
        print(line)

# 이해는 되는데 잘 와닿진 않아요 ㅎ그흑 그치만 다 바로 이해할 순 없는 법 ㅠ !