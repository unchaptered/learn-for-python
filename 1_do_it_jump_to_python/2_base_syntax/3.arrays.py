# ARRAYS

string_arr = ["AAA","BBB","CCC", "DDD"]

print('string_arr[0]', string_arr[0]) # AAA
print('string_arr[2]', string_arr[2], '\n') # CCC

mixed_arr = ['AAA', 'BBB', 342]
print('mixed_arr[0]', mixed_arr[0],) # AAA
print('mixed_arr[0]', type(mixed_arr[0]),) # <class 'str'>

print('mixed_arr[2]', mixed_arr[2]) # 342
print('mixed_arr[2]', type(mixed_arr[2]), '\n') # <class 'int'>

arranged_arr = [111,222,333,444,555,666,777]
print('arranged_arr[0:1]', arranged_arr[0:1]) # [111]
print('arranged_arr[0:2]', arranged_arr[0:2]) # [111, 222]
print('arranged_arr[0:len(arranged_arr):2]', arranged_arr[0:len(arranged_arr):2], '\n') # [111, 333, 555, 777]

arranged_arr[0] = '111'
print('arranged_arr[0]', arranged_arr) # ['111', 222, 333, 444, 555, 666, 777]

arranged_arr[0:3] = 'AAA'
print('arranged_arr[0:3]', arranged_arr) # ['A', 'A', 'A', 444, 555, 666, 777]

arranged_arr[0:3] = ['AAA', 'AAA', 'AAA']
print('arranged_arr[0:3]', arranged_arr) # ['AAA', 'AAA', 'AAA', 444, 555, 666, 777]

arranged_arr[0:2] = []
print('arranged_arr[0:2]', arranged_arr, '\n') # ['AAA', 444, 555, 666, 777]