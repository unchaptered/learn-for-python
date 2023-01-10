# File System

file = open('새파일.txt', 'w', encoding='UTF-8')
string_list = ['AAA', 'BBB', 'CCC', '무야호', 'DDD']
for string in string_list:
    file.write(string + '\n')
file.close()


opened_file_1 = open('새파일.txt', 'r', encoding='UTF-8')
line = opened_file_1.readline()
print(line) # 'AAA'


opened_file_2 = open('새파일.txt', 'r', encoding='UTF-8')
while True:
    line = opened_file_2.readline()
    if not line: break
    print(line)
        # 'AAA'
        # 'BBB'
        # 'CCC'
        # '무야호'
        # 'DDD'
opened_file_2.close()


