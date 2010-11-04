

import re, itertools, optparse

DEFAULT_REGEX = r'''(?x)
    [^a-zA-Z_](
        (?:_[a-zA-Z0-9_]+)|
        (?:[a-zA-Z_][a-zA-Z0-9_]*_CSS))'''


def main():
  
  parser = optparse.OptionParser()
  parser.add_option('-r', '--regex', dest='regex', default=DEFAULT_REGEX)
  options, args = parser.parse_args()
  
  code = sys.stdin.read()
  minified = minify(code, regex=options.regex)
  sys.stdout.write(minified)



def minify(code, regex=DEFAULT_REGEX):
  mapping = findMapping(code, regex=regex)
  for longName, shortName in mapping.items():
    code.replace(longName, shortName)
  return code


def findMapping(code, regex=DEFAULT_REGEX):
  
  mapping = {}
  
  longNames_freq = {}
  for m in re.finditer(regex, code):
    name = m.group(1)
    longNames_freq[name] = longNames_freq.get(name, 0) + 1
  
  shortNames_iter = gen_names()
  for longName, count in sorted(
                              longNames_freq.items(),
                              cmp=lambda x, y: -cmp(x[1], y[1])):
    for shortName in shortNames_iter:
      if code.find(shortName) == -1:
        print(count, longName, shortName)
        code = code.replace(longName, shortName)
        mapping[longName] = shortName
        break
  
  return mapping



# Sure, there's a general way to do this.
# But this way is more readable, harder too mess up,
# and (52**4 = 7,311,616 + ...) ought to be enough for anybody
def gen_names():
  
  ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
  
  for x1 in range(len(ALPHABET)):
    yield ''.join(ALPHABET[i] for i in [x1])
  
  for x1 in range(len(ALPHABET)):
    for x2 in range(len(ALPHABET)):
      yield ''.join(ALPHABET[i] for i in [x1, x2])
  
  for x1 in range(len(ALPHABET)):
    for x2 in range(len(ALPHABET)):
      for x3 in range(len(ALPHABET)):
        yield ''.join(ALPHABET[i] for i in [x1, x2, x3])
  
  for x1 in range(len(ALPHABET)):
    for x2 in range(len(ALPHABET)):
      for x3 in range(len(ALPHABET)):
        for x4 in range(len(ALPHABET)):
          yield ''.join(ALPHABET[i] for i in [x1, x2, x3, x4])


if __name__ == '__main__':
  main()
