def nearby_permutations(letters, index):
  if(index >= len(letters)):
    return [""]

  subwords = nearby_permutations(letters, index + 1)
  nearbyletters = get_nearby_letters(letters[index])
  permutations = [] 

  for subword in subwords:
    for nearbyletter in nearbyletters:
      permutations.append(subword + nearbyletter)

  return permutations

def get_nearby_letters(letter):
  if(letter == 'g'):
    return ['g', 'h', 'f']
  else:
    return ['i', 'o', 'k']


letters = ['g', 'i']
print nearby_permutations(letters, 0)
