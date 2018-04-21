# Pythone cheat sheat

## `2`と`3`

破壊的変更がきつくて移行がおくれまくってるけど、最近はmacでも3が標準になったらしい

この項は`3`でいく

## 環境について

`pyenv`でPythonそのものの管理  
`venv`ないし`virtualenv`で実行環境(使用するPythonとライブラリ)の管理を行う

厳密にやるならpyenvも使ったほうがいいけど、そんなにバージョンがあがらないのでvenvのみが一般的らしい

今回はvenvのみでいく

Dockerを使うのもありだけどコード書くのは保管とかいろいろでしんどそ。

### 構築

```bash
# .venvに実行環境を構築 このファイル名が多いっぽい
# なお、git管理はしないのがベター
python3 -m venv .venv
# こんな感じでpythonのバージョン指定もできるっぽい?
python3 -p python2 -m venv .venv

# 作成した環境を読み込む
# fishとか変わり種シェル使ってる人はそれ用のスクリプトがあるっぽい
. .venv/bin/activate
# 指定のpipをインストール
pip install -r requirements.txt
```

## pipについて

venv環境下でいじってもローカルにしか反映されないけど何も考えずに実行するとグローバルに入るので注意。  
グローバルに入れるものはあんまりないと思う。後述するIPythonくらいでいいのでは？

`requirements.txt`というファイルに依存モジュールを保存するのがマナー。

```bash
# install
pip install neovim
# update requirements.txt
pip freeze > requirements.txt
```

## REPL

`IPython`がいいらしい。Rubyのpryみたいなもんか。

---

## 文法

[Guide](http://www.python.ambitious-engineer.com/archives/52)

```python
# print
print('hello, world!')
print(1)
# 改行を外すには最終引数にend=''などを指定
print(1, end='')

# 文字列結合は+
'Hello,' + 'World' # => Hello,World
# 数値など文字列以外を結合する際にはキャスト
str(12) + '/' + str(31) # => 12/31

# 変数そのものはRubyとそっくり いきなり宣言OKとか
a = 10
b = a
a = 1
print(a, b) # => 1, 10 参照渡しじゃーない
# 複数いっぺんにいける
x, y, z = 1, 2, 3
a, b, c = x, y, z

# 定数はない 残念
```

```python
# idメソッドでインスタンスidが取れる
id(1)
id(True)
# 値を変更するとidが変わる
true = True
id(true)
true = 'True'
id(true)
```

```python
# 引数はsys.argvという配列に入る
import sys 
# 0に実行パスからの相対パスでファイル名、
# 以後順番に入っていく
print(sys.argv)
```

識別子は`/[a-zA-Z_][a-zA-Z0-9_]'/` でおけ  
先頭は数字禁止と覚えよう  
また**先頭に_つけると特殊な扱いになるので注意**

```python
# numeric 
1
# int, float, complexの3つがある
# int _は無視される
1_000 # => 1000
# 0b, 0o, 0xはじまりにするとそれぞれ2進、8進、16進
0b11110101 # => 245
0o234567 # => 80247
0x1af29d # => 1766045
# float まぁいつもの感じ
0.0012
1.2e+3 # => 0.012
1.2e-3 # => 1200.0
# 制度を調べるにはsys.float_info
import sys
sys.float_info
# complex 複素数なんだけど…学がないからわからん TODO

# 演算子については以下
10 + 3 # => 13
10 - 3 # => 7
10 * 3 # => 30
10 / 3 # => 3.3333333333335
10 // 3 # 3 (/ の端数切り捨てver)
10 % 3 # => 1
-(-10) # => 10 符号反転
+(-10) # => -10 符号そのまま…なにこれ
abs(-10) # => 10
int(-5.55) # => -5 小数点以下を切り捨てて整数へ変換
float(10) # => 10.0
complex(10, 3) # => 複素数 TODO
divmod(10, 3) # => (3, 1)
pow(10, 3) # => 1000
10 ** 3 # => 1000

# よく使うモジュール
# numbers 基底クラスなので型判定に使う import必要ない
isinstance(1.2e-3, numbers.Number) # => True
# math(複素数ならcmath) いろいろ定番が
import math
math.pi # => 3.141592...
math.sin(math.pi / 2) # => 1.0
# decimal
from decimal import Decimal
0.1 * 33 == 3.3 # => False
Decimal('0.1') * 33 == Decimal('3.3') # => True
# fractions (分数)
from fractions import Fraction
Fraction(3, 7) * 2 # => Fraction(6, 7)
# random 乱数とかランダムにとってくるとか
import random
random.random # => 0.0~1.0
random.uniform(3, 100) # => 3.0~100.0
random.randint(3, 100) # => 3 ~ 100
random.choice('asdfg') # => なんか1文字
random.shuffle([0, 1, 2, 3, 4]) # => 並び替えるんだけど、破壊的に変更するのでこれだと何も起こらない 微妙
```

```python
# boolean 先頭が大文字 Falseが0でTrueが1(というかそれ以外)というややこしさ
True
False
True == 1 # => true
False == 0 # => true
# 論理演算は記号ではなくand or not
False or True # => True
False and True # => False
not False # => True
not 0 # => True
not 1 # => False
not 100 # => False
# キャストもまぁ一応できる
bool(0) # => False
bool(100) # => True
bool('True') # => True
bool('False') # => True
```

```python
# None null的なもの boolにキャストするとFalse
None # => None
bool(None) # => False
```

```python
# Array よくある感じ ちゃんぽんもOK
ary = [1, 2, 3]
ary2 = [1, 'two', 3, 'vier', 5]
# 添字は正と逆両方OK
ary[0] # => 1
ary2[-1] # => 5
# :で範囲指定できる スライス構文というらしい 2つ目の手前まで対象
ary2[1:-1] # => ['two', 3, 'vier']
ary2[1:] # => ['two', 3, 'vier', 5]
ary2[:2] # => [1, 'two']
# 長さはlen
len(ary2) # => 5
# pushではなくappend
ary2.append('six')
ary2 # => [1, 'two', 3, 'vier', 5, 'six']
# 途中に突っ込むのはinsert
ary2.insert(3, 'mid') # index3の箇所に入れるって感じ
ary2 # => [1, 'two', 3, 'mid', 'vier', 5, 'six']
# 要素指定して削除はremoveだけど、うっかりないとErrorになるので微妙
ary2.remove('mid')
ary2 # => [1, 'two', 3, 'vier', 5, 'six']
# index指定して削除はpop
ary2.pop(2) # => 3
ary2 # => [1, 'two', 'vier', 5, 'six']
# まとめて削除はdel 単発でもいいけど
del ary2[1]
ary2 # => [1, 'vier', 5, 'six']
del ary2[:-2]
ary2 # => [5, 'six']

# イテレーションはfor x in X:
for el in ary:
    print(el)
for i, el in enumerate(ary):    # indexを取得しつつまわす
    print(i, el)
# forで一気にmapとかfilterっぽいことができる
# リスト内包表記というらしい
# filter単発はできない？
ary3 = [num ** 2 for num in ary] # map
ary4 = [num ** 2 for num in ary if num % 2 == 0] # map & filter
# ソートはsorted
sorted(ary3) # => [0, 1, 4, 9, 16]
sorted(ary3, reverse=True) # => [16, 9, 4, 1, 0]
# keyに色々条件をかけるらしいけど難しいのでとりあえず大文字小文字無視sort
sorted(['bc', 'ac', 'bD', 'AB']) # => ['AB', 'ac', 'bD', 'bc']
sorted(['bc', 'ac', 'bD', 'AB'], key=str.lower) # => ['AB', 'ac', 'bc', 'bD']
# 破壊的ソートやるならary.sort()でできるけど使わないな…

# tupleがある やったぜ
# イテレーションとかできるけどイミュータブル こうでないと
(1, 2, 3)
('one', 2, 'drei')
(1,) # 値が一つしかない場合カンマをつける

# rangeもある
range(0, 10) # => range(0, 10)
# listでキャスト
# 見ての通り、第一引数 < 第二引数
list(range(0, 10)) # => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 第3引数つけると、その値ずつ増加する
list(range(0, 10, 3)) # => [0, 3, 6, 9]
# イテレーションできるので、for文なんかで使うとわかりやすい
for i in range(0, 10):
    print(i)
```

```python
# 文字列 シングル、ダブルどっちも同じ
'asd'
"asd"
# 実はほとんど配列
"asd"[1] # => 's'
# キャストはstr
str(12)
# 足すとconcat
ary + ary2 # => [1, 2, 3, 1, 'two', 3]
```

シーケンス型共通で使える演算子はこんな感じ

```python
# LEFT include RIGHT
'apple' in ('orange', 'pineapple') # => False
'apple' in ('apple', 'orange', 'pineapple') # => True
'apple' not in ('orange', 'pineapple') # => True
'apple' not in ('apple', 'orange', 'pineapple') # => False
# concat 2 sequence
[1, 2, 3] + ['orange', 'pineapple'] # => [1, 2, 3, 'orange', 'pineapple']
[1, 2, 3] + ('orange', 'pineapple') # => ERROR!
# multiplize
[1, 2, 3] * 3 # => [1, 2, 3, 1, 2, 3, 1, 2, 3]
# get
('apple', 'orange', 'pineapple', 'grape', 'mango')[3] # => 'grape'
('apple', 'orange', 'pineapple', 'grape', 'mango')[-3] # => 'pineapple'
('apple', 'orange', 'pineapple', 'grape', 'mango')[2:-1] # => ['pineapple', 'grape']
('apple', 'orange', 'pineapple', 'grape', 'mango')[2:5:2] # => ['pineapple', 'mango']
```

共通で使えるメソッドはこんな感じ

```python
len([0, 1, 2]) # => 3
min([99, 10030, 8]) # => 8
max([99, 10030, 8]) # => 10030
(99, 10030, 8).index(8) # => 2
(0, 0, 0, 10, 0, 0).count(0) # => 5
```

setもある(重複と順序を持たないarrayみたいな)

```python
s = {1, 2, 3}
s = {'eight', 'nine', 10}
s = {1, 2, 3, 1, 1, 1} # => {1, 2, 3}
s = {1, 2, [1, 2, 3]} # => ERROR! ハッシュ化できる値しか入れられない 
s = {1, 2, (1, 2, 3)} # => OK
set([1, 2, 3, 1, 2, 3]) # => {1, 2, 3}

s = {1, 2, 3}
s.add(4) # => {1, 2, 3, 4}
s.remove(4) # => s == {1, 2, 3}
s.remove(5) # ERROR!存在しない要素を渡すと落ちる
s.discard(3) # => s == {1, 2}
s.discard(5) # Nothing else

# frozenset 名前の通りあとからいじれない
fs = frozenset({1, 2, 3})
fs = frozenset(['one', 'two', 'three'])

# setは集合演算できる
s1 = {'A', 'B', 'C'}
s2 = {'C', 'D', 'E'}
# 和集合
s1.union(s2) # => {'A', 'B', 'C', 'D', 'E'}
# 共通要素(積集合)
s1.intersection(s2) # => {'C'}
# 差集合
s1.difference(s2) # => {'A', 'B'}
s2.difference(s1) # => {'D', 'E'}
# subset
s1 = {'A', 'B'}
s2 = {'A', 'B', 'C'}
s1.issubset(s2) # True s1の要素がs2にぜんぶあるのでsubset
s2.issubset(s1) # False 'C'がs1にないからいかん
```

```python
# Dictionaly キーは''でくくる
dict = {'apple': 200, 'orange': 100, 'banana': 150}
# キーもバリューも変数使える
k = 'APPLE'
v = 'りんご'
{k: v} # => {'APPLE': 'りんご'}
# [key]でアクセスするか、getメソッドを使うか getの場合は存在しないのにアクセスしたらNoneが帰る
dict['apple'] # => 200
dict['pineapple'] # => ERROR!
dict.get('apple') # => 200
dict.get('pineapple') # => None
dict['apple'] = '1111' # => 更新される

# それぞれlistっぽいものにmapする
dict.keys() # => key ちなみにいきなりforでまわすとkeyでまわる
dict.values() # => value
dict.items() # => セット
# まわせる
for value in dict.values():
    print(value)
for i, (key, value) in enumerate(dict.items()):
    print(i, key, value)
```

### 比較

```python
# 値の比較とオブジェクトの比較の2種類がある
# 以下のxとyは同じオブジェクト、xとzは値は同じだが異なるオブジェクトである
x = [1, 2]
y = x
z = [1, 2]

# ==は値を比較し、 isはオブジェクトを比較する
print(x == y) # True
print(x == z) # True
print(x is y) # True
print(x is z) # False

# pythonは比較演算子をズラズラ並べて利用できる
1 < 2 < 3 # => True
1 < 2 > -1 # => True
1 < 2 > 3 # => False
```

### 制御構文

```python
# Pythonで偽と判定されるのは以下など
False
None
0
# __len__が定義されてて、これが0返すもの
''
[]
{}
()
# __nonezero__が定義されてて、これがFalse返すもの 知らない

x = 0
y = 1
# if elif else elifがちょっとめずらしい
if x == 0:
    print('x == 0')
elif y == 1:
    print('y == 1')
else:
    print('other')

# forにもelseがつけられる finally的に動作するけどいるの？
ary = [0, 1, 2]
for i in ary:
    print(i)
else:
    print(str(len(ary)) + '回まわりました')
# continueとbreakが使えるけど略

# whileあるよ
is_continue = True

while is_continue:
    print('キーを入力してください eと入力すると終了します')
    string = input()
    print(string + 'が入力されました')

    if string == 'e':
        is_continue = False
else:
    print('終了します')

# ifやらforやらのブロックの中がカラだとエラーになるので、
# なんもしませんよーという意味でpassというのがある…まぁこれを書くようなプログラミングはダメなんだろう
if True:
    pass

# fizzbuzz
for index in range(1, 100 + 1):
    is_fizz = index % 3 == 0
    is_buzz = index % 5 == 0

    if is_fizz and is_buzz:
        print(str(index) + ' fizzbuzz')
    elif is_fizz:
        print(str(index) + ' fizz')
    elif is_buzz:
        print(str(index) + ' buzz')
    else:
        print(index)
```

### 関数

```python
# defで定義
# なお、巻き上げとかないので定義前に使用することはできない
def sum(a, b):
    return a + b

# 呼び出しは引数を順番通りに指定するやり方と、キーワード引数がある
sum(1, 10) # => 11
# キーワード引数の場合、順番を無視できる
sum(b=10, a=1)

# デフォルト引数もあるよ
def hw(name='world'):
    return 'Hello, ' + name

hw() # => 'Hello, world'
hw('Jane') # => 'Hello, Jane'

# 可変長引数は2種類 *ひとつで値だけのやつ たくさん突っ込むとtupleでとれる
def sum_arguments(a, *args):
    print(a, args)

sum_arguments(1, 2, 3, 4, 5) # => 1 (2, 3, 4, 5)

# *2つでkey, valueのdictとれる
def sum_args(a, **args):
    print(a, args)

sum_args(1, b=2, c=3, d=4, e=5) # => 1 {'b': 2, 'c': 3, 'd': 4, 'e': 5}

# 戻り値はreturnで普通に返す
def sum_result():
    return 'Hello'
# なんもないとNoneが帰る
def non_result():
    pass
# 戻り値複数返すとtupleでとれる
def multi_result():
    return 'Hello', 'You'

# デフォルト引数は宣言時？の1回だけ初期化されるので、気をつけないとダメ
# 以下は想像通りのことがおきる
def ng_default_argv(x, arg=[]):
    arg.append(x)
    return arg
# これならOK...なんだけどそもそももうすこし考えたほうがいいだろうなー
def ok_default_argv(x, arg=None):
    if arg is None:
        arg = []

    arg.append(x)
    return arg

# 関数外で宣言した変数をグローバル変数、関数内はローカル変数と一般的に言われるらしい
# グローバル変数を関数内で変更したい際には小ネタが必要 まぁでもそもそもこういうのダメだよね
x = 100
def sample_function():
    global x # global宣言 xはglobal変数であることを明示する
    x = 200

# 関数は変数にぶち込める 最近の言語だね
def add(a, b):
    return a + b

a = add
a(1, 2) # => 3

# 関数内で関数を宣言できる
# その際、上位の関数で宣言された変数を参照するときにお作法がいろいろ
def outer_function():
    x = 100
    print(x, 'outer_function') # => 100

    def inner_function():
        # 上位で宣言されたものを参照する際には以下のように宣言する
        nonlocal x
        x = 200
        print(x, 'inner_function') # => 200

    inner_function()
    print(x 'after inner_function()') # => 200

outer_function()

---

# ジェネレータがある
# イテレートできるから、色々使えるみたい
def greeting_generator():
    yield 'おはよう'
    yield 'こんにちは'
    yield 'こんばんわ'

g = greeting_generator()

g.__next__() # => おはよう
next(g) # => こんにちは この書き方でもOK
g.__next__() # => こんばんわ
g.__next__() # => Error! StopIteration

# まわせる
for greet in greeting_generator():
    print(greet)

# 超巨大なlistの読み込みとかに使うといいみたい。file readとか…。

# yield variableと書くと値をセットすることもできる
def argv_generator():
    text = 'おはよう'
    yield text
    yield text
    yield text

g = argv_generator()
next(g) # => 'おはよう'
g.send('こんにちわ') # => 'こんにちわ'
next(g) # => 'こんにちわ'
next(g) # => Error!

# 他にも
# throw() で例外を送りつける
# close() で打ち切り
# などできるらしいけどまだよーわからん

# lambda(即時関数) 引数: 戻り値 と書く
sum = lambda a, b: a + b
sum(1, 2) # => 3

# デコレータ 高階関数を便利というか見やすくと言うか、そんな感じでかける
def deco_func(func):
    def new_func(*args, **kwargs):
        print('start')
        print(func(*args, **kwargs))
        print('end')

    return new_func

# こんな感じでデコレーションしたい関数の上に@関数名でOK
@deco_func
def sum(a, b):
    return a + b
```
