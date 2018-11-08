# リスト型変数　参照
a = [1,2,3]
print(a[1]);

# リスト型変数　代入
b = [1,2,3]
b[0] = 'ONE'
b[1] = 'TWO'
b[2] = 'Three'
print(b)

#リストの要素数の取得
print(len(b))

# あたいの有無を確認する
list1 = ['ACE', 'King', 'Queen']
chk = 'ACE' in list1
print('chk = ',chk)

# 他の型からリスト型に変換する
c = list('ABCDEF')
print(c)

# リスト内にリストを詰める (多次元配列)
a1 = ['A', 'B', 'C']
a2 = ['D', 'E', 'F']
a3 = [a1, a2]
print(a3)

# 要素を追加する
d = [1,2,3]
d.append(4)
print(d)

# リストの連結
list2 = ['red', 'blue', 'yellow']
list3 = ['white', 'black']
list4 = list2 + list3
print(list4)

# 要素を削除する pop(削除する要素番号)
list4.pop(2)
print(list4)

# delによる削除
del list4[1]
print(list4)

# リストを変数に分割する
list5 = ['tea', 'coffee', 'soda']
x, y, z = list5
print('x = ',x ,'y = ', y, 'z = ',z)

# ソート
v = [53, 6, 80, 1, 17]
v.sort()
print(v)
v.sort(reverse = True)
print(v)

# ソート結果を別変数に格納する
s = [53, 6, 80, 1, 17]
f = sorted(s)
print(f)
