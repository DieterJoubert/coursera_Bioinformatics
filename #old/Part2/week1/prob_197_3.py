def prob_197_3():
  lines = open("dataset_197_3.txt").read().splitlines()
  k = int(lines[0])
  string = lines[1]

  fout = open("out.txt", "w")
  composition = Composition(string, k)
  for s in composition:
    fout.write(s + "\n")
  fout.close() 

def Composition(text, k):
  kmers = []
  for i in range(len(text)-k+1):
    kmer = text[i:i+k]
    kmers.append(kmer)
  return sorted(kmers)

if __name__ == '__main__':
  prob_197_3()