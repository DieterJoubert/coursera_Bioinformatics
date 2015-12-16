from functions import *

def prob_199_6():
  lines = open("data/dataset_199_6.txt").read().splitlines()
  k = int(lines[0])
  text = lines[1]

  graph = debruijn_k(k,text)

  fout = open("out/out_199_6.txt", "w")
  for key,value in graph.items():
    fout.write(key + " -> " + ",".join(value) + '\n')
  fout.close()  

if __name__ == "__main__":
  prob_199_6()