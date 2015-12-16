from functions import *

def prob_200_7():
  lines = open("data/dataset_200_7.txt").read().splitlines()
  patterns = []
  for line in lines:
    if line == "":
      break
    patterns.append(line.strip())

  graph = debruijn_from_kmers(patterns)

  fout = open("out/out_200_7.txt", "w")
  for key,value in graph.items():
    fout.write(key + " -> " + ",".join(value) + '\n')
  fout.close()  

if __name__ == "__main__":
  prob_200_7()