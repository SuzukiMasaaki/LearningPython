#条件式を含む内包表記
a = [1, 5, 17, 25, 32]
# a[]のvalueが10以上のもののみ、2倍して格納する
a_chk = [x*2 for x in a if x >= 10]
print(a_chk)
