def pattern_to_number(pattern):
  number = 0
  freq_dict = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
  for i in range(len(pattern)):
    number += freq_dict[pattern[len(pattern)-i-1]] * (4**i)
  return number