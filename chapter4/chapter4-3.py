# 連続したif文
a = 1000
print(a, 'は')

if 0 <= a & a <= 9:
    print('1桁の数字です。')
elif 10 <= a & a <= 99:
    print('2桁の数字です。')
elif 100 <= a & a <= 999:
    print('3桁の数字です。')
else:
    print('4桁以上です。')
