def prob_200_7():
  lines = open("dataset_200_7.txt").read().splitlines()

  kmers = []
  for i in range(len(lines)):
    kmers.append(lines[i])

  fout = open("out.txt", "w")
  for key, value in DeBruijnGraph(kmers).items():
    if value != []:
      fout.write(key + " -> " + ",".join(value) + "\n")
  fout.close() 

def DeBruijnGraph(kmers):
  graph = {}

  for kmer in kmers:
    prefix = kmer[:-1]
    suffix = kmer[1:]
    if prefix not in graph:
      graph[prefix] = [suffix]
    else:
      graph[prefix] += [suffix]

  return graph

if __name__ == '__main__':
  prob_200_7()