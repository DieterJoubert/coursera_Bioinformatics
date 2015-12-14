import computing_frequencies as cf
from number_to_pattern import *

def clump_finding(genome, k, t, L):
  frequent_patterns = []
  clump = [0] * (4**k)
  for i in range(0,len(genome)-L+1):
    text = genome[i:i+L]
    frequency_array = cf.computing_frequencies(text,k)
    for index in range(0,4**k):
      if frequency_array[index] >= t:
        clump[index] = 1
  for i in range(0,4**k):
    if clump[i] == 1:
      pattern = number_to_pattern(i, k)
      frequent_patterns.append(pattern)
  return frequent_patterns