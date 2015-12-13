def PatternToNumber(pattern):
  string = reversed(pattern)
  value = {
    'A': 0,
    'C': 1,
    'G': 2,
    'T': 3
  }

  number = 0

  sig = 1
  for char in string:
    number += (value[char] * sig)
    sig = sig * 4

  return number

def NumberToPattern(number, k):
  string = ""

  num_to_symbol = {
    0: 'A',
    1: 'C',
    2: 'G',
    3: 'T'
  }

  while k >= 1:
    string += num_to_symbol[ number % (4 ** k) ] 
    k -= 1

  return string


def FrequentWords(Text, k):
  kmers_count = {}
  for i in range(0,len(Text)-k):
    kmer = Text[i:i+k]
    if kmer in kmers_count:
      kmers_count[kmer] += 1
    else:
      kmers_count[kmer] = 1

  max_value = 0
  for key, value in kmers_count.items():
    max_value = max(value, max_value)

  max_kmers = []
  for key, value in kmers_count.items():
    if value == max_value:
      max_kmers.append(key)

  return " ".join(max_kmers)