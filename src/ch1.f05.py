def f05(target):
  str2charlist = lambda s: [c for c in s]
  str2wordlist = lambda s: [w for w in s.split()]
  ngram = lambda n: lambda tl: [''.join(tl[i:i + n]) for i in range(len(tl) - n + 1)]
 
  bigram = ngram(2)
  print(bigram(str2charlist(target)))
  print(bigram(str2wordlist(target)))

f05('I am an NLPer')