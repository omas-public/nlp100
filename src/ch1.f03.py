def f03(s):
  strip_punctuation = lambda w : "".join([c for c in w if c.isalnum()])
  return list(map(len, list(map(strip_punctuation, s.split()))))
