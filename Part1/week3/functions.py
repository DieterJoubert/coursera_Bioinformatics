def number_to_pattern(number,k):      
  num_to_symbol = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
  if k == 1:
    return num_to_symbol[number]
  quotient = number / 4
  remainder = number % 4
  symbol = num_to_symbol[remainder]
  prefix_pattern = number_to_pattern(quotient,k-1)
  return prefix_pattern + symbol  

def neighbors(pattern, d):
  """Given a DNA string, pattern, returns a list of all patterns
  differening from pattern by at most d mismatches"""
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

def hamming_distance(str_1, str_2):
  """Given two strings of equal length, finds the number of character
  differences between the two and returns difference as int"""
  mismatches = 0
  if len(str_1) != len(str_2):
    raise ValueError('Strings are not of equal length')
  for i in range(len(str_1)):
    if str_1[i] != str_2[i]:
      mismatches += 1
  return mismatches

def distance_between_pattern_and_strings(pattern, dna):
  k = len(pattern)
  distance = 0
  for text in dna:
    hamm_distance = float("inf")
    for i in range(len(text)-k+1):
      pattern_star = text[i:i+k]
      if hamm_distance > hamming_distance(pattern_star, pattern):
        hamm_distance = hamming_distance(pattern_star, pattern)
    distance += hamm_distance
  return distance

def approximately_contained(text, pattern, d):
  """Given two strings, pattern and text, this checks whether the kmer
  can be approximately found in any k-length window of the text"""
  k = len(pattern)
  for i in range(len(text)-k+1):
    window = text[i:i+k]
    if hamming_distance(pattern, window) <= d:
      return True
  return False

def approximate_pattern_count(text, pattern, d):
  count = 0
  for i in range(len(text)-len(pattern)+1):
    window = text[i:i+len(pattern)]
    if hamming_distance(pattern, window) <= d:
      count += 1
  return count

#####################################################################

def motif_enumeration(dna, k, d):
  patterns = []
  for dna_string in dna:
    for i in range(len(dna_string)-k+1):
      pattern = dna_string[i:i+k]
      pattern_neighbors = neighbors(pattern, d)
      for pattern_star in pattern_neighbors:
        in_each = True
        for elmt in dna:
          if not approximately_contained(elmt, pattern_star, d):
            in_each = False
        if in_each:
          patterns.append(pattern_star)
  return list(set(patterns))

#####################################################################

def median_string(dna, k):
  distance = float("inf")
  for i in range(0,4**k):
    pattern = number_to_pattern(i,k)
    if distance > distance_between_pattern_and_strings(pattern, dna):
      distance = distance_between_pattern_and_strings(pattern, dna)
      median = pattern
  return median

#####################################################################

def profile_most_probable_kmer(text, k, profile):
  char_to_index = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
  best_kmer = None
  best_prob = 0
  for i in range(len(text)-k+1):
    window = text[i:i+k]
    prob = float(1)
    for j in range(len(window)):
      char = window[j]
      index = char_to_index[char]
      prob = prob * profile[index][j]
    if prob > best_prob:
      best_prob = prob
      best_kmer = window

  if best_kmer == None:
    return text[0:k]
  return best_kmer

#####################################################################

def score(motifs):
  score = 0
  for i in range(len(motifs[0])):
    count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for mot in motifs:
      count[mot[i]] += 1
    (best_found, best_count) = (None, 0)
    for key, value in count.items():
      if value > best_count:
        (best_found, best_count) = (key, value)
    for key, value in count.items():
      if key != best_found:
        score += value
  return score

def create_profile(patterns):
  char_to_index = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
  profile = []
  for i in range(4):
    profile.append([])

  for i in range(len(patterns[0])):
    count = [0,0,0,0]
    total = 0
    for j in range(len(patterns)):
      count_index = char_to_index[patterns[j][i]]
      count[count_index] += 1
      total += 1
    for x in range(4):
      profile[x].append(float(count[x])/total)

  return profile

def greedy_motif_search(dna, k, t):
  best_motifs = []
  for string in dna:
    best_motifs.append(string[0:k])

  for index in range(len(dna[0])-k+1):
    motifs = [""] * t
    motifs[0] = dna[0][index:index+k]

    for i in range(1,t):
      profile = create_profile([item for item in motifs[:i]])
      motifs[i] = profile_most_probable_kmer(dna[i],k,profile)

    if score(motifs) < score(best_motifs):
      best_motifs = motifs

  return best_motifs

#####################################################################

def create_laplace_profile(patterns):
  char_to_index = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
  profile = []
  for i in range(4):
    profile.append([])

  for i in range(len(patterns[0])):
    count = [1,1,1,1]
    total = 4
    for j in range(len(patterns)):
      count_index = char_to_index[patterns[j][i]]
      count[count_index] += 1
      total += 1
    for x in range(4):
      profile[x].append(float(count[x])/total)

  return profile

def greedy_motif_search(dna, k, t):
  best_motifs = []
  for string in dna:
    best_motifs.append(string[0:k])

  for index in range(len(dna[0])-k+1):
    motifs = [""] * t
    motifs[0] = dna[0][index:index+k]

    for i in range(1,t):
      profile = create_laplace_profile([item for item in motifs[:i]])
      motifs[i] = profile_most_probable_kmer(dna[i],k,profile)

    if score(motifs) < score(best_motifs):
      best_motifs = motifs

  return best_motifs