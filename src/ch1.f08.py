def f08(message):
  cipher = lambda c: chr(0xdb - ord(c)) if c.islower() else c

  return ''.join([cipher(c) for c in message])