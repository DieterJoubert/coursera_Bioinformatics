def computing_frequencies(text, k):
  frequency_array = []
  for i in range(0,4**k):
    frequency_array.append(0)
  for i in range(0,len(text)-k+1):
    pattern = text[i:i+k]
    j = pattern_to_number(pattern)
    frequency_array[j] += 1
  return frequency_array

def pattern_to_number(pattern):
  number = 0
  freq_dict = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
  for i in range(len(pattern)):
    number += freq_dict[pattern[len(pattern)-i-1]] * (4**i)
  return number