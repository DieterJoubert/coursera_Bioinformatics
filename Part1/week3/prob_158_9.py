from functions import *

def main():
  lines = open("data/dataset_158_9.txt").read().splitlines()
  k = int(lines[0])
  dna = []
  for line in lines[1:]:
    if line == "":
      break
    dna.append(line)

  fout = open("out/out_158_9.txt", "w")
  fout.write(median_string(dna, k))
  fout.close()  

if __name__ == "__main__":
  main()