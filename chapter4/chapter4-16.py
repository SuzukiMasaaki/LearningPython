# 辞書の内包表記
# モジュールの読み込み
from random import randint

keys = ['いちご', 9, 'みかん', 25, 'りんご']

# keys[]が文字列の場合のみ、1〜100のランダムな値を取って辞書化する
d = { x:randint(1, 100) for x in keys if type(x) == str }
print(d)
