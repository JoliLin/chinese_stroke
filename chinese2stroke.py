import os
import sys
import pickle

unicode_path = './unicode_list.pickle'
stroke_path = './stroke.pickle'


with open( unicode_path, 'rb') as f:
    unicode_list = pickle.load(f)

with open( stroke_path, 'rb') as f:
    stroke = pickle.load(f)

trans2unicode = lambda x:hex(ord(x))[2:].upper()

def ch2stroke(ch_char):
    uni_text = trans2unicode(ch_char)
    cns_text = unicode_list.get(uni_text)
    stroke_text = stroke.get(cns_text)
    return stroke_text, ord(ch_char)

none2zero = lambda x: 0 if x == None else x

def trans2stroke(text=[], is_clear=False):
    stroke_ = []
    ord_ = []
    for i in text:
        _s = []
        _o = []
        for char in i:
            _ss, _oo = ch2stroke(char)
            _s.append(_ss)
            _o.append(_oo)
        stroke_.append(_s)
        ord_.append(_o)

    if is_clear:
        return [list(map(int, map(none2zero, i))) for i in stroke_], ord_

    else:
        return stroke_, ord_



