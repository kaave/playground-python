# Python cheat sheat

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
# numeric _は無視される
1
1_000 # => 1000
# 文字列 シングル、ダブルどっちも同じ
'asd'
"asd"
# boolean 先頭が大文字
True
False
# Array よくある感じ
ary = [1, 2, 3]
ary2 = [1, 'two', 3]
ary[0] # => 1
# 足すとconcat
ary + ary2 # => [1, 2, 3, 1, 'two', 3]

# Hash キーは''でくくる
{'apple': 200, 'orange': 100, 'banana': 150}
# キーもバリューも変数使える
k = 'APPLE'
v = 'りんご'
{k: v} # => {'APPLE': 'りんご'}

# 変数はRubyとそっくり いきなり宣言OKとか
a = 10
b = a
a = 1
print(a, b) # => 1, 10 参照渡しじゃーない
# 複数いっぺんにいける
x, y, z = 1, 2, 3
a, b, c = x, y, z

# 定数はない 残念
```
