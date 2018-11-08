# 集合
a  = {'いちご', 'りんご', 'みかん'}
print(a)

# 他の型から集合に変換
seta = set('ABCDEF')
print(seta)

# リストから集合に変換
li = [1, 5, 11, 9, 7, 12]
setb = set(li)
print(setb)

# 集合の要素数を取得する
length = len(li)
print(length)

# 値の有無の判定
chk = 1 in li
print(chk)

# 集合の演算
# 積集合
d = [1, 4, 11, 10, 8, 3]
setd = set(d)
c = setd.intersection(setb) #または c = setd & setb
print(c)

# 和集合
c  = setd.union(setb) #または c = setd | setb
print(c)

# 差集合
c = setd.difference(setb) #または c = setd - setb
print(c)

# 対象差集合(排他的論理和)
c = a.symmetric_difference(setb) #または c = setd ^ setb
print(c)


# 部分集合 どちらかの集合にもう一方の集合が全て含まれているかどうか
c = setd.issubset(setb) #または c = setd <= setb
print(c)

li = [1, 11]
setb = set(li)
c = setb.issubset(setd) #または c = setd <= setb
print(c)
