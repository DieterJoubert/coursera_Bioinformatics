def ImmediateNeighbors(Pattern):
  neighborhood = [Pattern]
  DNA = ['A', 'C', 'G', 'T']
  for i in range(len(Pattern)):
    symbol = Pattern[i]
    for nucleotide in DNA:
      if nucleotide == symbol:
        continue
      neighbor = Pattern[0:i] + nucleotide + Pattern[i+1:]
      neighborhood.append(neighbor)

  return list(set(neighborhood))

def Neighbors(Pattern, d):
  if d == 0:
    return [Pattern]
  if len(Pattern) == 1:
    return ['A', 'C', 'G', 'T']

  DNA = ['A', 'C', 'G', 'T']      
  neighborhood = []
  suffix_neighbors = Neighbors(Pattern[1:], d)
  for string in suffix_neighbors:
    if HammingDistance(Pattern[1:], string) < d:
      for nucleotide in DNA:
        neighborhood.append(nucleotide + string)
    else:
      neighborhood.append(Pattern[0] + string)

  """
  fout = open("out.txt", "w")
  for s in neighborhood:
    fout.write(s + "\n")
  fout.close() 
  """

  return neighborhood

def HammingDistance(string1, string2):
  hamm = 0
  for i in range(len(string1)):
    if string1[i] != string2[i]:
      hamm += 1
  return hamm