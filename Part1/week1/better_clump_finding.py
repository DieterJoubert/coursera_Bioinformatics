from computing_frequencies import *
from number_to_pattern import *
from pattern_to_number import *

def better_clump_finding(genome, k, t, L):
  frequent_patterns = []
  clump = [0] * (4**k)

  text = genome[0:L]
  frequency_array = computing_frequencies(text,k)

  for i in range(0,4**k):
    if frequency_array[i] >= t:
      clump[i] = 1

  for i in range(1,len(genome)-L+1):
    first_pattern = genome[i-1:i-1+k]
    index = pattern_to_number(first_pattern)
    frequency_array[index] = frequency_array[index] - 1
    last_pattern = genome[i+L-k:i+L]
    index = pattern_to_number(last_pattern)
    frequency_array[index] = frequency_array[index] + 1

    if frequency_array[index] >= t:
      clump[index] = 1

  for i in range(0,4**k):
    if clump[i] == 1:
      pattern = number_to_pattern(i,k)
      if pattern not in frequent_patterns:
        frequent_patterns.append(pattern)

  return frequent_patterns
