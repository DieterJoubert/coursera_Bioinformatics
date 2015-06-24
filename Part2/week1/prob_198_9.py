def prob_198_9():
  lines = open("dataset_198_9.txt").read().splitlines()

  kmers = []
  for i in range(len(lines)):
    kmers.append(lines[i])

  fout = open("out.txt", "w")
  for key, value in OverlapGraph(kmers).items():
    if value != []:
      fout.write(key + " -> " + value[0] + "\n")
  fout.close() 

def OverlapGraph(kmers):
  graph = {}
  for kmer in kmers:
    graph[kmer] = []

  for key_source in graph:
    for key_to in graph:
      if key_source == key_to:
        continue
      if key_source[1:] == key_to[0:0+len(key_source[1:])]:
        graph[key_source] = graph[key_source] + [key_to]

  return graph


if __name__ == '__main__':
  prob_198_9()