# Set

number_set = set([1, 2, 3])
print(number_set) # { 1, 2, 3 }

number_set = { 1, 2, 3 }
print(number_set) # { 1, 2, 3 }

number_list = [ 1, 2, 3, 4, 5, 6 ]
new_number_list = list(set(number_list))
print(new_number_list) # { 1, 2, 3, 4, 5, 6}

string_ = 'abcde'
string_list = set(string_)
print(string_list) # { 'b', 'd', 'c', 'e', 'a' } # 매번 달라짐