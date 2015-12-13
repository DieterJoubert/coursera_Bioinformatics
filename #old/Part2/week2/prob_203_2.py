def prob_203_2():
  lines = open("dataset_203_2.txt").read().splitlines()

  graph = {}
  for line in lines:
    split = line.split(" -> ")
    source = int(split[0])
    neighbors = split[1].split(",")
    neighbors = map(int, neighbors)
    graph[source] = neighbors

  fout = open("out.txt", "w")
  #fout.write(EulerianCycle(graph))
  fout.write("->".join(map(str, EulerianCycle(graph))))
  fout.close()

def Cycle(graph):
  for key, value in graph.items():
    if value != [] and value != None:
      current_node = key

  path = []
  start_node = current_node  

  while True:
    path.append(current_node)
    next_node = graph[current_node][0]
    graph[current_node].remove(next_node)
    current_node = next_node

    if start_node == current_node:
      path.append(current_node)
      break

  return (graph, path)

def AdditionalCycle(graph, path):
  found = False
  current_node = None
  start_index = None
  inner_path = []

  for i in range(len(path)):
    key = path[i]
    if graph[key] != [] and graph[key] != None:
      current_node = key
      found = True
      start_index = i
      break
  if found == False:
    return (graph, path)

  start_node = current_node  
  while True:
    inner_path.append(current_node)
    next_node = graph[current_node][0]
    graph[current_node].remove(next_node)
    current_node = next_node

    if start_node == current_node:
      inner_path.append(current_node)
      break

  print inner_path
  print path

  path = path[0:0+start_index] + inner_path[1:] + path[start_index:]

  return (graph, path)

def EulerianCycle(graph):
  (graph, path) = Cycle(graph)

  while True:
    (old_graph, old_path) = (graph, path)
    (graph, path) = AdditionalCycle(graph, path)
    if (old_graph, old_path) == (graph, path):
      break

  return path

if __name__ == '__main__':
  prob_203_2()