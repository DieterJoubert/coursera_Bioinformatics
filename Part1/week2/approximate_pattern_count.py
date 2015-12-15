from hamming_distance import *

def approximate_pattern_count(text, pattern, d):
  count = 0
  for i in range(len(text)-len(pattern)+1):
    window = text[i:i+len(pattern)]
    if hamming_distance(pattern, window) <= d:
      count += 1
  return count