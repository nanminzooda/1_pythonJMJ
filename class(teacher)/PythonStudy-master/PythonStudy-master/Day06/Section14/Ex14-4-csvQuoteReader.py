'''
Ex14-4-csvQuoteReader.py
'''

member_list = []
with open('회원명단.csv', 'rt', encoding='UTF-8') as file:
    file.readline()
    while True:
        line =file.readline()
        if not line:
            break
        member = line.split(',')
        member[0] = member[0].strip('"')
        member_list.append(member)
print(member_list)






