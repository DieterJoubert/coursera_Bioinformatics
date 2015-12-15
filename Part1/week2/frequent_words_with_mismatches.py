from pattern_to_number import *
from number_to_pattern import *
from neighbors import *
from hamming_distance import *
from approximate_pattern_count import *

def frequent_words_with_mismatches(text, k, d):
  frequent_patterns = []
  close = [0] * (4**k)
  frequency_array = [0] * (4**k)

  for i in range(0,len(text)-k+1):
    neighborhood = neighbors(text[i:i+k], d)
    for pattern in neighborhood:
      index = pattern_to_number(pattern)
      close[index] = 1

  for i in range(0,4**k):
    if close[i] == 1:
      pattern = number_to_pattern(i, k)
      frequency_array[i] = approximate_pattern_count(text, pattern, d)

  max_count = max(frequency_array)

  for i in range(0,4**k):
    if frequency_array[i] == max_count:
      pattern = number_to_pattern(i, k)
      if pattern not in frequent_patterns:
        frequent_patterns.append(pattern)

  return frequent_patterns