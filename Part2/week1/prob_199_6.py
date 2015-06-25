def prob_199_6():
  lines = open("dataset_199_6.txt").read().splitlines()

  k = int(lines[0])
  string = lines[1]

  fout = open("out.txt", "w")
  for key, value in DeBruijnGraph(string, k).items():
    if value != []:
      fout.write(key + " -> " + ",".join(value) + "\n")  
  fout.close() 

def DeBruijnGraph(string, k):
  graph = {}
  comp = Composition(string, k)

  for kmer in comp:
    prefix = kmer[:-1]
    suffix = kmer[1:]
    if prefix not in graph:
      graph[prefix] = [suffix]
    else:
      graph[prefix] += [suffix]

  return graph

def Composition(text, k):
  kmers = []
  for i in range(len(text)-k+1):
    kmer = text[i:i+k]
    kmers.append(kmer)
  return kmers

if __name__ == '__main__':
  prob_199_6()