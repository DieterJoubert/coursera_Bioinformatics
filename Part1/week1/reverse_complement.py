def reverse_complement(pattern):
  complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
  reverse_complement = ""
  for i in range(len(pattern)):
    reverse_complement += complement_dict[pattern[len(pattern)-1-i]]
  return reverse_complement