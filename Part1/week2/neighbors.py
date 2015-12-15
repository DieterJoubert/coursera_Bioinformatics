from hamming_distance import *

def neighbors(pattern, d):
  nucleotides = ["A", "C", "G", "T"]

  if d == 0:
    return [pattern]
  if len(pattern) == 1:
    return nucleotides

  neighborhood = []
  suffix_neighbors = neighbors(pattern[1:], d)
  for text in suffix_neighbors:
    if hamming_distance(pattern[1:], text) < d:
      for x in nucleotides:
        neighborhood.append(x + text)
    else:
      neighborhood.append(pattern[0] + text)
  return neighborhood