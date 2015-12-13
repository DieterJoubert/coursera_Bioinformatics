def E_coli():
  """find all k-mers forming (L, t) clumps in genome"""  
  lines = open("E-coli.txt").read().splitlines()

  Genome = lines[0]

  k = 9
  L = 500
  t = 3

  fout = open("out.txt", "w")
  fout.write( str(len(FindClump(Genome, k, L, t))) )
  fout.close() 

def FindClump(Genome, k, L, t):
  """apply freq kmers to every window of length L"""
  result = []
  for i in range(len(Genome)):

    window_result = FrequentWords(Genome[i:i+L], k, t)
    for clump_kmer in window_result:
      if clump_kmer not in result:
        result.append(clump_kmer)
        print clump_kmer

  return result

def FrequentWords(Text, k, t):
  kmers_count = {}
  for i in range(len(Text)-k):
    kmer = Text[i:i+k]

    if kmer in kmers_count:
      kmers_count[kmer] += 1
    else:
      kmers_count[kmer] = 1

  max_kmers = []
  for key, value in kmers_count.items():
    if value >= t:
      max_kmers.append(key)

  return max_kmers

if __name__ == '__main__':
  E_coli()
