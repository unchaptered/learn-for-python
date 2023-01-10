# Set
# Set can't be not sorted

number_set = set([1, 2, 3])
print(number_set) # { 1, 2, 3 }

number_set = { 1, 2, 3 }
print(number_set) # { 1, 2, 3 }

number_list = [ 1, 2, 3, 4, 5, 6 ]
new_number_list = list(set(number_list))
print(new_number_list) # { 1, 2, 3, 4, 5, 6 }

string_ = 'abcde'
string_list = set(string_)
print(string_list) # 문자열을 배열화 : { 'b', 'd', 'c', 'e', 'a' }

left_set = set([1, 2, 3, 4, 5, 6])
right_set = set([4, 5, 6, 7, 8, 9])
print(left_set & right_set) # 교집함 탐색 : { 4, 5, 6 }
print(left_set - right_set) # 차집함 탐색 : { 1, 2, 3 }
