def f04(s):
  within = lambda n : n in [1, 5, 6, 7, 8, 9, 15, 16, 19]
  get_letters = lambda pred, w: [w[:2], w[0]][pred]
  wt, wdic = ((i + 1, w) for i, w in enumerate(s.split())), {}
  
  for index, word in wt:
    wdic[get_letters(within(index), word)] = index

  return wdic


s = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'

print(f04(s))