# STRINGS...

string_sentence = 'Hello, World'

print('string_sentence[0]', string_sentence[0]) # H
print('string_sentence[1]', string_sentence[1]) # e
print('string_sentence.find("e")', string_sentence.find('e'))  # 1

print('string_sentence[-1]', string_sentence[-1]) # d
print('string_sentence[-2]', string_sentence[-2]) # l

print('string_sentence[0:-1:1]', string_sentence[0:-1:1]) # Hello, Worl
print('string_sentence[0:-1:2]', string_sentence[0:-1:2], '\n') # Hlo ol


string_backtick = "BACK {aaa}, COMBACK {bbb}".format(aaa="오마이", bbb=37)

print('string_backtick', string_backtick, '\n') # BACK 오마이, COMBACK 37
