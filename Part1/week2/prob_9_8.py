def prob_9_8():
  lines = open("dataset_9_8.txt").read().splitlines()

  text = lines[0]
  
  kd = lines[1].split()
  k = int(kd[0])
  d = int(kd[1])

  fout = open("out.txt", "w")
  fout.write( " ".join(FrequentWordsWithMismatchesAndReverseCompliment(text, k, d)) )
  fout.close() 

def FrequentWordsWithMismatchesAndReverseCompliment(Text, k, d):
  kmers_count = {}
  for i in range(len(Text)-k):
    kmer = Text[i:i+k]

    kmer_approx = DMatches(kmer, d)

    for check_mer in kmer_approx:
      if check_mer in kmers_count:
        kmers_count[check_mer] += 1
      else:
        kmers_count[check_mer] = 1

  for i in range(len(Text)-k):
    kmer = Text[i:i+k]

    kmer_approx = DMatches(ReverseCompliment(kmer), d)

    for check_mer in kmer_approx:
      #check_mer = ReverseCompliment(mer)
      if check_mer in kmers_count:
        kmers_count[check_mer] += 1
      else:
        kmers_count[check_mer] = 1  

  max_value = 0

  for key, value in kmers_count.items():
    max_value = max(value, max_value)

  max_kmers = []
  for key, value in kmers_count.items():
    if value == max_value:
      max_kmers.append(key)

  return max_kmers

def DMatches(kmer, d):
  d_matches = [kmer]
  DNA = ['A', 'C', 'G', 'T']

  count = 0
  while count < d:
    import copy
    matches = copy.deepcopy(d_matches)

    for item in matches:
      for index in range(len(kmer)):
        for neu in DNA:
          new_string = item[0:0+index] + neu + item[index+1:]
          if new_string not in d_matches:
            d_matches.append(new_string)
    count += 1

  return d_matches

def ReverseCompliment(string_in):
  string_out = ""
  compliment = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C'
  }
  length = len(string_in)
  for i in range(length):
    string_out += compliment[string_in[length-i-1]]
  return string_out

if __name__ == '__main__':
  prob_9_8()