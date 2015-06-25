def prob_198_3():
  lines = open("dataset_198_3.txt").read().splitlines()

  kmers = []
  for i in range(len(lines)):
    kmers.append(lines[i])

  fout = open("out.txt", "w")
  fout.write(OverlapString(kmers))
  fout.close() 

def OverlapString(kmers):
  graph = {}
  for kmer in kmers:
    graph[kmer] = []

  for key_source in graph:
    for key_to in graph:
      if key_source == key_to:
        continue
      if key_source[1:] == key_to[0:0+len(key_source[1:])]:
        graph[key_source] = graph[key_source] + [key_to]

  #reverse graph to find source node
  rev_graph = {}
  for key in graph:
    rev_graph[key] = []

  for key, value in graph.items():
    for node in value:
      rev_graph[node] = rev_graph[node] + [key]

  #find source node in graph by finding sink in reverse graph
  for key, value in rev_graph.items():
    if value == []:
      source = key
      break

  overlap_string = source
  current_node = source

  while graph[current_node] != []:
    print overlap_string
    print current_node
    print "--"
    current_node = graph[current_node][0]
    overlap_string += current_node[-1]

  print "---------"
  print overlap_string
  return overlap_string

if __name__ == '__main__':
  prob_198_3()