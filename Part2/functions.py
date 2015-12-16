def composition_k(k,text):
  kmers = []
  for i in range(len(text)-k+1):
    window = text[i:i+k]
    kmers.append(window)
  return sorted(kmers)

#######################################################################

def overlap_adjacency_graph(patterns):
  adjacency_list = []
  for i in range(len(patterns)):
    for j in range(len(patterns)):
      if i == j:
        continue
      if patterns[i][1:] == patterns[j][:-1]:
        adjacency_list.append((patterns[i],patterns[j]))
  return adjacency_list

#######################################################################

def debruijn_k(k,text):
  graph = {}
  for i in range(len(text)-k+1):
    kmer = text[i:i+k]
    if kmer[:-1] in graph:
      graph[kmer[:-1]].append(kmer[1:])
    else:
      graph[kmer[:-1]] = [kmer[1:]]
  return graph

#######################################################################

def debruijn_from_kmers(patterns):
  graph = {}
  for kmer in patterns:
    if kmer[:-1] in graph:
      graph[kmer[:-1]].append(kmer[1:])
    else:
      graph[kmer[:-1]] = [kmer[1:]]
  return graph
