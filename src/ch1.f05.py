def f05(target):
  str2charlist = lambda s: list(s)
  str2wordlist = lambda s: s.split()
  ngram = lambda n: lambda tl: [''.join(tl[i:i + n]) for i in range(len(tl) - n + 1)]
 
  bigram = ngram(2)
  print(bigram(str2charlist(target)))
  print(bigram(str2wordlist(target)))

