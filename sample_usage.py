from chinese2stroke import trans2stroke

data = ['機器學習', '青玉案']
stroke, ord_text = trans2stroke(data, True)
print('input:\t\t',data)
print('stroke:\t\t',stroke)
print('ordinary:\t',ord_text)

