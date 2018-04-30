# Python cheat sheet

## `2`と`3`

破壊的変更がきつくて移行がおくれまくってるけど、最近はmacでも3が標準になったらしい

この項は`3`でいく

## 環境について

`pyenv`でPythonそのものの管理  
`venv`ないし`virtualenv`で実行環境(使用するPythonとライブラリ)の管理を行う  
`pip`でライブラリのインストールとか

で、これらをまとめて`pipenv`で管理するのがモダンな雰囲気

### 構築

```bash
# .zshrc

# recommended setting: use local dir
PIPENV_VENV_IN PROJECT=1
```

```bash
# install global pip
pip install pipenv
pip3 install pipenv
# create virtual environment(v3)
pipenv --three
# install all libraries
pipenv install
# manual install 
pipenv install numpy
# manual install (development tools)
pipenv install -d flake8 yapf ipython
# remove library
pipenv uninstall numpy
# enable venv
pipenv shell
# run Pipfile's [scripts] or global commands
pipenv run COMMAND
```

`Pipfile`が要するにGemfile `toml` format  
`Pipfile.lock`が要するにGemfile.lock `json` format  
環境変数はデフォルトで `.env` に対応しているらしい

#### Pipfileの書式

```toml
# libraries source url
[[source]]
url = "https://pypi.python.org/simple"
verify_ssl = true
name = "pypi"

# pipenv run XXX
[scripts]
test = "unittest"

# Dependencies libraries
[packages]
numpy = "*"

# Devendencies libraries (for development)
[dev-packages]
yapf = "*"
"flake8" = "*"
ipython = "*"
jedi = "*"
neovim = "*"

# Python version
[requires]
python_version = "3.6"
```

#### 以下、手動pip&venv(deprecated!)

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

##### pipについて

venv環境下でいじってもローカルにしか反映されないけど何も考えずに実行するとグローバルに入るので注意。  
グローバルに入れるものはあんまりないと思う。後述するIPythonくらいでいいのでは？

`requirements.txt`というファイルに依存モジュールを保存するのがマナー。

ただし、もうpipenvでええのでわ

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
# 詳しくは後ほど

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
# numbers 基底クラスなので型判定に使う
# ちなみに、見ての通りtypeはそのものをチェック、isinstanceは親クラスでもOK
import numbers
type(1.2e-3) == float # => True
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

### クラス

```python
# ざくっとこんな感じ
class Calc():
    # static variable
    pi = 3.141592

    # static method
    @staticmethod
    def is_same(calc1, calc2):
        return calc1.value == calc2.value

    # create instance (fire before constructor)
    # TODO: im not understand this
    # def __new__(cls):
    #     print('create instance')

    # constructor
    def __init__(self, initial_value=0):
        self.value = initial_value

    # instance method
    def add(self, val):
        self.value += val
        return self.value

    # attach self class(class method)
    @classmethod
    def create(cls):
        return cls()

    # like toString
    def __str__(self):
        return str(self.value)

    # destructor: NOT recommended use this
    # why?
    # * can't know when called
    # * can't guarantee called
    def __del__(self):
        self.value = None

# use instance var
Calc.pi # => 3.141592
# create class instance
calc = Calc()
# ...and use
calc.value # => 0
calc.pi # => 3.141592
calc.add(10) # => 10
calc.add(10) # => 20
str(calc) # => '20'
print(calc) # => '20'
# use static method
Calc.is_same(Calc(), Calc(100)) # => False
# add instance var...
calc.append_value = 10_000
calc.append_value # => 10000
# remove instance var...
del calc.append_value
calc.append_value # => AttributeError!

# create Blank class
class BlankClass: pass

blank = BlankClass()
blank.value = 100
blank.value # => 100 ...blank class's useful usecase?
```

継承

```python
class Base:
    def f1(self):
        print('f1')

    def f3(self):
        print('f3')

# set variable parent class 
class Sub(Base):
    def f2(self):
        print('f2')

    def f1and2(self):
        super().f1()
        self.f2()
    
    # override
    def f3(self):
        print('overrided f3')

# extends multiple
class Base1:
    def f1(self):
        print('f1')

class Base2:
    def f2(self):
        print('f2')

class Sub(Base1, Base2):
    def func(self):
        super().f1()
        super().f2()
```

プライベートメンバー  
慣習的にアンスコ始まりはプライベートとみなすのが一般的(アクセスは可能)  
アンスコ2つはじまりかつ末尾がアンスコ1つ以下の場合は外部アクセスすると**AttributeError**が発生する(がんばればアクセス不能)

100%信用できるわけじゃないけど、アンスコ2つは普通に使えばいいと思う

```python
class Calc():
    # constructor
    def __init__(self, initial_value=0):
        # private member
        self.__value = initial_value

calc.__value # => AttributeError
calc._Calc__value # => 100
```

プロパティ  
Decoratorでいい感じに書ける

```python
import numbers

class Calc():
    def __init__(self, initial_value=0):
        self.__value = initial_value

    # calc.value
    @property
    def value(self):
        return self.__value

    # calc.value = 100
    @value.setter
    def value(self, value):
        if isinstance(value, numbers.Number):
            self.__value = value

    # del calc.value
    @value.deleter
    def value(self):
        pass

calc = Calc(100)
calc.value # => 100
calc.value = 1000
calc.value # => 1000
del calc.value
calc.value # => None
```

ディスクリプタ  
**\_\_get__**  
**\_\_set__**  
**\_\_delete__**  
これらのメンバを持つオブジェクトへアクセスした際の挙動をカスタムできる

```python
class Money:
    def __init__(self):
        self.__price = 0

    def __get__(self, instance, owner):
        return self.__price

    def __set__(self, instance, price):
        self.__price = price

    def __delete__(self, instance):
        del self.__price
        print('losted...')

class You:
    def __init__(self):
        self.money = Money()

you = You();
you.money = 10000
print(you.money)
del you.money
print(you.money) # TODO: not active why?
```

クラスデコレータ  
関数と同じようなもん

```python
# 引数にクラスをとる関数
# TODO: もっといい感じのサンプル
def add_member(cls):
    cls.x = 'hello'
    return cls

# ↑を@つきで上に書くとデコレータとなる
@add_member
class Sample:
    pass

obj = Sample() # Sampleクラスをインスタンス化する 
obj.x # => hello
```

クラスの特殊メソッド一覧  
toString的なもの

| method name | desc |
|-------------|------|
|\_\_repr__(self)|オブジェクト情報を表す文字列|
|\_\_str__(self)|Python版toString|
|\_\_bytes__(self)|byte型に変換(TODO: 使えなかった)|
|\_\_format__(self, format_spec)|書式指定文字列format_specに準じた文字列に変換|
|\_\_hash__(self)|ハッシュ値(整数)に変換|
|\_\_bool__(self)|オブジェクトの比較用(TODO: 使えなかった)|

比較演算用メソッド  
それぞれの比較演算子で比較した際に発火する

| operator | method name (self, target) |
|---|---|
|==|\_\_eq__|
|!=|\_\_ne__|
|<|\_\_lt__|
|<=|\_\_le__|
|>|\_\_gt__|
|>=|\_\_ge__|

同じ要領で数値演算用メソッド  

| operator | method name (self, target) |
|---|---|
|+|\_\_add__|
|-|\_\_sub__|
|*|\_\_mul__|
|/|\_\_truediv__|
|//|\_\_floordiv__|
|%|\_\_mod__|
|divmod()|\_\_divmod__|
|**|\_\_pow__|
|<<|\_\_lshift__|
|>>|\_\_rshift__|
|&|\_\_and__|
|^|\_\_xor__|
|\||\_\_or__|

他にも色々あるので[公式ドキュメント](https://docs.python.jp/3.5/reference/datamodel.html#emulating-numeric-types)  
\_\_str__なんかは実装しといたほうがいいよね やっぱり

### 例外

```python
# Python's try~catch~finally
try:
    print(100 / 0)
except ZeroDivisionError as error:
    print('割り算なのに0')
except Exception as error:
    print('その他のエラー')
    print(type(error))
    print(str(error))
else:
    print('エラーなかった！')
finally:
    print('共通でここ通る')

# Python's throw
import numbers
def sum(a, b):
    if not isinstance(a, numbers.Number):
        raise TypeError('aがNumberではありません')
    elif not isinstance(b, numbers.Number):
        raise TypeError('bがNumberではありません')

    return a + b

# Python's custom error
class CurseNumberError(Exception):
    pass

def check_number(num):
    if num == 666:
        raise CurseNumberError('呪いの数字です')

    return True

check_number(1) # => True
check_number(666) # => CurseNumberError!
```

ファイル操作

```python
# Bad: Basic pattern
f = open('memo/sample.txt', 'r')   # Read mode
# f = open('memo/sample.txt', 'r') # Write mode
# f = open('memo/sample.txt', 'r') # Append mode
# f = open('memo/sample.txt', 'r') # Read&Write mode
# f = open('memo/sample.txt', 'r', encoding='shift_jis') # use sjis
print(f.read()) # output all text
f.write('Hello, it is python script.') # output text
f.close()

# Good: use 'with' statement
with open('memo/sample.txt', 'w') as f:
    f.write('Hello, it is python script.') # output text

# exists
import os
path = '/usr/local/bin/python3'

if not os.path.exists(path):
    print('not found path')
elif os.path.isfile(path):
    print('file path')
elif os.path.isdir(path):
    print('dir path')
else:
    raise(Exception('Unknown file: not file&dir.'))

# remove file
import os
os.remove('file.txt') # remove file
os.remove('dir') # Error! PermissionError

# create dir
import os
os.mkdir('parent')          # mkdir
os.makedirs('parent/child') # mkdirp

# remove dir
import os
os.rmdir('parent')            # rmdir enable empty dir only
os.removedirs('parent/child') # rmdirp

# copy
import shutil
shutil.copy('docs/CheatSheet.md', 'dummy.md') # => dummy.md, and copied file
shutil.copytree('docs', 'dummy') # => dummy, and copied dir
```

文字列について

```python
# concat
'Hello' + 'World' # => HelloWorld
'Hello' + str(100) # => Hello100
# listをjoin
' '.join(('Arsenal', 'Football', 'Club')) # => Arsenal Football Club
# split
'Arsenal Football Club'.split(' ') # => ['Arsenal', 'Football', 'Club']
# replace
'Apple Computer'.replace('Apple', 'Microsoft') # => Microsoft Computer
# get char/string
'Apple'[0] # => A
'Apple'[3] # => l
'Apple'[-1] # => e
'Apple'[1:3] # => pp
'Apple'[:3] # => App
'Apple'[2:] # => ple
'Apple'[:-1] # => Appl
# includes
'pl' in 'Apple' # => True
'APPLE' in 'Apple' # => False
# loop
for c in 'Apple':
    print(c)
# search
'Apple'.find('pl') # => 2
'Apple'.rfind('pl') # => 2
# count
'Apple'.count('p') # => 2
# trim
' Apple   '.strip() # => 'Apple'
' Apple   '.lstrip() # => 'Apple   '
' Apple   '.rstrip() # => ' Apple'
# Upper/Lower
'ApPlE'.upper() # => 'APPLE'
'ApPlE'.lower() # => 'apple'
'ApPlE'.capitalize() # => 'APPLE'

# Checker
# isalnum => /a-zA-Z0-9/
# isalpha => /a-zA-Z/
'1a'.isalnum() # => True
'1a'.isalpha() # => True
'あ'.isalnum() # => True!!!!!
'あ'.isalpha() # => True!!!!!
'あ'.encode('utf-8').isalnum() # => False
'あ'.encode('utf-8').isalpha() # => False
# isdecimal
# isdigit
# isnumeric
# いずれも微妙
'1'.isdigit() # => True
'1'.isdecimal() # => True
'1'.isnumeric() # => True
'-0.01'.isdigit() # => False!!!!!!!!!!
'-0.01'.isdecimal() # => False!!!!!!!!!!
'-0.01'.isnumeric() # => False!!!!!!!!!!
'0.01'.isdigit() # => False
'0.01'.isdecimal() # => False
'0.01'.isnumeric() # => False
'0٠01'.isdigit() # => True!!!!!!!!!!
'0٠01'.isdecimal() # => True!!!!!!!!!!
'0٠01'.isnumeric() # => True!!!!!!!!!!
'１'.isdigit() # => True
'１'.isdecimal() # => True
'１'.isnumeric() # => True
'百'.isdigit() # => False
'百'.isdecimal() # => False
'百'.isnumeric() # => True
'Ⅳ'.isdigit() # => False
'Ⅳ'.isdecimal() # => False
'Ⅳ'.isnumeric() # => True
# いずれも使いものにならないため、とりあえず変換して例外を拾うのが早い
def is_int(num_str, default=0):
    try:
        return (True, int(num_str))
    except ValueError:
        return (False, default)

is_int('いちおく', 1_000_000_000) # => (False, 1000000000)
is_int('-10') # => (True, 10)
is_int('1E20') # => (False, 0)

# string format
# >= 3.6
f'Oh, it\'s nice!: Python{3.6}' # => "Oh, it's nice!: Python3.6"
# >= 3
'{0}, {1}, {2}'.format('Zero', 'One', 'Two') # => 'Zero, One, Two'
# 2.x
'%s, %s, %s' % ('Zero', 'One', 'Two') # => 'Zero, One, Two'
'%(first)s, %(second)s, %(third)s' % {'first': 'Zero', 'second': 'One', 'third': 'Two' } # => 'Zero, One, Two'
```

### モジュール

```python
# 全部引っ張る
import math
math.pi # => 3.141592...
# ピンポイントで引っ張る
# from モジュール名 import ターゲット
from math import pi
pi # => 3.141592...
# 別名を付けて引っ張る
import numpy as np
# from numpy import random as ran # これもできる
np.random.rand(50)
```

#### 自作モジュール

```python
# ~/src/add.pyに定義されているaddとmulをindex.pyから引っ張る
# import src # 冗長な書き方なので以下のように書くべき
from src.add import add, mul
# import src.add as my_add こういうのもありだと思う
add(1, 2) # => 3
mul(1, 2) # => 2
# 古いpython(3.3以前)だとディレクトリの中に__init__.pyってファイルが必要だったみたいだけど、もう今はいらない
# 3.3は2012年9月29日リリースなのでもういいでしょう

```

モジュール利用時に`__pycache__`というコンパイル結果のキャッシュディレクトリが作成されてウンウンカンヌン  
venv環境下だと`lib/pythonX.X/__pycache__`にできるっぽい  
あんま意識することもないか 省略

`__name__` という特殊変数にはそのファイルが実行された際のモジュール名がはいる  
ただしエントリーポイントの場合は`__main__`という文字列が入る ので、

```python
if __name__ == '__main__':
    print('run from this file')
```

とか書くと直叩きの際にのみこの文字列が実行される

### 定番モジュール

#### OrderedDict

dict型(っぽい)のに順序が保証されるというphpのdictみたいなものである

**コンストラクタで値を突っ込むと順序が保証されない**ので気をつける

```python
from collections import OrderedDict
data_dict = OrderedDict()
data_dict['apple'] = 100
data_dict['orange'] = 80
data_dict['banana'] = 70

for key, val in data_dict.items():
    print(key, val) # => apple 100, orange 80, banana 70

# これなら保証されるらしい
data_dict = OrderedDict([['apple', 100], ['orange', 80], ['banana', 70]])
for key, val in data_dict.items():
    print(key, val)
```

#### 日時関係

すべて`datetime`モジュールに入っている

|name     |task       |
|:--------|:----------|
|date     |年月日     |
|time     |時分秒     |
|datetime |date + time|
|timedelta|経過時間   |

```python
# datetime
from datetime import datetime, timedelta

datetime.now() # => CURRENT DATETIME
# required ymd!
datetime(2018, 4, 30) # => 2018-4-30 00:00:00
datetime(year=2018, month=4, day=30) # => 2018-4-30 00:00:00
datetime.strptime('2018-04-30', '%Y-%m-%d') # => 2018-4-30 00:00:00
# option args
datetime(2018, 4, 30, 10, 0) # => 2018-4-30 10:00:00
datetime(2018, 4, 30, minute=10) # => 2018-4-30 00:10:00
datetime.strptime('2018-04-30 10:20:30', '%Y-%m-%d %H:%M:%S') # => 2018-4-30 00:00:00
# get values
dt = datetime(2018, 4, 30, 10, 20, 30, 123) # => 2018-04-30 10:20:30.000123
str(dt) # => 2018-04-30 10:20:30.000123
dt.year # => 2018
dt.month # => 4
dt.day # => 30
dt.hour # => 10
dt.minute # => 20
dt.second # => 30
dt.microsecond # => 123
dt.strftime('%A %Y/%m/%d %H:%M:%S') # => Monday 2018/04/30 10:20:30
# calc
delta = datetime(2018, 6, 1) - datetime(2018, 5, 15, 20, 39, 32, 1234)
delta.days # => 16
delta.seconds # => 12027
delta.microseconds # => 998766
delta.total_seconds() # => 1394427.998766
str(delta) # => 16 days, 3:20:27
(datetime(2018, 6, 1) - timedelta(days=1)).strftime('%A %Y/%m/%d') # => Thursday 2018/05/31


```

`strptime`, `strftime` の書式については[ここ](https://docs.python.jp/3/library/datetime.html#strftime-strptime-behavior) Cと同じ

```python
# date
# required ymd!
from datetime import date, datetime
date(2018, 4, 30) # => 2018-4-30
date(year=2018, month=4, day=30) # => 2018-4-30
# not have strptime. cast from datetime
datetime.strptime('2018-04-30', '%Y-%m-%d').date() # => 2018-4-30

# time
from datetime import time, datetime
time(10) # => 10:00:00
time(hour=10, second=20) # => 10:00:20
# not have strptime. cast from datetime
datetime.strptime('10:20:30', '%H:%M:%S').time() # => 10:20:30
```

#### json

`json` を使う

```python
import json

# Pythonの値をJSON形式の文字列へ変換
json.dumps(
    # この例はdictだがかなりなんでもOK tuple, OrderedDict, boolean...
    {
        'user': {
            'name': '山田太郎',
            'age': 30,
            'height': 172,
            'weight': 62
        }
    },
    indent=2,   # 出力結果にインデントをつける デフォルトはなし(つけない)
    ensure_ascii=False, # 出力結果をアスキーエンコードするか 日本語含む場合はしないとえらいことに デフォルトTrue
    sort_keys=True # 出力のたびに順番が変わるのが嫌ならsortする デフォルFalse
)

# JSON形式の文字列からPythonの値へ変換
json.loads('{"items": [{"id": 1, "name": "ペン"}, {"id": 2, "name": "アップル"}, {"id": 3, "name": "パイナップル"}], "status": "sell"}')

# JSONファイルを読み込む
with open('./memo/dummy.json', 'r') as f:
    print(json.load(f))
```

#### configparser

`.ini`ファイル形式で設定ファイルを作るのがデフォらしい 拡張子は`.conf`ﾄﾉｺﾄ

```python
from configparser import ConfigParser
conf = ConfigParser()
conf.read('memo/dummy.conf')

# get [TEST] section
test = conf['TEST']
test.get('message') # => im lucky
test.getint('num') # => 10
test.getboolean('iam') # => True
test.get('nothing', 'to say') # => to say: use default value
```
