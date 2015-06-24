def count2(text, pattern):
  count = 0
  for i in range(len(text)-len(pattern)+1):
    if HammingDistance(pattern,text[i:i+len(pattern)]) <= 2:
      count += 1
  return count

def HammingDistance(string1, string2):
  hamm = 0
  for i in range(len(string1)):
    if string1[i] != string2[i]:
      hamm += 1
  return hamm

def MinSkewIndex(Genome):
  skew_table = []
  curr_skew = 0
  skew_table.append(curr_skew)
  for char in Genome:
    if char == 'G':
      curr_skew += 1
    elif char == 'C':
      curr_skew -= 1
    skew_table.append(curr_skew)

  min_skew = 0
  min_indices = []

  for skew in skew_table:
    min_skew = min(min_skew, skew)

  for i in range(len(skew_table)):
    if skew_table[i] == min_skew:
      min_indices.append(i)

  return min_indices

def count1(text, pattern):
  count = 0
  for i in range(len(text)-len(pattern)+1):
    if HammingDistance(pattern,text[i:i+len(pattern)]) <= 1:
      count += 1
  return count


def DMatches(kmer, d):
  d_matches = [kmer]
  DNA = ['A', 'C', 'G', 'T']

  count = 0
  while count < d:
    import copy
    matches = copy.deepcopy(d_matches)

    for item in matches:
      for index in range(len(kmer)):
        for neu in DNA:
          new_string = item[0:0+index] + neu + item[index+1:]
          if new_string not in d_matches:
            d_matches.append(new_string)
    count += 1

  return len(d_matches)