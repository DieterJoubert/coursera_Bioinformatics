from functions import *

def main():
  lines = open("data/dataset_160_9.txt").read().splitlines()
  k = int(lines[0].split()[0])
  t = int(lines[0].split()[1])
  dna = []
  for line in lines[1:]:
    if line == "":
      break
    dna.append(line.strip())

  fout = open("out/out_160_9.txt", "w")
  fout.write("\n".join(greedy_motif_search(dna,k,t)))
  fout.close()  

if __name__ == "__main__":
  main()