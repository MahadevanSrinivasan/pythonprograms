def buildDict(words):
  worddict = {}
  for i in xrange(len(words)):
    for j in xrange(len(words[i])):
      bucket = words[i][:j] + '_' + words[i][j+1:]
      if(bucket in worddict):
        worddict[bucket].append(words[i])
      else:
        worddict[bucket] = [words[i]]
  return worddict

words = ['pope', 'rope', 'nope', 'hope', 'lope',
         'mope', 'cope', 'pipe', 'pape', 'pole',
         'pore', 'pose', 'poke', 'pops'];

print buildDict(words)
