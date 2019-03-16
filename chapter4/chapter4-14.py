# 内包表記
a = [1, 2, 3, 4, 5]
a_db = []
for x in a:
    # a[]の値を2倍しながらa_db[]に格納
    a_db.append(x*2)
    print(a_db)

# 別の書き方
# 左から順に処理していく
# この場合は、ループの x in aから処理する 
b_db = [x*2 for x in a]
print(b_db)
