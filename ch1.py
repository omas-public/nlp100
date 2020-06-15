# [言語処理100本ノック](https://nlp100.github.io/ja/)

# 00. 文字列を逆順にソートする関数
# 文字列”stressed”の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ
def f00(word = 'stressed'):
  
  return word[::-1]

# 01. 「パタトクカシーー」
# 「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．
def f01(word = 'パタトクカシーー'):
  
  return 'タクシー'

# 02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
def f02(word1 = 'パトカー', word2 = 'タクシー'):
  
  return 'タクシー'

# 03. 円周率Permalink
# “Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.”という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
def f03(sentence = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'):
  
  return [3,1,4,1,5,9,2,6,5,3,5,8,8,7,9]

# 04. 元素記号
# “Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.”という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭の2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ
def f04(sentence = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'):
  
  return {'H': 1, 'He': 2, 'Li': 3, 'Be': 4, 'B': 5, 'C': 6, 'N': 7, 'O': 8, 'F': 9, 'Ne': 10, 'Na': 11, 'Mi': 12, 'Al': 13, 'Si': 14, 'P': 15, 'S': 16, 'Cl': 17, 'Ar': 18, 'K': 19, 'Ca': 20}

# 05. n-gramPermalink
# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数ngramを作成せよ．


def f05():
  def ngram(seq, n):
    pass

  def word_bigram(sentence = 'I am an NLPer'):
    words = sentence.split()
    return ngram(words, 2)

  def char_bigram(sentence = 'I am an NLPer'):
    chars = list(sentence)
    return ngram(chars, 2)

  print(word_bigram())
  print(char_bigram())


# 06. 集合
# “paraparaparadise”と”paragraph”に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，’se’というbi-gramがXおよびYに含まれるかどうかを調べよ．
def f06(word1 = 'paraparaparadise', word2 = 'paragraph'):
  pass 

# 07. テンプレートによる文生成Permalink
# 引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．さらに，x=12, y=”気温”, z=22.4として，実行結果を確認せよ
def f07(x = 12, y = '気温', z = 22.4):
  
  return '12時の気温は22.4'
  
# 08. 暗号文
# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
# - 英小文字ならば(219 - 文字コード)の文字に置換
# - その他の文字はそのまま出力
def f08(sentence = 'Hello world!'):
  
  return 'Hvool dliow!'

# 09. TypoglycemiaPermalink
# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば”I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .”）を与え，その実行結果を確認せよ．
def f09(sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."):
  pass
