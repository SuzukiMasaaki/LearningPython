# continue
li = [1, 3, 5, '七', 9]
for a in li:
    if type(a) == str:
        # 文字列かどうかの判定は、type()関数 == str を使う。
        print(a, '数値ではなく文字列です')
        continue
    print(a)
