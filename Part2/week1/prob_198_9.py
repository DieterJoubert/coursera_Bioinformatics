from functions import *

def prob_198_9():
  lines = open("data/dataset_198_9.txt").read().splitlines()
  patterns = []
  for line in lines[0:]:
    if line == "":
      break
    patterns.append(line.strip())

  graph = overlap_adjacency_graph(patterns)

  fout = open("out/out_198_9.txt", "w")
  for (x,y) in graph:
    fout.write(x + " -> " + y + '\n')
  fout.close()  

if __name__ == "__main__":
  prob_198_9()