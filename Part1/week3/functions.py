def motif_enumeration(dna, k, d):
  patterns = []
  for i in range(len(dna)-k+1):
    pattern = dna[i:i+k]
    






def approximate_pattern_count(text, pattern, d):
  count = 0
  for i in range(len(text)-len(pattern)+1):
    window = text[i:i+len(pattern)]
    if hamming_distance(pattern, window) <= d:
      count += 1
  return count

def hamming_distance(str_1, str_2):
  mismatches = 0
  if len(str_1) != len(str_2):
    raise ValueError('Strings are not of equal length')
  for i in range(len(str_1)):
    if str_1[i] != str_2[i]:
      mismatches += 1
  return mismatches