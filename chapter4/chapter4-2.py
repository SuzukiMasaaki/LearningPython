# if文のブロック
s = 60
print('あなたの点数は', s, '点です。')

# {}でくくらない。インデントでブロックを表現する。
if s < 70 :
    print('平均点まであと', 70 - s, '点です。')
    print('頑張りましょう')
else:
    print('よくできました！')
