import pickle

stroke_list = open('Open_Data/Properties/CNS_stroke.txt').readlines()
unicode_list1 = open('Open_Data/MapingTables/Unicode/CNS2UNICODE_Unicode 15.txt').readlines()
unicode_list2 = open('Open_Data/MapingTables/Unicode/CNS2UNICODE_Unicode 2.txt').readlines()
unicode_list3 = open('Open_Data/MapingTables/Unicode/CNS2UNICODE_Unicode BMP.txt').readlines()

stroke = dict() 
for i in stroke_list:
    _ = i.strip().split('\t')
    stroke.update({_[0]:_[1]})

unicode_list = dict() 
for i in unicode_list1:
    _ = i.strip().split('\t')
    unicode_list.update({_[1]:_[0]})
for i in unicode_list2:
    _ = i.strip().split('\t')
    unicode_list.update({_[1]:_[0]})
for i in unicode_list3:
    _ = i.strip().split('\t')
    unicode_list.update({_[1]:_[0]})

with open('unicode_list.pickle', 'wb') as f:
    pickle.dump(unicode_list, f)

with open('stroke.pickle', 'wb') as f:
    pickle.dump(stroke, f)
