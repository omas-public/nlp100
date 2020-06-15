def f06(word1 = 'paraparaparadise', word2 = 'paragraph'):
  ngram = lambda n: lambda tl: [''.join(tl[i:i + n]) for i in range(len(tl) - n + 1)]
  X = set(ngram(2)(list(word1)))
  Y = set(ngram(2)(list(word2)))

  print(X.union(Y))
  print(X.difference(Y))
  print(X.intersection(Y))

