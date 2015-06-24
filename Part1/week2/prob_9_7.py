def prob_9_7():
  lines = open("dataset_9_7.txt").read().splitlines()

  text = lines[0]
  
  kd = lines[1].split()
  k = int(kd[0])
  d = int(kd[1])

  fout = open("out.txt", "w")
  fout.write( " ".join(FrequentWordsWithMismatches(text, k, d)) )
  fout.close() 

def FrequentWordsWithMismatches(Text, k, d):
  kmers_count = {}
  for i in range(len(Text)-k):
    kmer = Text[i:i+k]

    kmer_approx = DMatches(kmer, d)

    for check_mer in kmer_approx:
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
          if new_string not in matches:
            d_matches.append(new_string)
    count += 1

  return d_matches

if __name__ == '__main__':
  prob_9_7()