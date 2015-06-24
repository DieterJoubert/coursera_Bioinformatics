def prob_156_7():
  lines = open("dataset_156_7.txt").read().splitlines()
  kd = lines[0].split()
  k = int(kd[0])
  d = int(kd[1])

  dna = []
  for i in range(1,len(lines)):
    dna.append(lines[i])

  print dna

  fout = open("out.txt", "w")
  fout.write(" ".join(MotifEnumeration(dna, k, d)))
  fout.close()

def MotifEnumeration(Dna, k, d):
  Patterns = []
  for dna_string in Dna:
    for i in range(len(dna_string)-k):
      pattern = dna_string[i:i+k]
      pattern_neighbors = Neighbors(pattern, d)

      for pattern_star in pattern_neighbors:
        if InAll(Dna, pattern_star, d):
          Patterns.append(pattern_star)

  return list(set(Patterns))

def InAll(dna, pattern, d):
  for dna_string in dna:
    found = False
    for i in range(len(dna_string)-len(pattern)+1):
      kmer = dna_string[i:i+len(pattern)]
      if HammingDistance(kmer, pattern) <= d:
        found = True
        break
    if found == False:
      return False
  return True

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

  return neighborhood

def HammingDistance(string1, string2):
  hamm = 0
  for i in range(len(string1)):
    if string1[i] != string2[i]:
      hamm += 1
  return hamm

if __name__ == '__main__':
  prob_156_7()