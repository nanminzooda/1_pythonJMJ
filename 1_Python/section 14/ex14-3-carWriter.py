'''

아까는 학생명단을 읽어온 것 뿐.

'''

import csv
'''
csv 모듈을 사용할 거에요.

with open('차량관리.csv', 'w') as file:
    csv_maker = csv.writer(file, delimiter=',')
    csv_maker.writerow([1, '08러1234', '2020-10-20, 14:00'])
    csv_maker.writerow([2, '25롸2234', '2020-10-20, 14:10'])
    csv_maker.writerow([3, '29하9854', '2020-10-20, 14:20'])

print('차량관리.csv파일이 생성되었습니다.')
'''

### 호호 저 위로도 되고 ! 이제 하나 더 ! 다른 방법

'''
with open('차량관리.csv', 'w', newline='') as file:
    csv_maker = csv.writer(file, delimiter=',')
    csv_maker.writerow([1, '08러1234', '2020-10-20, 14:00'])
    csv_maker.writerow([2, '25롸2234', '2020-10-20, 14:10'])
    csv_maker.writerow([3, '29하9854', '2020-10-20, 14:20'])

# 이 파일을 엑셀에서 열어보면 예쁜 표가 기다리고 있따.

'''

# 마지막 방법 !

import csv

with open('차량관리.csv', 'w') as file:
    csv_maker = csv.writer(file, delimiter=',', quotechar='"')
    csv_maker.writerow([1, '08러1234', '2020-10-20, 14:00'])
    csv_maker.writerow([2, '25롸2234', '2020-10-20, 14:10'])
    csv_maker.writerow([3, '29하9854', '2020-10-20, 14:20'])