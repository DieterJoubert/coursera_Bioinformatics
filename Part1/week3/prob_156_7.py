from functions import *

def main()):
  lines = open("data/dataset_156_7.txt").read().splitlines()
  k = int(lines[0].split()[0])
  d = int(lines[0].split()[1])
  dna = []
  for line in lines[1:]:
    if line == "":
      break
    dna.append(line)

  fout = open("out/out_156_7.txt", "w")
  fout.write(" ".join(motif_enumeration(dna, k, d)))
  fout.close()  

if __name__ == "__main__":
  main()